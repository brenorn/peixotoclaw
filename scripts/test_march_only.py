from engine_v5 import NexusETLEngine
import pandas as pd
import sqlite3
import os

excel_path = r'd:\OneDrive\aiproj\Bolo_Flavio\base de dados\Vendas - VDS.xlsx'
db_path = r'd:\OneDrive\aiproj\Bolo_Flavio\data\db\bolo_flavio_v5.db'

# Configurar motor para processar apenas Março 2026
engine = NexusETLEngine(excel_path, db_path)
engine.cursor.execute("DELETE FROM fact_vendas")

sheet_resumo = "Venda MARÇO 2026"
sheet_detalhada = "Venda Detalhada Mar. 26"

print("--- INICIANDO RASTREIO MARCO 2026 ---")

# 1. Processar Resumo
df_resumo = pd.read_excel(engine.xl, sheet_name=sheet_resumo)
print(f"Lendo Resumo: {sheet_resumo}")
engine._process_summary_sheet(df_resumo, "2026", "03")

# 2. Processar Detalhada
df_detalhada = pd.read_excel(engine.xl, sheet_name=sheet_detalhada)
print(f"Lendo Detalhada: {sheet_detalhada}")
engine._process_detailed_sheet(df_detalhada, "2026", "03")

engine.conn.commit()
print("--- FIM DO RASTREIO ---")
