import sqlite3
import pandas as pd
import unicodedata

def normalize_str(text):
    if not text: return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

def clean_currency(val):
    if pd.isna(val): return 0.0
    if isinstance(val, (int, float)): return float(val)
    s = str(val).replace('R$', '').replace('.', '').replace(',', '.').strip()
    try: return float(s)
    except: return 0.0

excel_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'
conn = sqlite3.connect(db_path)
xl = pd.ExcelFile(excel_path)

# Lista completa de abas para auditar
sheets_to_audit = [
    ("Venda- maio 2025", "2025-05"),
    ("Venda Junho 2025", "2025-06"),
    ("Venda Julho 2025 ", "2025-07"),
    ("Venda Agosto 2025", "2025-08"),
    ("Venda Setembro 2025", "2025-09"),
    ("Venda OUTUBRO 2025", "2025-10"),
    ("Venda NOVEMBRO 2025", "2025-11"),
    ("Venda DEZEMBRO 2025", "2025-12"),
    ("Venda JANEIRO 2026", "2026-01"),
    ("Venda FEVEREIRO 2026", "2026-02"),
    ("Venda MARÇO 2026", "2026-03"),
    ("Venda ABRIL 2026", "2026-04")
]

print(f"{'MÊS (ABA)':<25} | {'BANCO (R$)':<15} | {'PLANILHA (R$)':<15} | {'DIFERENÇA'}")
print("-" * 75)

for sheet_name, db_prefix in sheets_to_audit:
    try:
        df = pd.read_excel(xl, sheet_name=sheet_name)
        
        # 1. Pegar Valor Real da Planilha (Linha Total das Vendas)
        planilha_total = 0.0
        for idx, row in df.iterrows():
            l0 = normalize_str(row.iloc[0])
            l1 = normalize_str(row.iloc[1]) if len(row)>1 else ""
            if "total das vendas" in l0 or "total das vendas" in l1:
                # Soma das 6 lojas (Colunas 2 a 7)
                for col in range(2, 8):
                    if col < len(row):
                        planilha_total += clean_currency(row.iloc[col])
                break
        
        # 2. Pegar Valor no Banco
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(valor_bruto) FROM fact_vendas WHERE data LIKE ?", (f"{db_prefix}%",))
        banco_total = cursor.fetchone()[0] or 0.0
        
        diff = abs(banco_total - planilha_total)
        status = "OK" if diff < 1.0 else f"DIFF: R$ {diff:.2f}"
        
        print(f"{sheet_name:<25} | {banco_total:>15.2f} | {planilha_total:>15.2f} | {status}")
    except Exception as e:
        print(f"{sheet_name:<25} | {'ERRO':<15} | {'ERRO':<15} | {str(e)}")

conn.close()
