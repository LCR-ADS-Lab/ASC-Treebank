The following commands were run in Terminal to train the model:

```python
#convert IOB to spacy docs:
python3 -m spacy convert assets corpus --n-sents 1

#train spacy ner model
python3 -m spacy train config.cfg --output training/

#evaluate model accuracy
python3 -m spacy evaluate training/model-best corpus/test.spacy --output training/test_metrics.json

```