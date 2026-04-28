import pandas as pd
import unicodedata

def normalize_str(text):
    if not text: return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

for sheet in ["Venda- maio 2025", "Venda OUTUBRO 2025", "Venda JANEIRO 2026"]:
    print(f"\n--- COLUNAS DE {sheet} ---")
    df = pd.read_excel(xl, sheet_name=sheet)
    # Procurar a linha onde estão os nomes das lojas
    for i in range(min(5, len(df))):
        row_vals = [str(x).strip() for x in df.iloc[i].tolist()]
        print(f"Linha {i}: {row_vals}")
