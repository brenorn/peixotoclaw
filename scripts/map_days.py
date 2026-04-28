import pandas as pd
import unicodedata

def normalize_str(text):
    if not text: return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

target = "venda marco 2026"
sheet_name = None
for s in xl.sheet_names:
    if normalize_str(s) == target:
        sheet_name = s
        break

if sheet_name:
    df = pd.read_excel(xl, sheet_name=sheet_name)
    print(f"COLUNA A (DIAS) DE {sheet_name}:")
    for i, val in enumerate(df.iloc[:, 0]):
        print(f"Linha {i}: {val}")
else:
    print("Aba não encontrada.")
