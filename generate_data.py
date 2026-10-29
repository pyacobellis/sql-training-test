"""Generate small, obviously synthetic CSVs into data/. Seeded, so output is reproducible."""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)


def write(name, header, rows):
    with open(OUT / name, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


REGIONS = ["North Example", "South Example", "East Example", "West Example"]
FACILITY_TYPES = ["Hospital", "Clinic", "Day Centre"]
facilities = []
for i in range(1, 13):
    ftype = FACILITY_TYPES[(i - 1) % 3] if i > 3 else "Hospital"
    facilities.append((i, f"Fictional {ftype} {i:02d}", ftype, random.choice(REGIONS), random.choice([40, 80, 120, 200])))
write("facilities.csv", ["facility_id", "facility_name", "facility_type", "region", "bed_capacity"], facilities)

diagnoses = [
    ("D01", "Synthetic respiratory condition A", "Respiratory"),
    ("D02", "Synthetic respiratory condition B", "Respiratory"),
    ("D03", "Synthetic cardiac condition A", "Cardiac"),
    ("D04", "Synthetic cardiac condition B", "Cardiac"),
    ("D05", "Synthetic cardiac condition C", "Cardiac"),
    ("D06", "Synthetic injury A", "Injury"),
    ("D07", "Synthetic injury B", "Injury"),
    ("D08", "Synthetic digestive condition A", "Digestive"),
    ("D09", "Synthetic digestive condition B", "Digestive"),
    ("D10", "Synthetic metabolic condition A", "Metabolic"),
    ("D11", "Synthetic metabolic condition B", "Metabolic"),
    ("D12", "Synthetic mental health condition A", "Mental Health"),
]
write("diagnosis_codes.csv", ["diagnosis_code", "description", "category"], diagnoses)

patients = []
for i in range(1, 151):
    birth = date(1930, 1, 1) + timedelta(days=random.randint(0, 365 * 90))
    sex = random.choice(["F", "M", "X"]) if random.random() > 0.05 else ""
    insurance = random.choice(["Public", "Private", "None"]) if random.random() > 0.12 else ""
    patients.append((i, f"Testpatient {i:04d}", sex, birth.isoformat(), random.choice(REGIONS), insurance))
write("patients.csv", ["patient_id", "patient_name", "sex", "birth_date", "home_region", "insurance_type"], patients)

admissions = []
for i in range(1, 401):
    admit = date(2023, 1, 1) + timedelta(days=random.randint(0, 729))
    atype = random.choices(["Emergency", "Elective", "Transfer"], weights=[5, 4, 1])[0]
    # ~8% still admitted (no discharge date)
    discharge = "" if random.random() < 0.08 else (admit + timedelta(days=random.choice([0, 1, 1, 2, 3, 3, 4, 5, 7, 10, 14, 21]))).isoformat()
    diag = random.choice(diagnoses)[0] if random.random() > 0.06 else ""
    admissions.append((i, random.randint(1, 150), random.randint(1, 12), diag, admit.isoformat(), discharge, atype))
write("admissions.csv", ["admission_id", "patient_id", "facility_id", "diagnosis_code", "admit_date", "discharge_date", "admission_type"], admissions)
print("Wrote CSVs to", OUT)
