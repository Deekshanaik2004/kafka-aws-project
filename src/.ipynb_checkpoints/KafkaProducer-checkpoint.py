
import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json





producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = lambda x:
                         dumps(x).encode('utf-8'))





producer.send('project2', value= {'name':'Deeksha'})





import pandas as pd





df = pd.read_csv("zomato_small.csv")





df.drop("url" ,  axis=1)





df = df.sample(n=5000, random_state=42)





df




df.sample(1).to_dict(orient = "records")[0]





import time
while True:
    data = df.sample(1).to_dict(orient="records")[0]
    producer.send('project2', value=data)
    producer.flush()   # 👈 IMPORTANT
    print("Sent:", data)
    time.sleep(1)





producer.flush()





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




while True:
    producer.send('project1' , value = data)
    





while True:
    stock = df.sample(1).to_dict(orient = "records")[0]
    producer.send('project1' , value = stock)

