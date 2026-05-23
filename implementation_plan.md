# Session 4 Implementation Plan (Final)

The goal is to execute the tasks for Session 4 of the P4A project as specified in the "Session 4 — Project Tasks.pdf" document. This involves data extraction, transformation, and visualization using DuckDB and pandas, saving output files, and populating `analysis.py` with reusable functions.

This plan incorporates user feedback to handle dependencies via mocked data and securely manage database credentials using a `.env` file.

## User Review Required
Please review this final plan. If it looks good, I will proceed with the execution.

## Proposed Changes

---

### `.env` and `.gitignore`
[NEW] `.env`
- Create a `.env` file containing the provided database credentials:
  - `DB_USER=a20254350`
  - `DB_PASS=2Aj0Mh`
  - `DB_HOST=3de0dac0-8513-4220-9ee7-414dc040c138.bn2a2uid0up8mv7mv2ig.databases.appdomain.cloud`
  - `DB_PORT=31131`
  - `DB_NAME=linkedin_jobs`

[MODIFY] `.gitignore`
- Ensure `.env` is added to the `.gitignore` file so credentials are not committed.

---

### `project_group23/notebook4.ipynb`
[MODIFY] `notebook4.ipynb`
- **Setup**: Add code to initialize the SQLAlchemy database connection by loading credentials from the `.env` file using `dotenv`.
- **Task 1**: Load `jobs_job_industries` and `mappings_industries` into DataFrames. Use DuckDB to JOIN these with full-time `postings_with_benefits` to get posting counts per industry. Include a markdown cell explaining why DuckDB is used (e.g., "DuckDB allows us to express complex JOINs and aggregations cleanly using familiar SQL syntax without the verbosity of nested Pandas merges").
- **Task 2**: Use DuckDB to filter full-time postings with 'Medical insurance' in the benefits column and count per industry (Top 10). Include a markdown cell comparing this to Task 1 rankings.
- **Task 3**: Create a horizontal bar chart (using `matplotlib`/`seaborn`) showing the top 15 industries by full-time posting count.
- **Task 4**: Create a histogram of the `views` column for full-time postings. Include a vertical line for the median. Include a markdown cell noting if the distribution is symmetric or skewed.
- **Task 5**: Export the industry counts from Task 1 as a CSV. For the top 10 countries JSON, I will mock a DataFrame with 10 countries and export it to JSON as requested.
- **Task 6 Integration**: Import the 4 functions from `analysis.py` and call them.

---

### `project_group23/analysis.py`
[MODIFY] `analysis.py`
- **`load_postings(engine)`**: Load the `postings_with_benefits` table and parse `listed_time` from Unix milliseconds to UTC datetime using `pd.to_datetime(..., unit='ms', utc=True)`.
- **`filter_fulltime(df)`**: Filter where `formatted_work_type == 'Full-time'`.
- **`company_summary(engine)`**: Load `companies_companies`, filter to US companies.
- **`top_industries(df_postings, df_job_industries, df_industries, n)`**: Encapsulate the DuckDB logic from Task 1 into a reusable Python function.

## Verification Plan

### Automated Tests
- I will perform syntactical checks to ensure the Python and SQL code is well-formed.

### Manual Verification
- You will be responsible for running `notebook4.ipynb` to verify that the charts render correctly and the outputs match your expectations. I will ensure the code is complete and syntactically correct so it's ready for your execution.
