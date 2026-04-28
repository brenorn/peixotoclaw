import sqlite3
import pandas as pd

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)

print("--- BUSCA POR 01/03/2026 ---")
df = pd.read_sql_query("SELECT * FROM fact_vendas WHERE data = '2026-03-01'", conn)
if df.empty:
    print("Nenhum registro encontrado para 01/03/2026.")
else:
    print(df)

print("\n--- BUSCA POR 31/03/2026 ---")
df2 = pd.read_sql_query("SELECT * FROM fact_vendas WHERE data = '2026-03-31'", conn)
if df2.empty:
    print("Nenhum registro encontrado para 31/03/2026.")
else:
    print(df2)

conn.close()
