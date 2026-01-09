# 🛡️ Phishing Email Detector

An AI-powered web application that analyzes email text and detects phishing attempts using machine learning.  
The system provides **confidence scores**, **explainable predictions**, and highlights the **most suspicious words** that influenced each decision.

Built with Python, scikit-learn, and Flask.

---

## 🚀 Features

- 🔍 Detects phishing vs legitimate emails  
- 🧠 Machine-learning model using TF-IDF + Logistic Regression  
- 📊 Confidence scoring  
- 🚩 Suspicious word extraction for explainability  
- 🖥️ Clean web interface with red/green indicators  
- 🧪 Local, fast, and fully offline  

---

## 🧱 Tech Stack

- Python 3  
- scikit-learn  
- Flask  
- HTML / CSS  
- joblib  

---

## 🏗️ Project Structure

Phishing Email Detector/
│
├── app.py
├── phishing_model.joblib
├── tfidf_vectorizer.joblib
├── feature_names.joblib
│
├── templates/
│ └── index.html
│
└── static/
├── style.css
└── favicon.ico
