# Regex in customer support
import re
#Retrive Email id or phone
chat1 = 'codebasics: you ask lot of questions 😠  1235678912, abc@xyz.com'
chat2 = 'codebasics: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'codebasics: yes, phone: 1235678912 email: abc@xyz.com'
pattern='(\(\d{3}\)-\d{3}-\d{4})|(\d{10})'
matches=re.findall(pattern,chat3)
print(matches)

pattern='[a-zA-z0-9_]*@[a-zA-z0-9_]*\.[a-zA-z0-9_]*'
matches=re.findall(pattern,chat2)
print(matches)

chat1='codebasics: Hello, I am having an issue with my order # 412889912'
chat2='codebasics: I have a problem with my order number 412889912'
chat3='codebasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$'

pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
print(matches)

def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]

# Information Extraction
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
(m. 2000; div. 2008)
Talulah Riley
(m. 2010; div. 2012)
(m. 2013; div. 2016)
'''
   

def extract_personal_Information(text):
	age=get_pattern_match('age (\d+)',text)
	Name=get_pattern_match('Born(.+)',text)
	Birth=get_pattern_match('Born.+\n(.+)\(age',text)
    Birthplace=get_pattern_match('\(age \d+\)\n(.+)',text)
	print(age)
	print(Name)
	print(Birth)

	extract_personal_Information(text)
