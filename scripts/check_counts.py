import sqlite3
import pandas as pd

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)

print("--- CONTTAGEM E AUDITORIA MARCO 2026 ---")

# 1. Contagem total de linhas em Março
count = pd.read_sql_query("SELECT COUNT(*) as qtd FROM fact_vendas WHERE data LIKE '2026-03%'", conn)
print(f"Total de linhas em Março: {count.iloc[0,0]}")
print(f"Esperado (6 lojas * 31 dias): {6 * 31}")

# 2. Verificar se o valor bruto é a soma de outros campos
df_sum = pd.read_sql_query("""
    SELECT 
        data, id_loja, valor_bruto,
        (valor_dinheiro + valor_credito + valor_debito + valor_pix + valor_ifood) as soma_canais
    FROM fact_vendas 
    WHERE data = '2026-03-05'
""", conn)
print("\nComparação Bruto vs Canais (05/03/2026):")
print(df_sum)

conn.close()
