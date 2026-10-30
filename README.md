# SQL Training – Setup Test

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pyacobellis/sql-training-test)


This small test checks that everything you need for the SQL course works from your computer and network. It takes about 5 minutes.

## Steps

1. **Create a free GitHub account** at <https://github.com/signup> (skip if you already have one). You can use any email address, work or personal.
2. **Click the "Open in GitHub Codespaces" button above.** If GitHub asks, click **Create new codespace**.
3. **Wait 2–3 minutes** while the environment builds (see *What's happening during setup* below). A web version of VS Code opens in your browser when it's ready.
4. A notebook called **`00_setup_check.ipynb`** opens automatically. Click **Run All** at the top of the notebook (or press the ▷▷ button).
5. If every cell shows a result and none shows a red error, **you're ready**. Tell your trainer it worked.

## What's happening during setup

A codespace is a small computer in the cloud, run by GitHub, that you use through VS Code in your browser. Nothing is installed on your own computer. The first time you open it:

1. GitHub starts the machine and copies this project onto it (about 1 minute).
2. It installs the tools the course needs: DuckDB and the Jupyter notebook support (about 1 minute). You may see a progress log while this runs. Leave the tab open and wait.
3. VS Code opens with the notebook ready to run.

If you reopen the same codespace later, it starts in a few seconds because everything is already installed.

## About the data

All data in this repository is **entirely synthetic**. Patients, facilities and admissions are made up by a script (`generate_data.py`) and do not describe real people or places.

## Troubleshooting

- **The build fails or shows an error:** click **Rebuild Container** in the error message (or press `F1` and search for "Codespaces: Rebuild Container"). If it fails again, send your trainer a screenshot.
- **The notebook asks you to select a kernel:** click **Select Kernel** (top right) → **Python Environments** → choose the entry marked `/usr/local/bin/python`. Then click **Run All** again.
- **The page is blocked or won't load:** your company network may be blocking GitHub or Codespaces. Take a screenshot of what you see and send it to your trainer – that is exactly what this test is for.

## When you're done

Codespaces gives you a limited number of free hours per month. Please **stop or delete your codespace** afterwards: go to <https://github.com/codespaces>, click the `...` next to your codespace and choose **Stop codespace** (or **Delete** if you no longer need it).

---

### For the trainer

- Rebuild the data/database: `python generate_data.py && python build_db.py` (needs `pip install -r requirements.txt`).
