from flask import Flask, render_template, request
from pathlib import Path
import joblib
import numpy as np

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "phishing_model.joblib")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.joblib")
feature_names = joblib.load(BASE_DIR / "feature_names.joblib")

def extract_suspicious_words(X_vector):
    coefs = model.coef_[0]
    X_array = X_vector.toarray()[0]
    word_scores = X_array * coefs

    top_indices = np.argsort(word_scores)[-8:][::-1]

    suspicious = []
    for idx in top_indices:
        if word_scores[idx] > 0:
            suspicious.append(feature_names[idx])

    return suspicious

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        email = request.form["email"]
        X = vectorizer.transform([email])
        label = model.predict(X)[0]
        prob = model.predict_proba(X)[0][label]

        suspicious_words = extract_suspicious_words(X) if label == 1 else []

        result = {
            "label": "Phishing" if label == 1 else "Legitimate",
            "confidence": round(prob, 3),
            "words": suspicious_words
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
