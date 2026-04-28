import pandas as pd
import os
import unicodedata
import re

def normalize_str(text):
    if not text or pd.isna(text): return ""
    text = "".join(c for c in unicodedata.normalize('NFD', str(text)) if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

file_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(file_path)

months_br = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

print("INICIANDO SCAN DE RODAPÉ E CABEÇALHOS...")

for sheet in xl.sheet_names:
    if 'Venda' not in sheet: continue
    print(f"\n--- EXPLORANDO: {sheet} ---")
    df = pd.read_excel(xl, sheet_name=sheet)
    
    for i, row in df.iterrows():
        # Verificamos as primeiras 3 colunas em busca de labels
        for col_idx in range(min(len(row), 3)):
            label = normalize_str(row.iloc[col_idx])
            
            # 1. Procurar por Total das Vendas (Rodapé)
            if "total das vendas" in label or "total de vendas" in label:
                print(f"[ACHOU TOTAL] Linha {i}, Col {col_idx}: '{row.iloc[col_idx]}' -> Totais: {row.iloc[col_idx+1:col_idx+10].tolist()}")
            
            # 2. Procurar por Meta Mensal (Nome do Mês)
            for m in months_br:
                if m == label:
                    print(f"[ACHOU META MENSAL] Linha {i}, Col {col_idx}: '{row.iloc[col_idx]}' -> Valores: {row.iloc[col_idx+1:col_idx+10].tolist()}")

print("\nSCAN CONCLUÍDO.")
