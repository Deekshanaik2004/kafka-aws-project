#!/usr/bin/env python
# coding: utf-8

# In[27]:


get_ipython().system('pip install kafka-python')


# In[28]:


import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json


# In[29]:


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = lambda x:
                         dumps(x).encode('utf-8'))


# In[30]:


producer.send('project2', value= {'name':'Deeksha'})


# In[31]:


import pandas as pd


# In[32]:


df = pd.read_csv("zomato.csv")


# In[33]:


df.drop("url" ,  axis=1)


# In[34]:


df = df.sample(n=5000, random_state=42)


# In[35]:


df


# In[36]:


df.sample(1).to_dict(orient = "records")[0]


# In[39]:


import time
while True:
    data = df.sample(1).to_dict(orient="records")[0]
    producer.send('project2', value=data)
    producer.flush()   # 👈 IMPORTANT
    print("Sent:", data)
    time.sleep(1)


# In[12]:


producer.flush()


# In[ ]:


import requests

url = "https://pizza-and-desserts.p.rapidapi.com/pizzas"

headers = {
	"x-rapidapi-key": "07bed90cc0msh0176ef69f59c718p1a0186jsnf286fbda9188",
	"x-rapidapi-host": "pizza-and-desserts.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

data = response.json()
print(data)


# In[ ]:


while True:
    producer.send('project1' , value = data)
    


# In[ ]:


while True:
    stock = df.sample(1).to_dict(orient = "records")[0]
    producer.send('project1' , value = stock)

