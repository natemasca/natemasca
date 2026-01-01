import joblib

# --- Load trained model and vectorizer ---
model = joblib.load("phishing_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

def predict_email(email_text):
    """
    Predict whether an email is phishing or legitimate.
    Returns a string and probability.
    """
    # Transform text to TF-IDF features
    X = vectorizer.transform([email_text])
    
    # Predict label
    label = model.predict(X)[0]
    
    # Predict probability
    prob = model.predict_proba(X)[0][label]  # confidence in predicted class
    
    if label == 1:
        return f"⚠ Phishing Email (Confidence: {prob:.2f})"
    else:
        return f"✅ Legitimate Email (Confidence: {prob:.2f})"

# --- Example usage ---
if __name__ == "__main__":
    while True:
        email_text = input("\nEnter email text (or 'exit' to quit):\n")
        if email_text.lower() == "exit":
            break
        result = predict_email(email_text)
        print(result)
