**Repository Overview**

This GitHub repository contains the code and resources used for training models on the updated GeoCorpus-3 dataset. The dataset, which is also available on Hugging Face, includes both CoNLL-formatted and JSON files.

**Training Models**

To train a model, use the following command:

```bash
python3 main.py [MODEL] geocorpus [METRIC]
```

Where:
- `[MODEL]` should be replaced with the name of the model you want to train.
- `[METRIC]` should be either `micro_avg` or `macro_avg`, depending on the evaluation metric you wish to use.

**Models Configuration**

The available models are defined in the `main.py` file. To train new models, update the model dictionary in `main.py` with the desired model configurations.

**Files and Structure**

- **main.py:** Contains the code for training models using the Flair library and defines the available models and their configurations.
- **Corpus Files:**
  - **TXT (CoNLL format):** Located in the respective folders for model training.
  - **JSON:** Mirrors the format used in the Hugging Face dataset.

**Additional Resources**

- The updated GeoCorpus-3 dataset is described in the paper **"An Evaluation of Large Language Models for Geological Named Entity Recognition"**, which will be presented at the ICTAI 2024 conference. The preprint of the paper is available [here](#).
- The original GeoCorpus-3 dataset is detailed in [GeoCorpus-3](https://github.com/Petroles/Petrovec/tree/master/GeoCorpus%20V3) and the corresponding article can be found [here](https://www.sciencedirect.com/science/article/pii/S0166361520305819).
- For more details on the Hugging Face dataset, visit the [Hugging Face page](https://huggingface.co/datasets/ronunes/GeoCorpus-3v2).

**BibTeX**

Please cite the dataset and repository using the following BibTeX entry:

```bibtex
@inproceedings{YourCitationHere,
  title={NOME DO PAPER},
  author={Your Authors Here},
  booktitle={Proceedings of the 2024 IEEE International Conference on Tools with Artificial Intelligence (ICTAI)},
  year={2024},
  pages={},
  doi={},
  url={LINK},
}
```
