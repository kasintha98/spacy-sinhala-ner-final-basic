import spacy
from spacy.lang.si import Sinhala
from gazetteer_converter import GazetteerConverter
from fuzzy_matcher import FuzzyMatcher
from extract_entities_from_model import ExtractEntitiesFromModel

nlp = Sinhala()
ruler = nlp.add_pipe("entity_ruler")
patterns = GazetteerConverter.get_patterns()
ruler.add_patterns(patterns)

nlp_ner = spacy.load("./model-best")


class ExtractEntities:

    @staticmethod
    def tag_gazetteer_entities_from_text(text):
        doc = nlp(text)
        entities = [{"text": ent.text, "entity": ent.label_, "value": ent.ent_id_, "startChar": ent.start_char, "endChar": ent.end_char} for ent in doc.ents]
        return entities

    @staticmethod
    def tag_fuzzy_entities_from_text(text):
        fuzzy_entities = FuzzyMatcher.tag_entities_from_fuzzy_matcher(text, patterns)
        return fuzzy_entities

    @staticmethod
    def tag_model_entities_from_text(text):
        model_entities = ExtractEntitiesFromModel.extract_entities(text)
        return model_entities
