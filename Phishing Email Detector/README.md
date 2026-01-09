🛡️ Phishing Email Detector
An AI-powered web application that analyzes email text and detects phishing attempts using machine learning.
The system provides confidence scores, explainable predictions, and highlights the most suspicious words that influenced each decision.
Built with Python, scikit-learn, and Flask.
🚀 Features:

🔍 Detects phishing vs legitimate emails
🧠 Machine-learning model using TF-IDF + Logistic Regression
📊 Confidence scoring
🚩 Suspicious word extraction for explainability
🖥️ Clean web interface with red/green indicators
🧪 Local, fast, and fully offline

🧱 Tech Stack
Python 3
scikit-learn
Flask
HTML / CSS
joblib

    
⚡ Quick Start:
1️⃣ Install dependencies
python3 -m pip install flask scikit-learn joblib
2️⃣ Run the application
python3 app.py
3️⃣ Open in your browser
http://127.0.0.1:5000
Paste any email content into the text box and click Analyze Email.

🧪 How It Works:
Email text is converted to TF-IDF features
A Logistic Regression model predicts phishing probability
The app displays:
Final decision (Phishing / Legitimate)
Confidence score
Suspicious words responsible for the decision

📌 Example Use Cases:
Cybersecurity training
Email security analysis
Machine learning portfolio project
SOC tool demonstration


Built by Nathan Mascarenhas
