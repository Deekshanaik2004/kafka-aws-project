# 🚀 Real-Time Data Streaming Pipeline using Kafka & AWS

## 📌 Overview

This project implements a real-time data streaming pipeline using Apache Kafka integrated with AWS services. The system ingests streaming data, processes it, and stores it in AWS S3 for analytics using AWS Glue and Athena.

---

## 🎯 Problem Statement

Modern applications generate continuous streams of data that require real-time processing and analysis. This project demonstrates how to build a scalable pipeline to handle such streaming data efficiently.

---

## ⚙️ Tech Stack

* Apache Kafka
* Python
* AWS S3
* AWS Glue
* AWS Athena

---

## 🏗️ Architecture

Producer → Kafka Topic → Consumer → AWS S3 → Glue Crawler → Athena

---

## 🔄 Workflow

1. Producer streams data to Kafka topic
2. Consumer reads data from Kafka
3. Data is uploaded to AWS S3
4. Glue crawler creates schema
5. Athena is used for querying

---

## 📂 Project Structure

kafka-aws-project/
│
├── src/
│   ├── producer.py
│   ├── consumer.py
│
├── notebooks/
│   ├── producer.ipynb
│   ├── consumer.ipynb
│
├── config/
│   └── config.yaml
│
├── data/
│   └── sample_zomato.csv
│
├── README.md
├── requirements.txt
└── .gitignore

---

## ▶️ How to Run

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Start Kafka

* Start Kafka Server

### 3. Run Producer

python src/producer.py

### 4. Run Consumer

python src/consumer.py

---

## ☁️ AWS Setup

1. Create S3 bucket
2. Configure AWS credentials
3. Create Glue crawler
4. Query data using Athena

---

## 📊 Dataset

A sample dataset is included.
Full dataset is not uploaded due to GitHub size limitations.

---

## 🚀 Key Features

* Real-time data streaming using Kafka
* Scalable storage with AWS S3
* Automated schema detection using Glue
* SQL-based analytics with Athena

---

## 💡 Future Improvements

* Add Spark Streaming
* Add CI/CD (Jenkins)
* Dockerize pipeline
* Build dashboard

---

## 👩‍💻 Author

Deeksha Naik
