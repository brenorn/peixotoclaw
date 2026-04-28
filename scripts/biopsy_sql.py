import sqlite3
import pandas as pd

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)
print("--- BIOPSIA DE DADOS MARCO 2026 ---")

# 1. Ver se há duplicados (mesma data e loja)
df = pd.read_sql_query("SELECT data, id_loja, COUNT(*) as qtd, SUM(valor_bruto) as soma FROM fact_vendas WHERE data LIKE '2026-03%' GROUP BY data, id_loja HAVING qtd > 1", conn)
print(f"Duplicados encontrados: {len(df)}")

# 2. Amostra de um dia
df_sample = pd.read_sql_query("SELECT * FROM fact_vendas WHERE data = '2026-03-05'", conn)
print("\nAmostra 05/03/2026:")
print(df_sample)

# 3. Totais por Loja no Mes
df_total = pd.read_sql_query("SELECT id_loja, SUM(valor_bruto) as total FROM fact_vendas WHERE data LIKE '2026-03%' GROUP BY id_loja", conn)
print("\nTotais por Loja (Março):")
print(df_total)

# 4. Total Geral do Mes
total = pd.read_sql_query("SELECT SUM(valor_bruto) as total FROM fact_vendas WHERE data LIKE '2026-03%'", conn)
print(f"\nTOTAL GERAL MARÇO: {total.iloc[0,0]}")

conn.close()
