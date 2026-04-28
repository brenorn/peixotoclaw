import sqlite3

db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Conferir faturamento total por mês no banco
months = ["2025-05", "2025-10", "2025-11", "2026-01", "2026-03", "2026-04"]

print(f"{'MÊS':<10} | {'TOTAL BANCO'}")
print("-" * 25)

for m in months:
    cursor.execute("SELECT SUM(valor_bruto) FROM fact_vendas WHERE data LIKE ?", (f"{m}%",))
    total = cursor.fetchone()[0]
    print(f"{m:<10} | {total:>15.2f}")

conn.close()
