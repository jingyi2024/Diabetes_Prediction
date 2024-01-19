# Diabetes Prediction

This project focuses on predicting diabetes using various machine learning models. The aim is to accurately identify potential diabetes cases based on a set of health-related parameters.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

### About the Dataset
The Diabetes Prediction Dataset consists of medical and demographic data of patients along with their diabetes status (positive or negative). The dataset contains various features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. These features are used to predict whether a patient has diabetes or not.

## Business Case Scenario:
  Enhancing Diabetes Diagnosis and Empowering Healthcare Providers for Early Diagnosis.

## Problem Statement
  Diabetes remains a prevalent chronic disease, affecting millions worldwide. Diabetes is characterized by high blood sugar levels, which can lead to serious complications if left untreated. Collaborative efforts between the healthcare system and the insurance industry by implementing the risk assessment models.

## Solution
- Collaborative Data Sharing Platform for Machine Learning Algorithms Integrating the Electronic Health Record (EHR) systems enables healthcare providers to identify patients at high risk for diabetes early on. Deploying Machine Learning models would predict the likelihood of a person developing diabetes with the help of their complete health records. This would lead to providing efficient medications and treatment.
- Collaboration between healthcare providers and insurance companies in diabetes care can lead to better outcomes for patients, more accurate risk assessment models, and cost savings for everyone involved. By using data-driven insights and promoting collaboration, this initiative can pave the way for a more effective and efficient healthcare system.

## Conclusions & Recommendations
### Conclusion:
- We tried multiple models to find key factors contributing to diabetes in a person based in their medical data.
Final Model is Logistic regression with threshold of 0.5 which have less false negative rate. Thus Healthcare and Insurance providers can use this data to identify the person with diabetes early on.

### Recommendations:
- The highest percentage of individuals with diabetes falls within the 70-79 age group, followed by the 60-69 and 50-59 age groups. Conversely, the lowest prevalence of diabetes is observed in the 0-19 age group.
Age Group < 29 -> 1% Age Group 30 - 59 -> 15% Age Group 60+ -> 86% Early detection of diabetes are crucial for younger and middle-aged adults, as they are less likely to develop diabetes but may have undiagnosed diabetes. On the other hand, interventions focused on managing diabetes and preventing complications are crucial for older adults, who have a higher risk of developing diabetes and its related complications. It is important to prioritize such interventions based on the age group and their respective risks.

- A weak positive correlation exists between BMI and diabetes, with a correlation value of 0.20. Increased BMI can lead to insulin resistance and inflammation, contributing to the development of diabetes. However, other factors can also affect the development of diabetes, and high BMI does not guarantee it.
If you are concerned about your risk of developing diabetes, there are a number of things you can do to reduce your risk:

- Maintain a healthy weight. A BMI of 18.5 to 24.9 is considered healthy. Further, when HbA1c and Blood Glucose level increases in the blood, the person needs to take care of his health because the increase in the HbA1c and blood glucose level would lead to diabetes maintaining the optimal level of HbA1c and blood glucose level is important for the person. When it comes to prior health conditions such as hypertension and heart disease, 3 in 10 people with hypertension would have a chance of diabetes. There is a one in five people having heart disease would have the chance of having diabetes.
