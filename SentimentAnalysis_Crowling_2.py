#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Okt 
import re
from collections import Counter
import pytagcloud
import pygame


# In[2]:


from konlpy.tag import Hannanum
from konlpy.tag import Kkma


# In[3]:


from datetime import datetime
from pandas.tseries.offsets import Day
from dateutil.parser import parse


# In[4]:


stop_word_list=[]
def ds_trans(x):
    current_ds=''
    if len(str(x.month))==1 and len(str(x.day))==1 :
        current_ds='.0'.join([str(x.year),str(x.month),str(x.day)])
    elif len(str(x.month))==1 and len(str(x.day))==2 :
        current_ds='.0'.join([str(x.year),str(x.month)])
        current_ds='.'.join([current_ds, str(x.day)])  
    elif len(str(x.month))==2 and len(str(x.day))==1 :
        current_ds='.'.join([str(ds.year),str(x.month)])
        current_ds='.0'.join([current_ds, str(x.day)])    
    else :
        current_ds='.'.join([str(x.year),str(x.month), str(x.day)])
    return current_ds


# In[5]:


def de_trans(x):
    current_de=''
    if len(str(x.month))==1 and len(str(x.day))==1 :
        current_de='.0'.join([str(x.year),str(x.month),str(x.day)])
    elif len(str(x.month))==1 and len(str(x.day))==2 :
        current_de='.0'.join([str(x.year),str(x.month)])
        current_de='.'.join([current_de, str(x.day)])  
    elif len(str(x.month))==2 and len(str(x.day))==1 :
        current_de='.'.join([str(x.year),str(x.month)])
        current_de='.0'.join([current_de, str(x.day)])    
    else :
        current_de='.'.join([str(x.year),str(x.month), str(x.day)])
    return current_de


# In[6]:


def get_title_url(page_num, URL, query, per):
    ds=datetime.now()
    de=datetime.now()
    for day in range(per):
        currently_ds=ds+Day(-day) 
        currently_de=de+Day(-day)
        current_ds=ds_trans(currently_ds)
        current_de=de_trans(currently_de)
        print(ds_trans(currently_ds))
        print(de_trans(currently_de))
        current_page_num=0
        whole_url=''
        for i in range(page_num):
            current_page_num = (0+i)*11
            whole_url= URL+query+'&sm=tab_pge&sort=0&pd=3&ds='+current_ds+'&de='+current_de+'&start='+str(current_page_num)
            print(whole_url)
            source_url = urllib.request.urlopen(whole_url) #url 오픈 
            soup = BeautifulSoup(source_url, 'lxml', from_encoding='utf-8') #soup에 저장
            for title in soup.find_all('dd','txt_inline'):
                title_link = title.find('a')
                title_link = title_link['href']
                if title_link != '#':
                    print(day)
                    get_text(title_link,day)


# In[7]:


def get_text(url,day):
    source_Url = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_Url, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
        print(text)
        cleaned_text = re.sub('[a-zA-Z]', '', text)
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
        noun_text(cleaned_text,day)
        
def noun_text(Text,day):
    splitter = Okt()
    Okt_tagger=splitter.pos(Text)
    for i in Okt_tagger:
        if i[1] == 'Josa' or i[1] == 'Punctuation' or i[1] == 'Conjunction':
            file_name='불용어'
            outputfile=open(file_name,'a',-1,'utf-8')
            outputfile.write(str(i[0]))
            outputfile.write(',')
            outputfile.close()     

#     nouns = splitter.nouns(Text)
#     tag = count.most_common(100)

#     file_name='불용어'
#     outputfile=open(file_name,'a',-1,'utf-8')
#     outputfile.write(str(stop_word_list))
#     outputfile.close()     
#     print('ok')


# In[8]:


get_title_url(5,'https://search.naver.com/search.naver?&where=news&query=',query='%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90',per=3)


# In[9]:


file_test=open('불용어','r',-1,'utf-8')
Text=file_test.read()


# In[10]:


Text


# In[11]:


Text=Text.split(',')


# In[12]:


stop_word_list=[]
for i in Text:
    if i not in stop_word_list:
        stop_word_list.append(i)


# In[13]:


stop_word_list


# In[14]:


file_test.close()


# In[15]:


stop_words=file_stop_word.read()


# In[ ]:




