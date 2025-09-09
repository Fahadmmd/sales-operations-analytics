import pandas as pd
import sqlite3

# Step 1: Read your cleaned CSV
# 👉 Replace with the path to your file
csv_path = "cleaned_sales.csv"
df = pd.read_csv(csv_path)

# Step 2: Connect to SQLite (creates sales_ops.db if not exists)
conn = sqlite3.connect("sales_ops.db")

# Step 3: Import DataFrame into SQLite as table "Sales"
df.to_sql("Sales", conn, if_exists="replace", index=False)

# Step 4: Test a sample query
query = """
SELECT strftime('%Y-%m', "Order Date") AS Month, SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Month
ORDER BY Month;
"""
result = pd.read_sql(query, conn)
print(result.head())

# Step 5: Close the connection
conn.close()
