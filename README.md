# BERT_CRF
BERT_CRF model for Name Entity Recognition in pytorch</br>
Dataset source: https://github.com/synalp/NER</br>conlleval.py downloaded from: https://github.com/sighsmile/conlleval

For traninig a model: python bert_crf.py --mode train <br>
For testing the model: python bert_crf.py --mode test <br>
You can check the notebook at https://github.com/Dhanachandra/bert-crf4NER/blob/master/bert-crf4NER/bert_crf_4_ner_training.ipynb



## usage:
train model:

```
python bert_NER.py --mode train

### with crf:
python bert_crf.py --mode train
```

Evaluate model
```
python bert_NER.py --mode test

### with crf:
python bert_crf.py --mode test
