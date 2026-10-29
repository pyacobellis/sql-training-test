-- Creates the course tables and loads the synthetic CSVs.
CREATE TABLE facilities (
    facility_id   INTEGER PRIMARY KEY,
    facility_name VARCHAR NOT NULL,
    facility_type VARCHAR,
    region        VARCHAR,
    bed_capacity  INTEGER
);

CREATE TABLE diagnosis_codes (
    diagnosis_code VARCHAR PRIMARY KEY,
    description    VARCHAR,
    category       VARCHAR
);

CREATE TABLE patients (
    patient_id     INTEGER PRIMARY KEY,
    patient_name   VARCHAR NOT NULL,
    sex            VARCHAR,
    birth_date     DATE,
    home_region    VARCHAR,
    insurance_type VARCHAR
);

CREATE TABLE admissions (
    admission_id    INTEGER PRIMARY KEY,
    patient_id      INTEGER NOT NULL REFERENCES patients (patient_id),
    facility_id     INTEGER NOT NULL REFERENCES facilities (facility_id),
    diagnosis_code  VARCHAR REFERENCES diagnosis_codes (diagnosis_code),
    admit_date      DATE NOT NULL,
    discharge_date  DATE,
    admission_type  VARCHAR
);

-- Empty CSV fields become NULL.
INSERT INTO facilities      SELECT * FROM read_csv('data/facilities.csv',      header = true);
INSERT INTO diagnosis_codes SELECT * FROM read_csv('data/diagnosis_codes.csv', header = true);
INSERT INTO patients        SELECT * FROM read_csv('data/patients.csv',        header = true);
INSERT INTO admissions      SELECT * FROM read_csv('data/admissions.csv',      header = true);
