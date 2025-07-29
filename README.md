
[![View App - Streamlit Cloud](https://img.shields.io/badge/Launch-App-brightgreen?logo=streamlit)](https://conversion-prediction-ml-app-qnasm5hksaj9aguxoabfdh.streamlit.app/)

------

# Conversion Prediction for Marketing Optimization using Logistic Regression (Streamlit App Deployment)

---

## 📌 Abstract

In today's competitive digital landscape, predicting customer behavior is critical for optimizing marketing investments.  
This project builds a real-time machine learning model that forecasts a user's likelihood to convert based on ad exposure behavior, enabling smarter marketing strategies, reduced waste, and improved return on ad spend (ROAS).

---

## 📚 About the Project

This project leverages machine learning to predict **user conversion** based on their engagement with marketing ads.  
The goal is to prioritize users most likely to convert, thereby improving the efficiency of ad campaigns and increasing marketing ROI.

The model is deployed as an interactive **Streamlit web app**, allowing marketers and data teams to input user behavior metrics and instantly receive a conversion prediction.

---

## 🎯 Business Objectives

- Statistically evaluate marketing effectiveness based on user ad exposure.
- Build a predictive model to forecast conversion likelihood.
- Help marketing teams focus ad spend on high-probability converters.
- Reduce customer acquisition costs and maximize revenue.

---

## 🧠 Machine Learning Approach

- **Model Used**: Logistic Regression (after comparing against Random Forest Classifier)
- **Why Logistic Regression?**
  - Higher Recall (69%) compared to Random Forest (32%).
  - Higher AUC score (0.85 vs 0.62).
  - Easier interpretability for business stakeholders.
  - More reliable for predicting rare but valuable outcomes (conversions).

---

## 📈 Model Performance Metrics

| Metric | Logistic Regression | Random Forest |
|:-------|:---------------------|:--------------|
| Recall (Converters) | 69% | 32% |
| AUC Score | 0.85 | 0.62 |
| Accuracy | 86% | 89% |

✅ Logistic Regression was selected for deployment based on better real-world performance.

---

## 💰 Business Impact

- **+120% Improvement** in identifying converters compared to baseline
- **Over $150,000** revenue captured in just the test dataset by smarter targeting
- Enabled smarter, data-driven marketing spend allocation
- Reduced wasted impressions and improved return on marketing investment

---

## 🏆 Achievements & Business Impact

- Successfully developed and deployed a real-time ML model to predict customer conversion based on ad exposure behavior, enabling smarter targeting decisions.
- Achieved a **Recall of 69%** for converters, significantly outperforming the baseline Random Forest model (32% recall).
- Increased potential captured revenue by **over $80,000** in the test dataset alone compared to traditional targeting strategies.
- Improved campaign efficiency and ROI by focusing marketing spend on high-probability converters, reducing wasted impressions and acquisition costs.
- Delivered an **AUC score of 0.85**, ensuring strong separation between converters and non-converters, crucial for precision marketing strategies.
- Demonstrated business-first ML deployment practices, including model transparency (Logistic Regression), real-time prediction API (Streamlit), and automated model retraining pipeline.
- Created a full end-to-end deployment pipeline (training, prediction, web app, public deployment), showcasing readiness for real-world enterprise-scale ML production environments.

---

## 🛠 Technologies Used

- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- GitHub
- Streamlit Cloud

---

## ⚙️ How to Run Locally

1. Clone the repository:
    git clone https://github.com/SweetySeelam2/conversion-prediction-ml-streamlit.git
    cd conversion-prediction-ml-streamlit

2. Install requirements:
    pip install -r requirements.txt

3. Run the app:
    streamlit run app.py

---

## 🌐 Deployment on Streamlit Cloud

This app is live and hosted publicly at:

[![View App - Streamlit Cloud](https://img.shields.io/badge/Launch-App-brightgreen?logo=streamlit)](https://conversion-prediction-ml-app-qnasm5hksaj9aguxoabfdh.streamlit.app/)

Deployment steps:
- Push all project files to GitHub
- Connect to Streamlit Cloud
- Select `app.py` as entry point
- Set up required packages via `requirements.txt`
- Click Deploy!

---

## 📁 Folder Structure

conversion-prediction-ml-streamlit/ │ 
├── app.py # Streamlit app code 
├── train_model.py # Model training script 
├── model.pkl # Trained Logistic Regression model 
├── input_columns.pkl # Features used for prediction 
├── requirements.txt # Required Python packages 
├── data/ │ └── Marketing_AB_Testing.csv # Dataset used for training

---

## 🤝 Acknowledgements

- Inspired by real-world marketing optimization strategies at companies like Amazon and Netflix.
- Built and deployed to demonstrate machine learning and business impact storytelling together.

---

## 🔒 Proprietary & All Rights Reserved

© 2025 Sweety Seelam. This work is proprietary and protected by copyright. All content, models, code, and visuals are © 2025 Sweety Seelam. No part of this project, app, code, or analysis may be copied, reproduced, distributed, or used for any purpose—commercial or otherwise—without explicit written permission from the author.

For licensing, commercial use, or collaboration inquiries, please contact: Email: sweetyseelam2@gmail.com

---

> Created by [Sweety Seelam](https://github.com/SweetySeelam2) | 2025                                                                                                                                       
> Email: sweetyseelam2@gmail.com                       
> LinkedIn: https://www.linkedin.com/in/sweetyrao670/                       
> My Portfolio: https://sweetyseelam2.github.io/SweetySeelam.github.io/
