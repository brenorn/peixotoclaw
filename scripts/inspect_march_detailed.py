import pandas as pd
import unicodedata

def normalize_str(text):
    if not text: return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

target = "venda detalhada mar. 26"
sheet_name = None
for s in xl.sheet_names:
    if normalize_str(s) == target:
        sheet_name = s
        break

if sheet_name:
    print(f"LENDO ABA: {sheet_name}")
    df = pd.read_excel(xl, sheet_name=sheet_name)
    print("\n--- LINHAS 0 A 20 ---")
    print(df.iloc[0:20, 0:3])
else:
    print("Aba Detalhada não encontrada.")
