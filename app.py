from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from check_entities import ExtractEntities

# create an instance of flask
app = Flask(__name__)
# creating an API object
api = Api(app)


# For Post request to http://localhost:5000/check-entities
class CheckEntities(Resource):
    def post(self):
        if request.is_json:
            text = request.json['text']
            extracted_gazetteer_entities = ExtractEntities.tag_gazetteer_entities_from_text(text)
            extracted_fuzzy_entities = ExtractEntities.tag_fuzzy_entities_from_text(text)
            extracted_model_entities = ExtractEntities.tag_model_entities_from_text(text)
            # return a json response
            return make_response(jsonify({'text': text, 'extractedGazetteerEntities': extracted_gazetteer_entities, 'extractedFuzzyEntities': extracted_fuzzy_entities, 'extractedEntitiesFromModel':extracted_model_entities}), 200)
        else:
            return {'error': 'Request must be JSON'}, 400


api.add_resource(CheckEntities, '/check-entities')

#
if __name__ == '__main__':
    app.run(debug=True)
