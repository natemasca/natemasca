
import joblib
import numpy as np

# --- Load trained model and vectorizer ---
model = joblib.load("scripts/phishing_model.joblib")
vectorizer = joblib.load("scripts/tfidf_vectorizer.joblib")
feature_names = joblib.load("scripts/feature_names.joblib")

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


def predict_email(email_text):
    X = vectorizer.transform([email_text])
    label = model.predict(X)[0]
    prob = model.predict_proba(X)[0][label]

    if label == 1:
        suspicious_words = extract_suspicious_words(X)
        return {
            "label": "Phishing",
            "confidence": round(prob, 3),
            "suspicious_words": suspicious_words
        }
    else:
        return {
            "label": "Legitimate",
            "confidence": round(prob, 3),
            "suspicious_words": []
        }

# --- Example usage ---
if __name__ == "__main__":
    while True:
        email_text = input("\nPaste email text (or 'exit'):\n")
        if email_text.lower() == "exit":
            break

        result = predict_email(email_text)

        print(f"\n🧾 Result: {result['label']}")
        print(f"📊 Confidence: {result['confidence']}")

        if result["suspicious_words"]:
            print("🚩 Suspicious words:", ", ".join(result["suspicious_words"]))

