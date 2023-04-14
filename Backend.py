import numpy 
import string 
import random
import spacy

# Reading the corpus of the text

f=open("Student.txt",'r',errors='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
# print(raw_doc)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
# sentence_tokens=nltk.sent_tokenize(raw_doc)
word_tokens=nltk.word_tokenize(raw_doc)
performing pre-procesing steps
from nltk.stem import WordNetLemmatizer
lemmer = WordNetLemmatizer()
def Lemtokens(tokens):
	return [lemmer.lemmatize(token) for token in tokens]
remove_punc_dict=dict((ord(punct), None)for punct in string.punctuation)
def LemNormalize(text):
	return Lemtokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))
# print(word_tokens)
# print(sentence_tokens)
# Responses for greeting
greet_inputs=("hello","hi","whatsapp","how are you",'hey')
greet_responses=("Hey","Hey there!",'Hi')

def greet(sentence):
	for word in sentence.split():
		if word.lower() in greet_inputs:
			return random.choice(greet_responses)

# Response Generation by the bot
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
	bot_response=''
	TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
	tfidf=TfidfVec.fit_transform(sentence_tokens)
	vals=cosine_similarity(tfidf[-1],tfidf)
	idx=vals.argsort()[0][-2]
	flat=vals.flatten()
	flat.sort()
	req_tfidf=flat[-2]
	if(req_tfidf==0):
		bot_response=bot_response+ "I am sorry.I cann't understand"
		return bot_response
	else:
		bot_response=bot_response+sentence_tokens[idx]
		return bot_response

# Main code
flag=True
print("Hello I am a chatbot, you can ask questions . I will try to answer.")

while (flag==True):

	user_response=input()
	user_response=user_response.lower()
	if(user_response!="bye"):
		if(user_response=="thank you" or user_response=="thanks"):
			print("You are most Welcome")
			flag=False
		elif greet(user_response)!=None:
			print(greet(user_response))
		else:
			sentence_tokens.append(user_response)
			word_tokens=word_tokens+nltk.word_tokenize(user_response)
			final_words=list(set(word_tokens))
			print(response(user_response))
			sentence_tokens.remove(user_response)
	else:
	    flag=False,print("Goodbye")