import spacy
nlp = spacy.load('en_core_web_sm')

def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
text = "Microsoft Corporation is headquartered in Redmond,Washington."
entities = perform_ner(text)
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
