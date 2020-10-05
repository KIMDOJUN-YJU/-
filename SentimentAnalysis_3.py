#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models import Word2Vec


# In[2]:


file_stop_word=open('불용어','r',-1,'utf-8')


# In[3]:


file_stop_word.close()


# In[4]:


file_samsung = open('samsung0.txt','r',-1,'utf-8')


# In[5]:


file_samsung.close()


# In[6]:


stop_words=file_stop_word.read()


# In[7]:


file_stop_word=open('불용어','r',-1,'utf-8')


# In[8]:


file_samsung = open('samsung0.txt','r',-1,'utf-8')


# In[9]:


stop_words=file_stop_word.read()


# In[10]:


samsungs_words=file_samsung.read()


# In[11]:


stop_word_list=[]
for i in stop_words.split(','):
    if i not in stop_word_list:
        stop_word_list.append(i)


# In[12]:


len(stop_word_list)


# In[13]:


samsungs_words


# In[14]:


import re
hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
samsungs_words=hangul.sub('',samsungs_words)


# In[15]:


samsungs_words=samsungs_words.split()


# In[16]:


samsungs_words


# In[17]:


samsungs_words_list=[]
for i in samsungs_words:
    if i not in stop_word_list:
        samsungs_words_list.append(i)


# In[18]:


samsungs_words_list


# In[19]:


import csv


# In[20]:


table= dict()


# In[21]:


with open('polarity.csv','r', -1,'utf-8') as polarity:
    next(polarity)
    
    for line in csv.reader(polarity):
        key = str()
        for word in line[0].split(';'):
            key += word.split('/')[0]
        
        table[key]= {'Neg':line[3], 'Neut': line[4], 'Pos':line[6]}


# In[22]:


with open('polarity.csv','r', -1,'utf-8') as polarity:
    next(polarity)
    
    for line in csv.reader(polarity):
        key = str()
        for word in line[0].split(';'):
            key += word.split('/')[0]
        
        table[key]= {'Neg':line[3], 'Neut': line[4], 'Pos':line[6]}


# In[23]:


table['희박']


# In[24]:


words=['협상','결렬','중단','취소']

negative=0
neutral=0
positive=0
for word in words:
    if word in table:
        negative += float(table[word]['Neg'])
        neutral += float(table[word]['Neut'])
        positive += float(table[word]['Pos'])


# In[25]:


negative


# In[26]:


positive


# In[27]:


neutral


# In[28]:


negative=0
neutral=0
positive=0
for word in samsungs_words_list:
    if word in table:
        negative += float(table[word]['Neg'])
        neutral += float(table[word]['Neut'])
        positive += float(table[word]['Pos'])


# In[29]:


negative


# In[30]:


neutral


# In[31]:


positive


# In[ ]:




