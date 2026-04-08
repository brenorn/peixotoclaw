import json
import os
from pathlib import Path

PASTA_REGISTRO = Path(".antigravity/equipe/registro_atividades.json")

def report_savings():
    if not PASTA_REGISTRO.exists():
        print("Erro: Ledger não encontrado em .antigravity/equipe/")
        return

    with open(PASTA_REGISTRO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    atividades = dados.get("atividades", [])
    total_tokens = sum(a.get("tokens_locais", 0) for a in atividades)
    total_savings = sum(a.get("custo_estimado_nuvem", 0.0) for a in atividades)

    print("=" * 40)
    print("💰 MONITOR DE ECONOMIA PEIXOTOCLAW 💰")
    print("=" * 40)
    print(f"Total de Atividades: {len(atividades)}")
    print(f"Total de Tokens Locais: {total_tokens:,}")
    print(f"Estimativa de Economia (USD): ${total_savings:.4f}")
    print("-" * 40)
    
    if total_savings > 0:
        print(f"🎉 Parabéns! Você já economizou aprox. R$ {total_savings * 5.0:.2f}")
    else:
        print("Dica: Use mais o OpenCode para ver a economia subir!")
    print("=" * 40)

if __name__ == "__main__":
    report_savings()
