from check_entities import ExtractEntities

bert = [
        {
            "endChar": 8,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 0,
            "text": "මහාචාර්ය",
            "value": "මහාචාර්ය"
        },
        {
            "endChar": 15,
            "entity": "DATE",
            "extractedBy": "xlm-roberta_model",
            "startChar": 9,
            "text": "දසුන්,",
            "value": "දසුන්,"
        },
        {
            "endChar": 10,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 9,
            "text": "අද",
            "value": "අද"
        },
        {
            "endChar": 27,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 19,
            "text": "පෙරවරුවේ",
            "value": "පෙරවරුවේ"
        },
        {
            "endChar": 35,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 28,
            "text": "බැංකොක්",
            "value": "බැංකොක්"
        },
        {
            "endChar": 39,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 36,
            "text": "සිට",
            "value": "සිට"
        },
        {
            "endChar": 45,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 40,
            "text": "ශ්‍රී",
            "value": "ශ්‍රී"
        },
        {
            "endChar": 51,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 46,
            "text": "ලංකාව",
            "value": "ලංකාව"
        },
        {
            "endChar": 55,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 52,
            "text": "වෙත",
            "value": "වෙත"
        },
        {
            "endChar": 65,
            "entity": "PERSON",
            "extractedBy": "xlm-roberta_model",
            "startChar": 56,
            "text": "පැමිනියා.",
            "value": "පැමිනියා."
        }
    ]

spacy = [
        {
            "confidence": 100,
            "endChar": 14,
            "entity": "PERSON",
            "extractedBy": "spacy_model",
            "startChar": 0,
            "text": "මහාචාර්ය දසුන්",
            "value": "මහාචාර්ය දසුන්"
        },
        {
            "confidence": 100,
            "endChar": 18,
            "entity": "DATE",
            "extractedBy": "spacy_model",
            "startChar": 16,
            "text": "අද",
            "value": "අද"
        },
        {
            "confidence": 100,
            "endChar": 51,
            "entity": "LOCATION",
            "extractedBy": "spacy_model",
            "startChar": 40,
            "text": "ශ්‍රී ලංකාව",
            "value": "ශ්‍රී ලංකාව"
        }
    ]

fuzzy = [
        {
            "confidence": 100,
            "endChar": 35,
            "entity": "LOCATION",
            "extractedBy": "fuzzy_matcher",
            "startChar": 28,
            "text": "බැංකොක්",
            "value": "බැංකොක් (Bangkok)"
        }
    ]

gaze = [
        {
            "confidence": 100,
            "endChar": 35,
            "entity": "LOCATION",
            "extractedBy": "gazetteer_matcher",
            "startChar": 28,
            "text": "බැංකොක්",
            "value": "බැංකොක් (Bangkok)"
        },
        {
            "confidence": 100,
            "endChar": 51,
            "entity": "LOCATION",
            "extractedBy": "gazetteer_matcher",
            "startChar": 40,
            "text": "ශ්‍රී ලංකාව",
            "value": "ශ්‍රී ලංකාව (Sri Lanka)"
        }
    ]

result = []
# result = ExtractEntities.combine_all_extracted_entities(gaze, fuzzy, spacy, bert)
print("result..................")

for item in result:
    print(item)


#text = ExtractEntities.remove_punctuation_from_text("මහාචාර්ය දසුන්, අද පෙරවරුවේ බැංකොක් සිට ශ්‍රී ලංකාව වෙත පැමිනියා.")

#print(text)

# a = ExtractEntities.remove_stop_words_from_picked_entity(None)
