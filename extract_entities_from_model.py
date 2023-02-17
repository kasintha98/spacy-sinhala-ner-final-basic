import spacy

nlp_ner = spacy.load("./model-best")


class ExtractEntitiesFromModel:

    @staticmethod
    def extract_entities(text):
        doc = nlp_ner(text)
        entities = []

        for ent in doc.ents:
            match_obj = {"entity": ent.label_,
                         "value": ent.text,
                         "text": ent.text, "startChar": ent.start_char,
                         "endChar": ent.end_char, "extractedBy": "spacy_model"}
            entities.append(match_obj)

        return entities
