from bert_trainer.flair import Training
import sys
import time

sys.stderr = sys.stdout

#args
model_arg = sys.argv[1]
corpus_name = sys.argv[2]
metric_name = sys.argv[3]

#Model
models_info = {
    "BERTimbau": "neuralmind/bert-large-portuguese-cased", 
    "XLM-R-large": "FacebookAI/xlm-roberta-large",     
    }

model_checkpoint = models_info[model_arg]
model_name = model_arg

#Corpus
data_folder = f"corpora/{corpus_name}"

#Training hyperparameters
max_length = 512
truncation = True
lr = 2e-05
num_epochs = 10

metrics = {
    "micro_avg" : ("micro avg", "f1-score"),
    "macro_avg" : ("macro avg", "f1-score"),
}

main_evaluation_metric = metrics[metric_name]
metric = metric_name

#Technique
technique = "supervised"

#Number of folds
folds = 5

#Output
architecture = [model_name]

for use_crf in [True, False]:
    if use_crf:
        architecture.append("crf")
    else:
        architecture.append("linear")

    architecture_str = "_".join(architecture)

    #Cross-validationca

    for fold in range(folds):
        data_folder = f"corpora/{corpus_name}/labeled/{folds}folds/fold{fold}"
        output_dir_list = [technique, corpus_name, architecture_str, metric, f"{folds}folds", f"fold{fold}"]

        trainer = Training(data_folder, corpus_name, model_checkpoint, model_name, output_dir_list)

        print("================================")
        print("Starting training: {model_name}, {model_checkpoint}".format(model_name=model_name, model_checkpoint=model_checkpoint))
        print("Fold: {fold}/{folds}".format(fold=fold, folds=folds-1))
        print("================================")

        start_time = time.time()
        trainer.train(max_length, truncation, lr, num_epochs, use_crf, main_evaluation_metric)
        y_probs, metrics = trainer.get_and_save_metrics_test()
        print("--- %s seconds ---" % (time.time() - start_time))

        output_dir = trainer._create_directory_recursive(".", ["time"]+output_dir_list)

        with open(f"{output_dir}/time.txt", "w", encoding="utf-8") as f_out:
            print("%s seconds" % (time.time() - start_time), file=f_out)