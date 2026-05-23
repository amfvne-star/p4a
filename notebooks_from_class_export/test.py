# Your code here
import pandas as pd
import numpy as np
import duckdb

np.random.seed(7)
n = 400

categories = np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], n, p=[0.35, 0.25, 0.25, 0.15])
regions    = np.random.choice(['North', 'South', 'East', 'West'], n)
channels   = np.random.choice(['Online', 'In-store', 'Phone', None], n, p=[0.40, 0.35, 0.15, 0.10])
quantity   = np.random.randint(1, 8, n)
unit_price = np.where(
    np.random.rand(n) < 0.18, np.nan,
    np.random.choice([29.99, 49.99, 99.99, 149.99, 299.99, 499.99, 799.99], n)
)

df_sales = pd.DataFrame({
    'sale_id':    range(1, n + 1),
    'category':   categories,
    'region':     regions,
    'channel':    channels,
    'quantity':   quantity,
    'unit_price': unit_price,
})
df_sales['revenue'] = df_sales['quantity'] * df_sales['unit_price']

df_categories = pd.DataFrame({
    'category':   ['Electronics', 'Clothing', 'Home', 'Sports'],
    'department': ['Technology', 'Fashion', 'Living', 'Active Lifestyle'],
    'buyer':      ['Ana Silva', 'Jo├úo Costa', 'Maria Pinto', 'Rui Ferreira'],
})

print("--- Average Unit Price ---")
print(round(df_sales['unit_price'].mean(), 2))

print("\n--- % Sales with No Revenue ---")
print(round(df_sales['revenue'].isnull().mean() * 100, 1))

print("\n--- In-Store Channel Department Revenue Ranking ---")
query = """
SELECT 
    c.department, 
    SUM(s.revenue) AS total_revenue
FROM df_sales s
INNER JOIN df_categories c ON s.category = c.category
WHERE s.channel = 'In-store'
GROUP BY c.department
ORDER BY total_revenue DESC
"""
res = duckdb.sql(query).df()
print(res)
res.to_csv('results.csv', index=False)

def channel_filter(df, channel):
    return df[df['channel'] == channel]

print(channel_filter(df_sales, 'In-store'))
