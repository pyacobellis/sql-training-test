"""Rebuild course.duckdb from setup.sql. Run from anywhere: python build_db.py"""
import os
from pathlib import Path

import duckdb

root = Path(__file__).parent
os.chdir(root)  # setup.sql uses paths relative to the repo root

db = root / "course.duckdb"
for p in (db, root / "course.duckdb.wal"):
    p.unlink(missing_ok=True)

con = duckdb.connect(str(db))
con.execute((root / "setup.sql").read_text())
con.close()
print(f"Built {db.name} with duckdb {duckdb.__version__}")
