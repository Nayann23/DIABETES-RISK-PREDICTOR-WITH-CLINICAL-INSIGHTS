
# DIABETES RISK PREDICTOR WITH CLINICAL INSIGHTS

**DIABETES RISK PREDICTOR WITH CLINICAL INSIGHTS** is an interactive Streamlit app that predicts the risk of diabetes using both numeric health metrics and clinical notes. It provides users with a prediction and the probability of developing diabetes, making it a useful tool for early risk assessment.

---

## Features

- Predicts diabetes risk using key health metrics: age, BMI, glucose level, blood pressure, insulin level
- Analyzes clinical notes using TF-IDF and machine learning
- Provides prediction probabilities for more informed decision-making
- Interactive web interface built with Streamlit

---

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/DIABETES-RISK-PREDICTOR-WITH-CLINICAL-INSIGHTS.git](https://github.com/your-username/DIABETES-RISK-PREDICTOR-WITH-CLINICAL-INSIGHTS.git)

2.  Navigate into the project directory:
    ```bash
    cd DIABETES-RISK-PREDICTOR-WITH-CLINICAL-INSIGHTS
    ```
3.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4.  Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

-----

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Input the required health metrics and clinical notes in the web interface.

Click **Predict** to see the diabetes risk prediction and probability.

-----

## Model & Data

  - Uses a Random Forest Classifier trained on a diabetes dataset
  - Numeric features are scaled using a saved scaler
  - Clinical notes are transformed using a TF-IDF vectorizer
  - Numeric and text features are combined for final prediction

-----

## Contributing

Contributions are welcome\! Open issues or submit pull requests to improve the app.

-----

## License

This project is licensed under the MIT License.

```

```
