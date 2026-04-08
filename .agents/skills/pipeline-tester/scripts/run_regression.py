
import asyncio
import os
import json
import sys
from pathlib import Path
from datetime import datetime

# Adicionar raiz do projeto ao sys.path
script_dir = Path(__file__).resolve().parent
root = script_dir.parent.parent.parent
sys.path.insert(0, str(root))

# Mudar diretório de trabalho para a raiz para evitar erros de caminhos relativos
os.chdir(str(root))

# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()

from core.lab.orchestrator import PipelineOrchestrator, create_llm_client

async def run_test(case_path: str):
    # 1. Carregar Caso de Teste
    with open(case_path, 'r', encoding='utf-8') as f:
        case = json.load(f)
    
    print(f"\n🚀 Iniciando Teste de Regressão: {case['name']}")
    print(f"🏢 Descrição: {case['company_description']}")
    
    # 2. Configurar Orquestrador
    api_key = os.getenv("GOOGLE_API_KEY")
    # Usar gemini-2.5-flash (modelo estável confirmado na varredura)
    llm = create_llm_client(api_key=api_key, use_mock=False)
    orch = PipelineOrchestrator(llm)
    
    # 3. Forçar Perfil (Skip Interview)
    await orch.skip_interview(case['company_description'])
    
    # 4. Gerar Estratégia
    print("📝 Gerando Estratégia...")
    strat_resp = await orch.generate_strategy()
    if strat_resp['type'] == 'error':
        print(f"❌ Erro na estratégia: {strat_resp['text']}")
        return
    
    strategy = strat_resp['strategy']
    print(f"✅ Descritores Principais: {strategy['descritores_principais']}")
    
    # 5. Executar Pipeline
    print("🔍 Executando Pipeline (Triador → Curador)...")
    results = {
        "triador_found_ids": [],
        "curador_approved_ids": [],
        "logs": []
    }
    
    async for event in orch.run_pipeline():
        if event['type'] == 'log':
            # print(f"  [{event['agent']}] {event['text']}")
            results['logs'].append(f"[{event['agent']}] {event['text']}")
        
        elif event['type'] == 'triador_complete':
            print(f"📦 Triador finalizou. Encontrados: {event['summary']['total_encontrado']}")
            
        elif event['type'] == 'curador_complete':
            print(f"🏆 Curador finalizou. Genuínos: {event['report']['genuinos']}")
    
    # 6. Analisar Resultados do Disco
    base_dir = Path("core/tests/jsons_API_PNCP")
    subdirs = sorted([d for d in base_dir.iterdir() if d.is_dir()], key=lambda d: d.stat().st_mtime, reverse=True)
    latest_dir = subdirs[0] if subdirs else None
    
    if latest_dir:
        print(f"📂 Analisando diretório: {latest_dir.name}")
        # IDs baixados pelo Triador
        downloaded = [f.stem for f in latest_dir.glob("*.json")]
        results['triador_found_ids'] = downloaded
        
        # IDs aprovados pelo Curador
        report_file = list(latest_dir.glob("relatorio_oportunidades_*.txt"))
        if report_file:
            with open(report_file[0], 'r', encoding='utf-8') as f:
                content = f.read()
                import re
                results['curador_approved_ids'] = re.findall(r"Edital: ([\w-]+)", content)

    # 7. Comparar com Golden Set
    print("\n📊 RESULTADO DA REGRESSÃO:")
    expected = case['expected_ids']
    
    table = []
    hits = 0
    for eid in expected:
        status = "❌ MISS"
        reason = "Não encontrado pelo Triador"
        
        if eid in results['curador_approved_ids']:
            status = "✅ HIT "
            reason = "Aprovado pelo Curador"
            hits += 1
        elif eid in results['triador_found_ids']:
            status = "⚠️ FAIL"
            reason = "Triado mas REPROVADO pelo Curador"
        
        table.append({"id": eid, "status": status, "reason": reason})
        print(f"  {status} | {eid} | {reason}")

    # 8. Salvar Benchmark
    bench_file = latest_dir / "benchmark_regression.json" if latest_dir else Path("benchmark_last_run.json")
    summary = {
        "case_name": case['name'],
        "timestamp": datetime.now().isoformat(),
        "strategy": strategy,
        "metrics": {
            "total_expected": len(expected),
            "total_hits": hits,
            "recall": hits / len(expected) if len(expected) > 0 else 0
        },
        "details": table
    }
    
    with open(bench_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n📈 Recall: {hits}/{len(expected)} ({hits/len(expected)*100:.1f}%)")
    print(f"📄 Relatório salvo em: {bench_file}")

if __name__ == "__main__":
    case_file = sys.argv[1] if len(sys.argv) > 1 else "core/tests/regression/cases/tv_cabo_rj.json"
    asyncio.run(run_test(case_file))
