import pandas as pd
import duckdb
from sqlalchemy import create_engine

def load_postings(engine) -> pd.DataFrame:
    """Load the postings_with_benefits staging table from the course database.
    Parses listed_time from Unix milliseconds to UTC datetime.
    """
    try:
        df = pd.read_sql("SELECT * FROM a20254350.postings_with_benefits", engine)
    except Exception:
        df = pd.read_sql("SELECT * FROM postings_with_benefits", engine)
    
    if 'listed_time' in df.columns:
        if pd.api.types.is_numeric_dtype(df['listed_time']):
            df['listed_time'] = pd.to_datetime(df['listed_time'], unit='ms', utc=True)
        else:
            df['listed_time'] = pd.to_datetime(df['listed_time'], utc=True)
    return df

def filter_fulltime(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to full-time postings. Returns a copy."""
    if 'formatted_work_type' in df.columns:
        return df[df['formatted_work_type'] == 'Full-time'].copy()
    elif 'work_type' in df.columns:
        return df[df['work_type'] == 'FULL_TIME'].copy()
    return df.copy()

def company_summary(engine) -> pd.DataFrame:
    """Load the companies_companies table, filter to US companies."""
    df_companies = pd.read_sql("SELECT * FROM companies_companies", engine)
    if 'country' in df_companies.columns:
        df_us = df_companies[df_companies['country'] == 'US'].copy()
        return df_us
    return df_companies

def top_industries(df_postings, df_job_industries, df_industries, n: int) -> pd.DataFrame:
    """Return the top N industries by posting count using DuckDB."""
    query = """
    SELECT mi.industry_name, COUNT(p.job_id) AS posting_count
    FROM df_postings p
    JOIN df_job_industries ji ON p.job_id = ji.job_id
    JOIN df_industries mi ON ji.industry_id = mi.industry_id
    GROUP BY mi.industry_name
    ORDER BY posting_count DESC
    LIMIT :n
    """
    return duckdb.query(query).to_df()