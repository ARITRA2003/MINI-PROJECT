#Feature Enginering is nothing 
#but primitive ways to represent
# a text into Number
#Approaches
#1)Label  Encoding
#2)One Hot Encoding
#3)Bag of words
#4)TF-IDF
#5)Word Embedding

# 1)Label Encoding
# suppose we have a vocabulary vector having 
# each word given a specific index
# In label Encoding we take a sentence and
# accoring to the vocabulary array , we give 
# that index numbers to each words and store into an 
# array
# using that array, we convert the similarity between 
# 2 sentences

# 2)one Hot Encoding
# It is a very similar approach to the previous one
# We do have the same vocabulary array
# Difference here is that here we will create arrays for
# each of the words having size that of the vocabulary 
# array.In those word arrays,we will assign the word index 
# from the vocabulary array as '1' and others as '0'
# That's how,we will compare the two texts

# Disadvantages of above two approaches
# 1)one hot encoding the meaning of the word in an
# accurate way.
# Example:
# 'I need help' and 'I need assistance' both have similar 
# meaning but we will not get the same using 
# using one hot encoding
# 2)Here, we are using vecotor for each word 
# so, a lot of meomory is needed 
# 3)out of vocabulary
# 4)No fixed length representation for texts
# ML expects similar kind of size of data sets
# so,it is a disadvantage

# 3)using bag of Words
# Here a sentence will have a vocalualy array size
# Here all the words present in the array will be '1' 
# others will be '0'
# Disadvantage:
# 1)large pace required
# 2)Do not capture the meaning of the sentence accurately 
import pandas as pd
import numpy as np

