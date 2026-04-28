import pandas as pd
import os
import unicodedata

def normalize_str(text):
    if not text or pd.isna(text): return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

print("INICIANDO AUDITORIA DE TOTAIS...")

for sheet in xl.sheet_names:
    if 'Venda' not in sheet: continue
    print(f"\n--- ABA: {sheet} ---")
    df = pd.read_excel(xl, sheet_name=sheet)
    
    # Procurar por ancoras de totais
    for i, row in df.iterrows():
        label = normalize_str(row.iloc[1]) if len(row) > 1 else ""
        
        if "total das vendas" in label:
            print(f"[ACHOU TOTAL] Linha {i}: {row.iloc[1]}")
            # Ver se a linha de baixo é a meta
            if i + 1 < len(df):
                meta_row = df.iloc[i+1]
                print(f"[META ABAIXO] Linha {i+1}: {meta_row.iloc[1]} -> Valores: {meta_row.iloc[2:8].tolist()}")
        
        # Procurar por blocos de meta no corpo (para comparar)
        if label == "meta" and i < 50:
             print(f"[META CORPO] Linha {i}: {row.iloc[1]} -> Valores: {row.iloc[2:8].tolist()}")

print("\nAUDITORIA CONCLUÍDA.")
