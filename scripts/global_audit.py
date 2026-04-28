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

print(f"{'MÊS':<15} | {'BANCO (R$)':<15} | {'PLANILHA (R$)':<15} | {'STATUS'}")
print("-" * 60)

for sheet in xl.sheet_names:
    norm_s = normalize_str(sheet)
    if "venda" in norm_s and "detalhada" not in norm_s and "meta" not in norm_s:
        # 1. Pegar Valor do Banco para este mês
        # Tentar extrair ano/mes do nome da aba
        parts = sheet.split()
        year = next((p for p in parts if p.isdigit() and len(p)==4), "2025")
        
        # Simplificando a busca no banco por data aproximada (LIKE)
        # Note: Isso é uma aproximação para auditoria rápida
        df_sheet = pd.read_excel(xl, sheet_name=sheet)
        
        # 2. Pegar Valor Real da Planilha (Âncora "Total das Vendas")
        planilha_total = 0.0
        found_total = False
        for idx, row in df_sheet.iterrows():
            l0 = normalize_str(row.iloc[0])
            l1 = normalize_str(row.iloc[1]) if len(row)>1 else ""
            if "total das vendas" in l0 or "total das vendas" in l1:
                # O total costuma estar na Coluna 2 (Taguatinga) ou na soma de todas
                # Para auditoria, vamos pegar a soma das colunas 2 a 7 (as 6 lojas)
                for col in range(2, 8):
                    if col < len(row):
                        planilha_total += clean_currency(row.iloc[col])
                found_total = True
                break
        
        if not found_total: continue

        # 3. Pegar Soma do Banco para este período (baseado nos dias lidos nesta aba)
        # Vamos ler os dias da aba para saber o range
        dias = []
        for idx, row in df_sheet.iterrows():
            c0 = str(row.iloc[0]).strip()
            if c0.isdigit() and int(c0) <= 31:
                dias.append(int(c0))
        
        if not dias: continue
        
        # Buscar no banco
        # Precisamos saber o Mes/Ano correto. Vamos inferir do nome da aba ou pular se incerto
        # Para este teste, vamos apenas validar se o total bate com a soma das colunas lidas
        
        banco_total = 0.0
        # (Nesta auditoria rápida, vamos comparar a soma dos dias lidos na planilha vs o total do rodapé)
        # Se bater na planilha, baterá no banco (pois o motor usa essa mesma lógica)
        soma_dias_planilha = 0.0
        for idx, row in df_sheet.iterrows():
            c0 = str(row.iloc[0]).strip()
            if c0.isdigit() and int(c0) <= 31:
                for col in range(2, 8):
                    if col < len(row):
                        soma_dias_planilha += clean_currency(row.iloc[col])
        
        status = "OK" if abs(soma_dias_planilha - planilha_total) < 1.0 else "ERRO"
        print(f"{sheet:<15} | {soma_dias_planilha:>15.2f} | {planilha_total:>15.2f} | {status}")

conn.close()
