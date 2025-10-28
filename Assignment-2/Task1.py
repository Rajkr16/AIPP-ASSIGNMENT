import csv
import statistics
import os

# ✅ Ensure the CSV is saved inside the same folder as this script
folder = os.path.dirname(os.path.abspath(__file__))  # current script folder
csv_path = os.path.join(folder, "data.csv")

# Data to write into the CSV file
data = [
    ["Name", "Age", "Score"],
    ["Raj", 21, 88],
    ["Priya", 22, 92],
    ["Amit", 20, 75]
]

# ✅ Create and write to data.csv inside Assignment-2 folder
with open(csv_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ CSV file created successfully at '{csv_path}'")

def analyze_csv(path):
    """
    Read CSV at path and compute mean, min, max for each numeric column.
    Returns a dict mapping column -> {'mean':..., 'min':..., 'max':...}
    """
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return {}

        cols = {name: [] for name in reader.fieldnames}

        for row in reader:
            for name, value in row.items():
                try:
                    cols[name].append(float(value))
                except (TypeError, ValueError):
                    continue  # ignore non-numeric values

        results = {}
        for name, values in cols.items():
            if values:
                results[name] = {
                    "mean": statistics.mean(values),
                    "min": min(values),
                    "max": max(values),
                }
        return results


# ✅ Example usage
if __name__ == "__main__":
    stats = analyze_csv(csv_path)
    for col, s in stats.items():
        print(f"{col}: mean={s['mean']}, min={s['min']}, max={s['max']}")

