import spacy
import re
nlp=spacy.blank("en")
doc=nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for token in doc:
   print(token)

print(doc[0])

doc=nlp("I like INR 1000 and two rupees ")
span=doc[0:3]
print(span)
print(type(span))

token0=doc[0]

print(token0)


# print(dir(token0))

print(token0.is_alpha)
print(token0.like_num)

token2=doc[2]

print(token2.like_num)

token1=doc[4]

print(token1.like_num)
print(token1.is_alpha)

for token in doc:
   print(token,"=> index: ",token.i ,"like_num:" ,token.like_num ,"is_alpha",token.is_alpha,"is_currency",token.is_currency,"is_punct",token.is_punct)

with open("Student.txt") as f:
   text=f.readlines()

print(text)

# Connecting every array elements using space
text = " ".join(text)
print(text)

pattern='[a-zA-z0-9_]*@[a-zA-z0-9_]*\.[a-zA-z0-9_]*'
matches=re.findall(pattern,text)
print(matches)

doc=nlp(text)
emails=[]
for token in doc:
   if(token.like_email):
      emails.append(token)

print(emails)

from spacy.symbols import ORTH

nlp = spacy.blank("en")
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]

print(tokens)

nlp.tokenizer.add_special_case("gimme", [
    {ORTH: "gim"},
    {ORTH: "me"},
])
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]
print(tokens)

#To ensure the splitting of a text into sentences
nlp.add_pipe('sentencizer')

doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for sentence in doc.sents:
    print(sentence)

text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

doc=nlp(text)

urls=[]

for token in doc:
   if(token.like_url):
    urls.append(token)

print(urls)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
doc=nlp(transactions)

ans=[]

for token in doc:
   if(token.is_currency):
      print(doc[(token.i-1)],doc[(token.i)])
