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

master_stores = ["Taguatinga", "Sudoeste 1", "Sudoeste 2", "Vicente Pires", "Ceilandia", "Taguatinga Sul", "Alameda"]

def discover_cols(df):
    cols = {}
    limit = min(10, len(df.columns))
    for i in range(min(15, len(df))):
        for j in range(limit):
            val = normalize_str(df.iloc[i, j])
            for store in master_stores:
                if normalize_str(store) == val:
                    cols[store] = j
    return cols

excel_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
xl = pd.ExcelFile(excel_path)

print(f"{'MÊS':<20} | {'SOMA LOJAS (R$)':<15} | {'TOTAL RODAPÉ (R$)':<15} | {'STATUS'}")
print("-" * 70)

for sheet in xl.sheet_names:
    norm_s = normalize_str(sheet)
    if "venda" in norm_s and "detalhada" not in norm_s and "meta" not in norm_s:
        df = pd.read_excel(xl, sheet_name=sheet)
        store_map = discover_cols(df)
        
        if not store_map: continue

        # 1. Somar apenas as colunas identificadas como LOJAS (Dia a Dia)
        soma_diaria = 0.0
        for idx, row in df.iterrows():
            c0 = str(row.iloc[0]).strip()
            if c0.isdigit() and int(c0) <= 31:
                for store, col_idx in store_map.items():
                    soma_diaria += clean_currency(row.iloc[col_idx])
        
        # 2. Pegar o Total do Rodapé (Âncora)
        # Atenção: O total do rodapé na planilha é a soma das lojas.
        # Vamos validar se a nossa soma dos dias bate com o total declarado na planilha.
        total_declarado = 0.0
        for idx, row in df.iterrows():
            l0 = normalize_str(row.iloc[0])
            l1 = normalize_str(row.iloc[1]) if len(row)>1 else ""
            if "total das vendas" in l0 or "total das vendas" in l1:
                for store, col_idx in store_map.items():
                    total_declarado += clean_currency(row.iloc[col_idx])
                break
        
        diff = abs(soma_diaria - total_declarado)
        status = "OK" if diff < 10.0 else f"ERRO (Diff: {diff:.2f})"
        print(f"{sheet:<20} | {soma_diaria:>15.2f} | {total_declarado:>15.2f} | {status}")

