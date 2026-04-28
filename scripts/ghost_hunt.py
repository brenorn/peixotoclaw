import sqlite3
import pandas as pd

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)

print("--- ANALISE DE LOJAS E REGISTROS MARCO 2026 ---")

# 1. Agrupado por Loja
df_lojas = pd.read_sql_query("""
    SELECT id_loja, COUNT(*) as qtd, SUM(valor_bruto) as total 
    FROM fact_vendas 
    WHERE data LIKE '2026-03%' 
    GROUP BY id_loja
""", conn)
print("Distribuição por Loja:")
print(df_lojas)

# 2. Ver se há datas estranhas
df_datas = pd.read_sql_query("""
    SELECT data, COUNT(*) as qtd
    FROM fact_vendas 
    WHERE data LIKE '2026-03%' 
    GROUP BY data
    ORDER BY qtd DESC
    LIMIT 10
""", conn)
print("\nDatas com mais registros:")
print(df_datas)

# 3. Ver um registro bruto
cursor = conn.cursor()
cursor.execute("SELECT * FROM fact_vendas WHERE data LIKE '2026-03%' LIMIT 5")
print("\nPrimeiros 5 registros de Março:")
print(cursor.fetchall())

conn.close()
