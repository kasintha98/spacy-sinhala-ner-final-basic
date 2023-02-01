from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from check_entities import ExtractEntities
import json
import requests

# create an instance of flask
app = Flask(__name__)
# creating an API object
api = Api(app)


# Command Start Server On Port:5000 -> flask run
# For Post request to http://localhost:5000/check-entities
class CheckEntities(Resource):
    def post(self):
        if request.is_json:
            text = request.json['text']
            extracted_gazetteer_entities = ExtractEntities.tag_gazetteer_entities_from_text(text)
            extracted_fuzzy_entities = ExtractEntities.tag_fuzzy_entities_from_text(text)
            extracted_spacy_model_entities = ExtractEntities.tag_model_entities_from_text(text)
            extracted_bert_model_entities = {}

            # get BERT model predictions
            text_for_bert = {
                "text": text
                }
            res = requests.post(url="http://localhost:6000/check-entities", json=text_for_bert)

            if res and res.status_code == 200:
                extracted_bert_model_entities = res.json()["extractedEntitiesFromModel"]

            # return a json response
            return make_response(jsonify({'text': text, 'extractedGazetteerEntities': extracted_gazetteer_entities, 'extractedFuzzyEntities': extracted_fuzzy_entities, 'extractedEntitiesFromSpacyModel':extracted_spacy_model_entities, 'extractedEntitiesFromBertModel': extracted_bert_model_entities}), 200)
        else:
            return {'error': 'Request must be JSON'}, 400


api.add_resource(CheckEntities, '/check-entities')

#
if __name__ == '__main__':
    app.run(debug=True)
