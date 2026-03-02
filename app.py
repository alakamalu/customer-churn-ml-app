from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model, scaler and features
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

# HOME PAGE

@app.route('/')
def home():
    return render_template("index.html", features=features, prediction=None)


# PREDICTION

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []

        # collect inputs in correct order
        for feature in features:

            value = request.form[feature]

            # categorical → encode
            if feature in encoders:
                value = encoders[feature].transform([value])[0]
            else:
                value = float(value)

            input_data.append(value)   

        # Convert to numpy array
        input_array = np.array([input_data])

        # Scale
        scaled_input = scaler.transform(input_array)

        # Probability
        probability = model.predict_proba(scaled_input)[0][1]
        percent = round(probability * 100, 2)

        # Yes / No prediction
        prediction_value = model.predict(scaled_input)[0]

        if prediction_value == 1:
            churn_result = "YES — Customer is likely to churn"
        else:
            churn_result = "NO — Customer is not likely to churn"

        # Risk level
        if percent < 40:
            risk = "LOW"
        elif percent < 70:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        # Final output
        result = f"""
Prediction: {churn_result}
Churn Probability: {percent}%
Risk Level: {risk}
"""

        return render_template(
            "index.html",
            features=features,
            prediction=result
        )

    except Exception as e:
        return render_template(
            "index.html",
            features=features,
            prediction=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)