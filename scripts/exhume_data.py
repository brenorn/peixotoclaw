import sqlite3
import pandas as pd

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)

print("--- EXUMAÇÃO TAGUATINGA (MARÇO 2026) ---")
df = pd.read_sql_query("SELECT data, valor_bruto, valor_pix, valor_ifood FROM fact_vendas WHERE id_loja = 1 AND data LIKE '2026-03%' ORDER BY data", conn)
print(df)
print(f"\nSOMA TOTAL TAGUATINGA: {df['valor_bruto'].sum()}")

conn.close()
