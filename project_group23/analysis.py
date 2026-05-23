import pandas as pd
import duckdb
from sqlalchemy import create_engine

def load_postings(engine) -> pd.DataFrame:
    """Load the postings_with_benefits staging table from the course database."""
    

def filter_fulltime(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to full-time postings. Returns a copy."""
    
def company_summary(engine) -> pd.DataFrame:
    """Load the companies_companies table, filter to US companies."""
def top_industries(df_postings, df_job_industries, df_industries, n: int) -> pd.DataFrame:
    """Return the top N industries by posting count."""