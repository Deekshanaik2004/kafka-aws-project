#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps , loads
import json
from s3fs import S3FileSystem


# In[9]:


consumer = KafkaConsumer('project2' , bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: loads(x.decode('utf-8')))


# In[10]:


for c  in consumer:
    print(c.value)


# In[11]:


get_ipython().system('pip install s3fs')


# In[13]:


s3 = S3FileSystem()


# In[17]:


import json

for count, i in enumerate(consumer):
    with s3.open(f"s3://kafka-zomato-food-deeksha/zomato_food_{count}.json", "w") as file:
        json.dump(i.value, file)


# In[ ]:


for count, i in enumerate(consumer):
    with s3.open(f"s3://kafka-stock-market-deeksha/stock_market_{count}.json", "w") as file:
        json.dump(i.value, file)


# In[ ]:


import json
import s3fs

s3 = s3fs.S3FileSystem()

for count, i in enumerate(consumer):
    print("Received:", i.value)

    data = i.value   # ✅ already dict

    with s3.open(f"s3://kafka-stock-market-deeksha/stock_market_{count}.json", "w") as file:
        json.dump(data, file)

    print("Uploaded to S3:", count)


# In[7]:


import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")


# In[15]:


get_ipython().system('pip install --upgrade s3fs boto3 botocore aiobotocore')


# In[16]:


get_ipython().system('pip uninstall awscli -y')


# In[17]:


pip install --upgrade s3fs boto3


# In[18]:


import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")


# In[19]:


pip install botocore==1.42.73 s3transfer==0.16.0 boto3==1.42.73


# In[ ]:


import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")


# In[21]:


get_ipython().system('pip uninstall aiobotocore botocore boto3 s3fs awscli -y')


# In[22]:


pip install s3fs==2024.3.1 boto3==1.34.34 aiobotocore==2.12.3


# In[23]:


import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")


# In[25]:


python -m venv kafka-env


# In[3]:


import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from jupyter clean env")


# In[ ]:




