#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk #Natural Language Toolkit
nltk.download('punkt')#unsupervised trainable model
nltk.download('wordnet')#is a lexical database of English.
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')#words that frequently appear in any language
nltk.download('omw-1.4')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords


# In[ ]:


#NLTK Stemmers. Interfaces used to remove morphological affixes from words, leaving only the word stem
from nltk.stem import PorterStemmer  #a process for removing suffixes from words in English.
from nltk.stem import LancasterStemmer #hat means it gets a certain string
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# # Reading from Text file

# In[ ]:


# text_2 = open('big.txt', "r")
with open('text3.txt', 'r') as file:
    text_op = file.read().replace('\n', '')
# text_op = text_2.readlines()


# In[ ]:


print(len(text_op))


# In[ ]:


text='I am sneha kadam'


# # Tokenization

# In[ ]:


tokens_sents = nltk.sent_tokenize(text_op)
print(tokens_sents)


# In[ ]:


tokens_words = nltk.word_tokenize(text_op)
print(tokens_words)


# # Stemming

# In[ ]:


# Stemming is a text preprocessing technique used in natural language processing (NLP) to reduce words to their root or base form


# In[ ]:


stem=[]
for i in tokens_words:
    ps = PorterStemmer()
    stem_word= ps.stem(i)
    stem.append(stem_word)
print(stem)


# # Lemmatization

# In[ ]:


# import nltk
# nltk.download('omw-1.4')


# In[ ]:


lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in stem])
print(lemmatized_output)


# In[ ]:


leme=[]
for i in stem:
    lemetized_word=lemmatizer.lemmatize(i)
    leme.append(lemetized_word)
print(leme)


# # POS (Parts of Speech) Tagging

# In[ ]:


print("Parts of Speech: ",nltk.pos_tag(leme))


# # Stopwords in sentence

# In[ ]:


sw_nltk = stopwords.words('english')
print(sw_nltk)


# # Words that aren't stopwords in sentence

# In[ ]:


# words = [word for word in text.split() if word.lower() not in sw_nltk]
# new_text = " ".join(words)
# print(new_text)


# # Calculating TF-IDF

# In[ ]:


text_op = []
with open('text3.txt', 'r') as file:
    for line in file:
        text_op.append(line)


# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


tr_idf_model  = TfidfVectorizer(stop_words='english')
corpus = text_op
tf_idf_vector = tr_idf_model.fit_transform(corpus)
print(corpus)


# In[ ]:


print(type(tf_idf_vector))
print(tf_idf_vector.shape)


# In[ ]:


tf_idf_array = tf_idf_vector.toarray()
print(tf_idf_array)


# In[ ]:


words_set = tr_idf_model.get_feature_names_out()
print(words_set)


# In[ ]:


import pandas as pd
df_tf_idf = pd.DataFrame(tf_idf_array, columns = words_set)

df_tf_idf.describe()


# In[ ]:


df_tf_idf


# In[ ]:





# In[ ]:





# In[ ]:




