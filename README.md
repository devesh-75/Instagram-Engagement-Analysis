\# Instagram User Engagement Analysis



\### Big Data Project using PySpark and Machine Learning



\---



\## 1. Introduction



This project analyzes Instagram user engagement using Big Data technologies and Machine Learning. It simulates how large-scale platforms process user interaction data and generate insights for content optimization.



\---



\## 2. Problem Statement



The objective of this project is to analyze large-scale Instagram engagement data and build a predictive model that classifies posts into high or low engagement categories using PySpark.



\---



\## 3. Dataset



\### Overview



\* Synthetic dataset generated using Python

\* Total records: 1000+

\* Designed to simulate real-world Instagram data



\### Features Used



\* Likes, Comments, Shares, Saves

\* Followers

\* Views, Watch Time

\* Hashtags Count, Caption Length

\* Posted Hour

\* Post Type (Image, Reel, Video)



\---



\## 4. System Architecture



\### Flow Diagram



Raw Data Generation (Python)

↓

Data Storage (CSV)

↓

Data Loading (PySpark)

↓

Data Cleaning \& Validation

↓

Exploratory Data Analysis

↓

Feature Engineering (Engagement Score)

↓

Feature Transformation (VectorAssembler)

↓

Machine Learning Model (Logistic Regression)

↓

Prediction (High / Low Engagement)

↓

Results \& Insights



\---



\## 5. Tools and Technologies



\* Python

\* PySpark (Distributed Data Processing)

\* Spark MLlib (Machine Learning)

\* NumPy

\* Git and GitHub



\---



\## 6. Working Methodology



\### 6.1 Data Generation



A synthetic dataset was generated using Python to simulate Instagram-like engagement data.



\### 6.2 Data Processing



Data was loaded into PySpark DataFrames for distributed processing and scalability.



\### 6.3 Data Cleaning



Null values were checked and handled to ensure data consistency.



\### 6.4 Exploratory Data Analysis



\* Calculated average likes, comments, and shares

\* Compared engagement across post types

\* Identified best posting hours



\### 6.5 Feature Engineering



Engagement Score formula:



\*\*Engagement Score = (Likes + Comments + Shares) / Followers\*\*



\### 6.6 Feature Transformation



\* StringIndexer → Converts categorical data into numeric form

\* VectorAssembler → Combines features into a single vector



\### 6.7 Machine Learning



\* Algorithm Used: Logistic Regression

\* Library: Spark MLlib

\* Task: Binary Classification (High vs Low Engagement)



\---



\## 7. Results and Insights



\### Key Metrics



\* Average Likes: \~5185

\* Average Comments: \~271

\* Average Shares: \~518



\### Observations



\* Reels show slightly higher engagement compared to images and videos

\* Evening hours (19–21) produce maximum engagement

\* Engagement depends strongly on interaction metrics and follower count



\### Model Performance



\* Accuracy: \~99% (due to synthetic dataset)

\* Model successfully classifies engagement levels



\---



\## 8. Technical Highlights



\* Distributed data processing using PySpark

\* Feature engineering for normalized engagement metrics

\* Use of MLlib for scalable machine learning

\* End-to-end pipeline from raw data to prediction

\* Simulation of real-world recommendation systems



\---



\## 9. Conclusion



This project demonstrates how Big Data tools like PySpark can be used to analyze large-scale social media data and build predictive models for engagement.



\---



\## 10. Future Scope



\* Integration with real-world Instagram API data

\* Use of advanced ML models (Random Forest, Gradient Boosting)

\* Deployment using Flask or Streamlit

\* Real-time data processing using Kafka

\* Dashboard visualization



\---



\## 11. How to Run



```bash

pip install pyspark numpy

python generate\_data.py

python analysis.py

```



\---



