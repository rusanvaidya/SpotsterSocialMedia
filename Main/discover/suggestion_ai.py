#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
from psycopg2 import sql
import pandas as pd
import pandas.io.sql as sqlio


# In[2]:


conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
query1 = 'SELECT * FROM "complete_userdetails"'
conn.autocommit = True
dataset1 = sqlio.read_sql_query(query1,conn)


# In[3]:


dataset1


# In[4]:


conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
query2 = 'SELECT * FROM "discover_interest"'
conn.autocommit = True
dataset2 = sqlio.read_sql_query(query2,conn)
dataset2


# In[5]:


conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
query3 = 'SELECT * FROM "discover_followers_follow_me"'
conn.autocommit = True
dataset3 = sqlio.read_sql_query(query3,conn)
dataset3


# In[6]:


dataset = pd.DataFrame(columns=['owner_id', 'Interests_id', 'following_to'])
dataset


# In[12]:


features = ['Interests_id', 'following_to']
label = ['owner_id']
#     print(ident,d1)


# In[13]:


values = []
key = []
follow = []
for i in range(0,len(dataset1)):
    list_interest = []
    x = dataset1['user_interest'][i]
    x = x.replace("'","")
    x = x.strip('][').split(', ')
    # print(x)
    for j in x:
        d2 = dataset2.loc[dataset2['my_interest']==j]
        for k in d2['id']:
            unique_id = dataset3['registration_id'].unique()
            for ident in unique_id:
                d3 = dataset3.loc[dataset3['registration_id']==ident]
                d1 = []
                for d in d3['followers_id']:
                    d1.append(d)
                    if ident==dataset1['owner_id'][i]:
                        for dz in d1:
                            values.append(k)
                            key.append(dataset1['owner_id'][i])
                            follow.append(dz)


# In[14]:


dataset['owner_id'] = key
dataset['Interests_id'] = values
dataset['following_to'] =follow


# In[15]:


dataset


# In[16]:


own_id = int(input("Enter id : "))
print(own_id)
train_data = dataset.loc[dataset['owner_id']!=own_id]
x_train = train_data[features]
y_train = train_data[label]

test = dataset.loc[dataset['owner_id']==own_id]
test = test[features]
test


# In[20]:


from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np


# In[21]:


loaded_model = pickle.load(open('RandomForest', 'rb'))
predicted_id_rfc = loaded_model.predict(test)
bbb = list(np.unique(predicted_id_rfc))
print(bbb)


# In[22]:


for i in dataset1.loc[dataset1['id']==own_id]['user_interest']:
    print(i)
print(own_id)


# In[23]:


for i in bbb:
    bb = dataset1.loc[dataset1['id']==i]['user_interest']
    print(bb)


# In[24]:


b0 = list(np.unique(test['following_to']))


# In[25]:


suggest_list = []
for num_id in bbb:
    if num_id in b0:
        pass
    else:
        suggest_list.append(num_id)
print(suggest_list)
for i in suggest_list:
    bb = dataset1.loc[dataset1['id']==i]['user_interest']
    print(bb)


# In[ ]:




