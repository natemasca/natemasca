import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# --- Load cleaned master dataset ---
df = pd.read_csv("../data/master/emails_master.csv")

# Drop rows with missing text or label
df = df.dropna(subset=["text", "label"])
df["label"] = df["label"].astype(int)

# Features and labels
X = df["text"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model (choose one)
model = LogisticRegression(max_iter=1000)
#model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "phishing_model.joblib")
joblib.dump(vectorizer, "tfidf_vectorizer.joblib")
print("✅ Model and vectorizer saved")
