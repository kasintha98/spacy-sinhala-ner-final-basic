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
        entities = [{"text": ent.text, "entity": ent.label_, "value": ent.ent_id_, "startChar": ent.start_char,
                     "endChar": ent.end_char, "confidence": 100, "extractedBy": "gazetteer_matcher"} for ent in
                    doc.ents]
        return entities

    @staticmethod
    def tag_fuzzy_entities_from_text(text):
        fuzzy_entities = FuzzyMatcher.tag_entities_from_fuzzy_matcher(text, patterns)
        return fuzzy_entities

    @staticmethod
    def tag_model_entities_from_text(text):
        model_entities = ExtractEntitiesFromModel.extract_entities(text)
        return model_entities

    @staticmethod
    def combine_all_extracted_entities(extracted_gazetteer_entities, extracted_fuzzy_entities,
                                       extracted_spacy_model_entities, extracted_bert_model_entities):

        all_objects = extracted_gazetteer_entities + extracted_fuzzy_entities + extracted_spacy_model_entities + extracted_bert_model_entities
        x = extracted_gazetteer_entities + extracted_fuzzy_entities + extracted_spacy_model_entities + extracted_bert_model_entities
        similar_objects = []
        for i, obj1 in enumerate(all_objects):
            for obj2 in all_objects[i + 1:]:
                if obj1["text"] == obj2["text"]:
                    similar_objects.append(obj1)
                    similar_objects.append(obj2)

        overlapped_entities = {(obj["text"], obj["extractedBy"]): obj for obj in similar_objects}.values()
        overlapped_entity_list = list(overlapped_entities)

        non_overlapped_entity_list = all_objects
        for obj in overlapped_entity_list:
            non_overlapped_entity_list.remove(obj)

        for item in non_overlapped_entity_list:
            print(item)

        print("**********************************************")
        cleaned_overlaps = ExtractEntities.get_unique_entities_from_duplicate_picks(overlapped_entity_list)
        for item in cleaned_overlaps:
            print(item)

        final_list = ExtractEntities.get_final_filtered_list(cleaned_overlaps + non_overlapped_entity_list)

        return final_list

    @staticmethod
    def resolve_overlapping_entities(entitiesObj):
        entities = [(entity["value"], entity["startChar"], entity["endChar"]) for entity in entitiesObj]
        print("len", len(entities))
        resolved_entities = []
        entity_starts = [entity[1] for entity in entities]
        print("entity_starts", entity_starts)
        entity_ends = [entity[2] for entity in entities]
        sorted_entities = sorted(zip(entity_starts, entity_ends, entities))
        print("sorted_entities", sorted_entities)
        current_entity_start, current_entity_end, current_entity = sorted_entities[0]
        for entity_start, entity_end, entity in sorted_entities[1:]:
            if entity_start <= current_entity_end:
                current_entity_end = max(current_entity_end, entity_end)
            else:
                resolved_entities.append((current_entity_start, current_entity_end, current_entity[0]))
                current_entity_start, current_entity_end, current_entity = entity_start, entity_end, entity
        resolved_entities.append((current_entity_start, current_entity_end, current_entity[0]))
        print("resolved_entities")
        for rs in resolved_entities:
            print(rs)
        return resolved_entities

    @staticmethod
    def get_unique_entities_from_duplicate_picks(duplicate_picks):
        result = []
        priorityList = ["gazetteer_matcher", "fuzzy_matcher", "spacy_model", "xlm-roberta_model"]
        for i in range(len(duplicate_picks)):
            for j in range(i + 1, len(duplicate_picks)):
                if duplicate_picks[i]["text"] == duplicate_picks[j]["text"]:
                    if duplicate_picks[i]["entity"] != duplicate_picks[j]["entity"]:
                        # print("No",duplicate_picks[i]["extractedBy"], duplicate_picks[i]["entity"],duplicate_picks[j]["extractedBy"],duplicate_picks[j]["entity"])
                        if priorityList.index(duplicate_picks[i]["extractedBy"]) < priorityList.index(
                                duplicate_picks[j]["extractedBy"]):
                            if next((x for x in result if
                                     x["value"] == duplicate_picks[i]["value"] and x["entity"] == duplicate_picks[i][
                                         "entity"]), None) is None:
                                result.append(duplicate_picks[i])
                                break
                    else:
                        duplicate_picks[i]["extractedBy"] = duplicate_picks[i]["extractedBy"] + "+" + \
                                                            duplicate_picks[j]["extractedBy"]
                        result.append(duplicate_picks[i])
                        break

        return result

    @staticmethod
    def get_final_filtered_list(all_list):
        print(len(all_list))
        filtered_entities = all_list
        a = []

        #for i in range(len(all_list)):
        #    for j in range(i + 1, len(all_list)):
         #       print(all_list[i]["startChar"], all_list[j]["startChar"], all_list[i]["value"], "and",
          #            all_list[i]["endChar"], all_list[j]["endChar"], all_list[j]["value"])
         #       if all_list[i]["startChar"] >= all_list[j]["startChar"] and all_list[i]["endChar"] <= all_list[j][
          #          "endChar"]:
          #          print(all_list[i]["value"])
          #          a.append(all_list[i])
           #         filtered_entities.remove(all_list[i])

        for i, obj1 in enumerate(all_list):
            for obj2 in all_list[i + 1:]:
                if obj1["startChar"] >= obj2["startChar"] and obj1["endChar"] <= obj2["endChar"]:
                    filtered_entities.remove(obj1)
                    a.append(obj1)

        print("AA", a)
        print(len(filtered_entities))
        return filtered_entities
