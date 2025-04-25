
import streamlit as st
import pickle
import numpy as np

# Load model and input columns
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("input_columns.pkl", "rb") as f:
    input_columns = pickle.load(f)

st.set_page_config(page_title="Conversion Prediction - Marketing ML", layout="centered")
st.title("🎯 Conversion Prediction using Logistic Regression")
st.markdown("""
This app uses a Logistic Regression model to predict whether a user will convert based on their ad exposure behavior.
""")
st.subheader("🔽 Enter user details:")

# Input widgets
test_group = st.selectbox("Test Group", ["PSA", "Ad"])
total_ads = st.slider("Total Ads Shown", 0, 50, 10)
most_ads_hour = st.slider("Hour with Most Ads (0-23)", 0, 23, 12)
most_ads_day = st.selectbox("Most Ads Day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Create input vector
input_data = np.zeros(len(input_columns))
input_data[input_columns.index("test group")] = 0 if test_group == "PSA" else 1
input_data[input_columns.index("total ads")] = total_ads
input_data[input_columns.index("most ads hour")] = most_ads_hour
day_col = f"most ads day_{most_ads_day}"
if day_col in input_columns:
    input_data[input_columns.index(day_col)] = 1

# Prediction
if st.button("Predict Conversion"):
    prediction = model.predict([input_data])[0]
    probability = model.predict_proba([input_data])[0][1]
    
    st.markdown("---")
    st.subheader("🔍 Prediction Result:")
    if prediction == 1:
        st.success(f"✅ This user is likely to convert! (Probability: {probability:.2%})")
    else:
        st.warning(f"❌ This user is unlikely to convert. (Probability: {probability:.2%})")

    st.markdown("### 📊 Model Insights")
    st.write("**Model Type**: Logistic Regression")
    st.write("**Business Use Case**: Predicting user conversion likelihood to improve ad targeting and marketing spend efficiency.")
    st.write("**Success Impact**: Helps reduce wasted ad impressions, improves ROI, and increases revenue through smarter targeting.")
    st.info("This model achieved a recall of 69% and AUC of 0.85 — excellent for identifying users who will convert.")
