import json
import re
import sys
from pathlib import Path

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except:
        pass

def analyze_maturity(dossier_path: Path):
    """Analisa os arquivos do dossiê para determinar o próximo passo lógico e econômico."""
    plan_path = dossier_path / "PLAN.md"
    tasks_path = dossier_path / "TASKS.md"
    specs_dir = dossier_path / "specs"
    
    # 1. Checar Plano Estratégico e Peso de Tokens
    if not plan_path.exists():
        return "LEVEL_0", "prd-manager", "O projeto não possui um PLANO estratégico. Recomendo iniciar com o prd-manager."
    
    plan_content = plan_path.read_text(encoding="utf-8")
    tasks_content = tasks_path.read_text(encoding="utf-8") if tasks_path.exists() else ""
    
    # Estimativa simples de tokens (1 token ~= 4 caracteres)
    total_chars = len(plan_content) + len(tasks_content)
    # Somar peso das specs
    if specs_dir.exists():
        for f in specs_dir.glob("*.md"):
            total_chars += len(f.read_text(encoding="utf-8"))
            
    estimated_tokens = total_chars // 4
    economic_alert = ""
    if estimated_tokens > 8000:
        economic_alert = f"\n⚠️ [ALERTA ECONÔMICO]: Contexto atual (~{estimated_tokens} tokens) ultrapassou o limite de 8K. Recomendo usar 'sandeco-token-reduce' para otimizar custos."

    if "Defina o objetivo central aqui" in plan_content or len(plan_content.splitlines()) < 10:
        return "LEVEL_0", "prd-manager", "O PLANO estratégico está vazio ou é apenas um template. Precisamos definir os objetivos com prd-manager." + economic_alert

    # 2. Checar Especificações Técnicas
    has_specs = any(specs_dir.iterdir()) if specs_dir.exists() else False
    if not has_specs:
        return "LEVEL_1", "sdd-spec", "O nível estratégico está pronto, mas não temos ESPECIFICAÇÕES técnicas. Recomendo usar sdd-spec." + economic_alert

    # 3. Checar Tarefas Táticas
    if not tasks_path.exists():
        return "LEVEL_2", "project-manager", "Faltam o acompanhamento de TAREFAS. Vamos inicializar o backlog?" + economic_alert
        
    tasks_content = tasks_path.read_text(encoding="utf-8")
    open_tasks = re.findall(r"- \[ \]", tasks_content)
    
    if len(open_tasks) > 0:
        return "LEVEL_2", "maestro_sandeco", f"Temos {len(open_tasks)} tarefas pendentes. Pronto para iniciar a execução via Maestro? {economic_alert}"

    return "LEVEL_3", "avaliacoes", "Todas as tarefas parecem concluídas. Iniciamos a auditoria final de qualidade?" + economic_alert

def run_diagnostic(project_name: str, dossier_path: str):
    print(f"\n🔍 [DIAGNÓSTICO AUTOMÁTICO: {project_name}]")
    level, skill, advice = analyze_maturity(Path(dossier_path))
    
    print(f"📊 Maturidade: {level}")
    print(f"🎯 Próximo Passo: {advice}")
    print(f"🛠️  Skill Recomendada: {skill}")
    print("-" * 40)
    
    # Retorna para que o script chamador possa sugerir a ação
    return skill

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        sys.exit(1)
    run_diagnostic(sys.argv[1], sys.argv[2])
