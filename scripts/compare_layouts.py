import pandas as pd
import unicodedata

def normalize_str(text):
    if not text: return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

print("--- CABEÇALHO MAIO 2025 (ERRO) ---")
df_maio = pd.read_excel(xl, sheet_name="Venda- maio 2025")
print(df_maio.iloc[0:5, 0:12])

print("\n--- CABEÇALHO JUNHO 2025 (OK) ---")
df_junho = pd.read_excel(xl, sheet_name="Venda Junho 2025")
print(df_junho.iloc[0:5, 0:12])
