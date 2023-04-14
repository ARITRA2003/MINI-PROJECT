import spacy
nlp=spacy.load("en_core_web_sm")
doc = nlp("Captain america ate 100$ of samosa. Then he said I can do this all day.")
for token in doc:
    print(token, " | ", spacy.explain(token.pos_), " | ", token.lemma_)

source_nlp = spacy.load("en_core_web_sm")

nlp = spacy.blank("en")
nlp.add_pipe("ner", source=source_nlp)
print(nlp.pipe_names)

doc = nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents:
    print(ent.text, ent.label_)