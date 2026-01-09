import pandas as pd
import re
from bs4 import BeautifulSoup
from pathlib import Path

RAW_DIR = Path("../data/raw")
CLEAN_DIR = Path("data/cleaned")
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

# --- Define per-file column mapping ---
# key = filename, value = {"text": text_column_name, "label": label_column_name}
COLUMN_MAP = {
    "Enron.csv": {"text": "body", "label": "label"},
    "CEAS_08.csv": {"text": "body", "label": "label"},
    "Ling.csv": {"text": "body", "label": "label"},
    "Nazario.csv": {"text": "body", "label": "label"},
    "Nigerian_Fraud.csv": {"text": "body", "label": "label"},
    "SpamAssasin.csv": {"text": "body", "label": "label"}
}

def remove_html(text):
    soup = BeautifulSoup(str(text), "html.parser")
    return soup.get_text()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

def clean_file(file_path, text_col, label_col):
    df = pd.read_csv(file_path)

    # Keep only valid labels (0 or 1)
    df = df[df[label_col].isin([0, 1])]

    # Clean and normalize text
    df[text_col] = df[text_col].astype(str).apply(remove_html).apply(clean_text)

    # Keep only relevant columns
    df = df[[text_col, label_col]]
    df.columns = ["text", "label"]

    return df

# --- Loop over all files ---
for file_path in RAW_DIR.glob("*.csv"):
    filename = file_path.name
    if filename in COLUMN_MAP:
        print(f"Cleaning {filename}...")
        cols = COLUMN_MAP[filename]
        cleaned_df = clean_file(file_path, cols["text"], cols["label"])
        cleaned_df.to_csv(CLEAN_DIR / filename, index=False)
        print(f"✅ Saved cleaned file: {CLEAN_DIR / filename}")
    else:
        print(f"⚠ Skipping {filename}: no column mapping defined")

print("✅ All datasets processed")
