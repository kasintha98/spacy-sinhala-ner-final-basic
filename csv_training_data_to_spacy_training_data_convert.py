import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import os

nlp = spacy.blank("si")  # load a new spacy model
db = DocBin()  # create a DocBin object
file_dir = 'C:/Users/SysAdminModule/Desktop/Research/spacy-sinhala-ner-final-basic/raw-files'
filename = 'annotations v1.0.json'

annotations = os.path.join(file_dir, filename)

f = open(annotations, encoding="utf8")
TRAIN_DATA = json.load(f)

for text, annot in tqdm(TRAIN_DATA['annotations']):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("./training_data_v1.0.spacy")  # save the docbin object
