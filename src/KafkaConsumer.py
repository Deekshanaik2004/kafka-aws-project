


import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps , loads
import json
from s3fs import S3FileSystem





consumer = KafkaConsumer('project2' , bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: loads(x.decode('utf-8')))





for c  in consumer:
    print(c.value)










s3 = S3FileSystem()





import json

for count, i in enumerate(consumer):
    with s3.open(f"s3://kafka-zomato-food-deeksha/zomato_food_{count}.json", "w") as file:
        json.dump(i.value, file)





for count, i in enumerate(consumer):
    with s3.open(f"s3://kafka-stock-market-deeksha/stock_market_{count}.json", "w") as file:
        json.dump(i.value, file)




import json
import s3fs

s3 = s3fs.S3FileSystem()

for count, i in enumerate(consumer):
    print("Received:", i.value)

    data = i.value   # ✅ already dict

    with s3.open(f"s3://kafka-stock-market-deeksha/stock_market_{count}.json", "w") as file:
        json.dump(data, file)

    print("Uploaded to S3:", count)




import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")























import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")











import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")
















import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from python")









import s3fs

s3 = s3fs.S3FileSystem()

with s3.open("s3://kafka-stock-market-deeksha/test.txt", "w") as f:
    f.write("hello from jupyter clean env")






