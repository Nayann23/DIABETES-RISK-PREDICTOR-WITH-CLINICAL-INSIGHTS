# Diabetes Risk Predictor with Clinical Insights

## Overview
This project provides a **Diabetes Risk Predictor** web application built using **Streamlit**. It predicts the likelihood of diabetes based on user-provided health metrics and clinical notes using a **pre-trained Random Forest Classifier**.

---

## Setup

### 1. Navigate to the project directory
```bash
cd DIABETES-RISK-PREDICTOR-WITH-CLINICAL-INSIGHTS
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
3. Install required packages
```
pip install -r requirements.txt

```

4. Usage
Run the Streamlit app

```
streamlit run app.py

```
Input the required health metrics and clinical notes in the web interface.
Click Predict to see the diabetes risk prediction and probability.

----

Model & Data
The dataset and pre-trained Random Forest model are too large to store in this repository. Download them from Google Drive and place them in the project directory:
Diabetes Dataset CSV
Random Forest Model Pickle

---

Model Details

Random Forest Classifier trained on the diabetes dataset.
Numeric features scaled using a saved scaler.
Clinical notes transformed using a TF-IDF vectorizer.

---
Both numeric and text features are combined for final prediction.
