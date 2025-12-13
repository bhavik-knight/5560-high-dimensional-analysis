import pandas as pd
import sqlite3

# 1. read all sheet into pandas dataframe -> dict
excel_file = "Supplier_Cube_PivotTable_TT.xlsx"
sheets_dict = pd.read_excel(excel_file, sheet_name=None)


# 2. create an in-memory SQLite DB connection
conn = sqlite3.connect(":memory:")


# 3. write each sheet (DataFrame) to SQLite3 DB as a table
for sheet, df in sheets_dict.items():
    print(f"{sheet}")
    df.to_sql(sheet, conn, if_exists="replace", index=False)


# 4. execute SQL Query
query = """
-- Find suppliers whose unit cost is above the average unit cost for each product
-- First Find the average unit cost per product, then join back to find suppliers above that average
WITH AvgProductCost AS (
    SELECT
        ProductName,
        AVG(MeasureValues) AS AvgUnitCost
    FROM
        Supplier_Cube
    WHERE
        MeasureNames = 'Unit Cost'
    GROUP BY
        ProductName
)
SELECT
    sc.FirstName as SupplierFirstName,
    sc.ProductName,
    sc.MeasureValues AS UnitCost,
    apc.AvgUnitCost
FROM
    Supplier_Cube sc
JOIN
    AvgProductCost apc ON sc.ProductName = apc.ProductName
WHERE
    sc.MeasureNames = 'Unit Cost'
    AND sc.MeasureValues > apc.AvgUnitCost
ORDER BY
    sc.MeasureValues DESC, sc.FirstName, sc.ProductName
"""

result_df = pd.read_sql_query(query, conn)
print(result_df)
