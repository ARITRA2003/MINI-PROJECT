import spacy
nlp=spacy.load("en_core_web_sm")

doc=nlp("wow! I am a boy.Mr. I love mango,guava etc.")

for token in doc:
  print(token,'|', token.pos_,'|',spacy.explain(token.pos_))

text='''Mukesh Dhirubhai Ambani (born 19 April 1957) is an Indian billionaire businessman. He is the chairman and managing director of Reliance Industries Ltd. (RIL), a Fortune Global 500 company and India's most valuable company by market value.[4] According to Bloomberg Billionaires Index, Ambani's net worth is estimated at $83.4 billion as of February 2023, making him the richest person in Asia and the 10th richest person in the world.[5][6][7]

Early life '''
doc=nlp(text)
for token in doc:
  if token.tag_ not in['SPACE','X','PUNCT']:
    print(token,'|', token.tag_,'|',spacy.explain(token.tag_))

count=doc.count_by(spacy.attrs.POS)

for k,v in count.items():
  print(doc.vocab[k].text,'|',v)

# Named Entity Recognition (NER)
print(nlp.pipe_names)

for i in doc.ents:
  print(i,'|',i.label_,'|',spacy.explain(i.label_))

print(nlp.pipe_labels['ner'])

# pre-trained model nlp is not perfect.
# so,we use custom NER

print(type(doc[2:5]))

from spacy.tokens import Span
s1=Span(doc,5,6,label="ORG")

doc.set_ents([s1],default="unmodified")

for i in doc.ents:
  print(i,'|',i.label_,'|',spacy.explain(i.label_))


text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""

doc = nlp(text)

count=0;
for i in doc.ents:
  if i.label_ in ["GPE"]:
    count=count+1
    print(i)

print(count)

text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
and finally Ricky ponting was born on 19 December 1974."""

doc = nlp(text)
count=0;
for i in doc.ents:
  if i.label_ in ["DATE"]:
    count=count+1
    print(i)

print(count)

print(count)