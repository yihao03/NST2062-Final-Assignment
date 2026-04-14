import pandas as pd
from pathlib import Path

# utility cell to validate if wrong answers are actually wrong
csv_to_inspect = "./part1_outputs/model_list_why_wrong_scored.csv"

# Prefer the expected CSV; fall back from accidental .dsv extension
csv_path = Path(csv_to_inspect)
if csv_path.suffix.lower() == ".dsv":
    csv_path = csv_path.with_suffix(".csv")

if not csv_path.exists():
    raise FileNotFoundError(f"Could not find scored file: {csv_path}")

df_scores = pd.read_csv(csv_path)

for row in df_scores.itertuples():
    if row.correct == 1:
        continue
    q = row.question
    model_ans = row.model_answer
    model_conf = row.confidence
    ground_truth = row.ground_truth
    why_wrong = row.reason
    print(
        f"Q: {q}\nModel Answer: {model_ans}\nConfidence: {model_conf}%\nGround Truth: {ground_truth}\nWhy Wrong: {why_wrong}\n{'-' * 50}"
    )

