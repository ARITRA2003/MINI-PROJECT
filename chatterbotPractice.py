from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
import random
import string
spacy.load('en_core_web_sm')


convo=[

"what do you do?",
"I am made to give Information about IIEST SHIBPUR college.",

"What else can you do?",
"I can help you know more about IIEST SHIBPUR",
    
"what is science?",
"Science is a systematic endeavor that builds and organizes knowledge in the form of testable explanations and predictions about the universe. The earliest written records of identifiable predecessors."


"Details about IIEST SHIBPUR"
"Indian Institute of Engineering Science and Technology, Shibpur (IIEST Shibpur), erstwhile Bengal Engineering College (also known as B.E. College), formerly Bengal Engineering and Science University (also known as BESU), is a public research university also a National Institute of Technology located at Shibpur, Howrah, West Bengal."
]

s="sorry,but I do not understand"
bot=ChatBot(
	'IIEST SHIBPUR CHATBOT',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': s,
        'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.db'
)

trainer = ListTrainer(bot)
trainer.train(convo)

greet_inputs=("hello","hi","whatsapp","how are you",'hey')
greet_responses=("Hey","Hey there!",'Hi')

def greet(sentence):
	for word in sentence.split():
		if word.lower() in greet_inputs:
			return random.choice(greet_responses)

count=0;

flag=True
print("Hello I am a chatbot, you can ask questions . I will try to answer.")


while (flag==True):
	user_response=input("You: ")
	# user_response=user_response.lower()
	if(user_response!="bye"):
		if(user_response=="thank you" or user_response=="thanks"):
			count=0
			print('bot:',"You are most Welcome")
			flag=False
		elif greet(user_response)!=None:
			count=0
			print('bot:',greet(user_response))
		else:
			answer=bot.get_response(user_response)
			print('bot:',answer)
	else:
	    flag=False,print('bot:',"Goodbye,Thank You for visiting!..")