import csv
import random
from datetime import datetime
from pathlib import Path
OUTPUT_DIR = Path("./generated_csv")
OUTPUT_DIR.mkdir(exist_ok=True)
NULL_RATE = 0.05  # 5% nulls
def random_value(col_index):
    # Mixed data types
    if col_index % 4 == 0:
        return random.randint(0, 1_000_000)
    elif col_index % 4 == 1:
        return f"{random.uniform(0, 10000):.4f}"
    elif col_index % 4 == 2:
        year = random.randint(2000, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year:04d}-{month:02d}-{day:02d}"
    else:
        return random.choice(["true", "false"])
def generate_csv(filename, columns, rows, mismatch_headers=False):
    path = OUTPUT_DIR / filename
    print(f"\nGenerating {filename} ({columns} cols x {rows} rows)...")
    headers = []
    for i in range(columns):
        if mismatch_headers and i % 10 == 0:
            headers.append(f"COL_{i}_WRONG")
        else:
            headers.append(f"Column_{i}")
 with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in range(rows):
            row = []
            for c in range(columns):
                if random.random() < NULL_RATE:
                    row.append("")
                else:
                    row.append(random_value(c))
            writer.writerow(row)
            if r % 5000 == 0 and r != 0:
                print(f"  {r} rows written...")
    print(f"Finished {filename}")
    return path
generate_csv("5cols_100rows_mixed.csv", 5, 100)