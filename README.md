## 📊 Customer Churn Prediction — End-to-End ML Project

This project is a complete end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn.

The system takes customer details as input, processes them using trained ML preprocessing steps, and provides:

* Churn prediction (YES / NO)
* Churn probability (%)
* Risk level (LOW / MEDIUM / HIGH)

The model is deployed as an interactive web application.

## 🚀 Project Highlights

- Real-world business problem (customer retention)
- Full ML pipeline from data to deployment
- Feature selection using Random Forest importance
- Logistic Regression classification model
- Data preprocessing with encoding and scaling
- Interactive web interface using Flask
- Dropdown handling for categorical features
- Probability-based risk classification
- Cloud deployment ready


## 🧠 Machine Learning Workflow

1. Data loading and cleaning
2. Handling missing values
3. Label encoding categorical variables
4. Feature selection using feature importance
5. Feature scaling using StandardScaler
6. Train-test split
7. Model training and evaluation
8. Model selection based on recall and ROC-AUC
9. Saving model and preprocessing objects
10. Web deployment using Flask


## 🤖 Model Used

Logistic Regression was selected because:

* Higher recall for churn class
* Better ROC-AUC score
* Interpretable predictions
* Stable performance


## 📥 Input Features

The web application accepts the following customer attributes:

* Total Charges
* Monthly Charges
* Tenure
* Contract Type
* Payment Method
* Online Security
* Tech Support

Categorical features are selected using dropdown menus and automatically encoded.


## 📈 Output Provided

The system predicts:

* Whether customer will churn (YES / NO)
* Probability of churn
* Risk level classification

Example output:

```
Prediction: YES — Customer is likely to churn
Churn Probability: 82%
Risk Level: HIGH
```

## 🖥️ Web Application

The trained model is integrated into a Flask web app that:

* Accepts user inputs
* Applies encoding and scaling
* Generates predictions instantly
* Displays results in a professional UI


## 📂 Project Structure

```
churn_web_app/
│
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── features.pkl
├── encoders.pkl
├── requirements.txt
├── render.yaml
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML / CSS
* Gunicorn


## 🌐 Live Demo

```
https://your-live-app-url
```


## 🎯 Business Value

Customer churn prediction helps companies:

* Identify high-risk customers
* Take retention actions early
* Reduce revenue loss
* Improve customer satisfaction


## 👨‍💻 Author

Machine Learning project built for real-world predictive analytics and deployment practice.
