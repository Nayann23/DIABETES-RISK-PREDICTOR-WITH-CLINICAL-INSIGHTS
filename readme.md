# Diabetes Risk Predictor with Clinical Insights

## Overview
This project is a **Diabetes Risk Predictor** web application developed using **Streamlit**. It predicts the likelihood of diabetes by analyzing both **user-provided health metrics** and **clinical notes**, utilizing a **pre-trained Random Forest Classifier** for accurate results. The application provides both risk prediction and probability insights for better clinical understanding.

---

Download rf_model.pkl here: ``` https://drive.google.com/file/d/1RQHWS73rzflpqD2SKBbEgPAkXws5ZSIk/view?usp=drive_link ```

---

## Setup
1. Navigate to the project directory
cd DIABETES-RISK-PREDICTOR-WITH-CLINICAL-INSIGHTS

---
2. Create and activate a virtual environment (recommended)
```
python -m venv venv           # Create a virtual environment named 'venv'
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate       # On Windows

```
---
### 3. Run the Streamlit app
```
 streamlit run app.py

```
---

Open the web interface in your browser.
Input the required health metrics (e.g., age, BMI, blood pressure, glucose levels).
Provide clinical notes for additional context.
Click Predict to get both the diabetes risk prediction and probability score.

--- 

## Model & Data

Note: The dataset and pre-trained Random Forest model are too large to include in this repository. Download them from Google Drive and place them in the project directory:
- Diabetes Dataset CSV
- Random Forest Model Pickle

---

## Model Details

Algorithm: Random Forest Classifier trained on the diabetes dataset.
Numeric Features: Scaled using a saved scaler for consistency.
Text Features: Clinical notes transformed using a TF-IDF vectorizer.
Feature Combination: Both numeric and textual features are combined to make the final prediction.
Output: Provides a clear probability score along with the prediction (diabetic/non-diabetic).

---

## Improvements Added

1. Clarified instructions for virtual environment activation on both Linux/macOS and Windows.
2. Added detailed steps for inputting health metrics and clinical notes.
3. Emphasized output details: prediction and probability.
4. Structured sections for easier readability.
5. Added brief explanation of model workflow and feature handling.

---


