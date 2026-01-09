import pandas as pd
from pathlib import Path

CLEAN_DIR = Path("../data/cleaned")
MASTER_DIR = Path("../data/master")
MASTER_DIR.mkdir(parents=True, exist_ok=True)

dfs = []

for file_path in CLEAN_DIR.glob("*.csv"):
    print(f"Loading {file_path.name}...")
    try:
        df = pd.read_csv(
            file_path,
            sep=None, 
            engine="python", 
            encoding="latin-1",
            on_bad_lines="skip"
        )
        df = df[['text', 'label']]  # Keep only these columns
        dfs.append(df)
    except Exception as e:
        print(f"⚠ Failed to load {file_path.name}: {e}")

# Merge all successfully loaded datasets
if dfs:
    master_df = pd.concat(dfs, ignore_index=True)
    master_df = master_df.sample(frac=1, random_state=42).reset_index(drop=True)
    master_file = MASTER_DIR / "emails_master.csv"
    master_df.to_csv(master_file, index=False)
    print(f"✅ Master dataset created: {master_file}")
    print(f"Total rows: {len(master_df)}")
else:
    print("❌ No datasets were successfully loaded.")
