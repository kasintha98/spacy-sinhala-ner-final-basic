from tqdm import tqdm
import json
import os
import requests
import csv
from check_entities import ExtractEntities

file_dir = 'C:/Users/SysAdminModule/Desktop/Research/spacy-sinhala-ner-final-basic/raw-files'
filename = 'testdata v1.1.json'

annotations = os.path.join(file_dir, filename)

f = open(annotations, encoding="utf8")
TRAIN_DATA = json.load(f)

predictions = []


class EvaluateAllModels:

    @staticmethod
    def get_predictions(model_type):
        for text, annot in tqdm(TRAIN_DATA['annotations']):
            extracted_entities = []

            if model_type == "spacy":
                extracted_entities = ExtractEntities.tag_model_entities_from_text(text)

            if model_type == "all":
                text_no_punc = ExtractEntities.remove_punctuation_from_text(text)
                extracted_gazetteer_entities = ExtractEntities.tag_gazetteer_entities_from_text(text)
                extracted_fuzzy_entities = ExtractEntities.tag_fuzzy_entities_from_text(text)
                extracted_spacy_model_entities = ExtractEntities.tag_model_entities_from_text(text)
                extracted_bert_model_entities = {}

                # get BERT model predictions
                text_for_bert = {
                    "text": text_no_punc
                }
                res = requests.post(url="http://localhost:6000/check-entities", json=text_for_bert)

                if res and res.status_code == 200:
                    extracted_bert_model_entities = res.json()["extractedEntitiesFromModel"]

                extracted_entities = ExtractEntities.combine_all_extracted_entities(extracted_gazetteer_entities,
                                                                                          extracted_fuzzy_entities,
                                                                                          extracted_spacy_model_entities,
                                                                                          extracted_bert_model_entities)

            for start, end, label in annot["entities"]:
                predicted_label = "OTHER"
                for extraction in extracted_entities:
                    if extraction["startChar"] == start and extraction["endChar"] == end:
                        # print("picked", text[start:end], label)
                        predicted_label = extraction["entity"]

                predictions.append([text[start:end], label, predicted_label, model_type])

        with open('predictions_output.csv', 'w', newline='', encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(["value", "target", "prediction", "predicted_by"])

            for item in enumerate(predictions):
                row = [item[1][0], item[1][1], item[1][2], item[1][3]]
                writer.writerow(row)
