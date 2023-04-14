import spacy
nlp=spacy.load("en_core_web_sm")

doc=nlp("I am a boy.Mr. I love mango,guava etc.")

for sentence in doc.sents:
  print(sentence)

for sentence in doc.sents:
  for word in sentence:
    print(word)


