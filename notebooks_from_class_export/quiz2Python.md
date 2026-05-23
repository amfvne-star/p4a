1
4 / 4 points
Multiple choice
Which line correctly queries a Pandas DataFrame called df_postings using DuckDB?

Correct answer:

duckdb.sql("SELECT * FROM df_postings").df()

duckdb.run("SELECT * FROM postings")
, Not Selected

duckdb.query(df_postings)
, Not Selected

pd.read_sql("SELECT * FROM df_postings", duckdb)
, Not Selected
Results for question 2.
2
4 / 4 points
Multiple choice
A student writes the following in their notebook:

from analysis import company_summary
df_us = company_summary(engine)
What must be true for this to work?


The engine variable must be named conn

, Not Selected
Correct answer:

analysis.py must exist in the same folder as the notebook and contain a function called company_summary


company_summary must be defined in the notebook first

, Not Selected

analysis.py must be in a subfolder called modules/

, Not Selected
Results for question 3.
3
4 / 4 points
Multiple choice
Where should reusable functions that compute results go in a well-structured project?


In the README.md file

, Not Selected

Directly in the Jupyter notebook cells

, Not Selected
Correct answer:

In a .py module such as analysis.py


In a SQL file

, Not Selected
Results for question 4.
4
4 / 4 points
True or False
A CSV file preserves nested structures such as lists within a column.


True
Correct answer:

False
Results for question 5.
5
4 / 4 points
True or False
Seaborn is built on top of Matplotlib and produces statistically-oriented charts with less code. 

Correct answer:

True

False