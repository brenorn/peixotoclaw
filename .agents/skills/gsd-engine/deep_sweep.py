import os
import json
from pathlib import Path
from typing import Dict, List, Any

# Configurações de Ingestão Monster
IGNORED_DIRS = {".git", "node_modules", "venv", "__pycache__", ".next", ".antigravity", ".gemini", "dist", "build"}
CORE_FILES = {"main.py", "package.json", "index.js", "server.js", "manage.py", "docker-compose.yml", "requirements.txt", ".env"}

def deep_sweep(project_path: str) -> Dict[str, Any]:
    """
    Realiza a varredura profunda de um projeto para extrair o DNA técnico.
    """
    path = Path(project_path)
    if not path.exists():
        return {"error": "Path not found"}

    sweep_result = {
        "root": str(path),
        "structure": {},
        "tech_stack": [],
        "entry_points": [],
        "database": "Unknown",
        "env_vars": [],
        "summary": ""
    }

    # 1. Mapear estrutura e identificar Tech Stack
    for item in path.iterdir():
        if item.is_dir() and item.name not in IGNORED_DIRS:
            sweep_result["structure"][item.name] = "Folder"
        elif item.is_file():
            if item.name in CORE_FILES:
                sweep_result["entry_points"].append(item.name)
            
            # Heurísticas de Stack
            if item.suffix == ".py": sweep_result["tech_stack"].append("Python")
            if item.suffix == ".js" or item.suffix == ".ts": sweep_result["tech_stack"].append("JavaScript/TypeScript")
            if item.suffix == ".sql": sweep_result["tech_stack"].append("SQL (Postgres/MySQL)")
            if item.name == "package.json": sweep_result["tech_stack"].append("Node.js/NPM")
            if item.name == "requirements.txt": sweep_result["tech_stack"].append("Pip/Requirements")

    # Deduzir Tech Stack única
    sweep_result["tech_stack"] = list(set(sweep_result["tech_stack"]))

    # 2. Investigar Banco de Dados e Variáveis
    env_file = path / ".env"
    if env_file.exists():
        lines = env_file.read_text(encoding="utf-8").splitlines()
        for line in lines:
            if "=" in line and not line.startswith("#"):
                key = line.split("=")[0].strip()
                sweep_result["env_vars"].append(key)
                if "DATABASE" in key.upper() or "DB_" in key.upper():
                    sweep_result["database"] = "Detected (Check .env)"

    # 3. Gerar Resumo Monster
    sweep_result["summary"] = f"Projeto detectado em {path.name}. Stack: {', '.join(sweep_result['tech_stack'])}. Pontos de entrada: {', '.join(sweep_result['entry_points'])}."
    
    return sweep_result

def format_deep_sweep_report(result: Dict[str, Any]) -> str:
    """Formata o resultado para o chat ou relatório."""
    if "error" in result: return f"❌ Erro: {result['error']}"
    
    report = f"""# 🧬 Monster DNA Report: {Path(result['root']).name}

**Status de Ingestão**: COMPLETO ✅
**Caminho**: `{result['root']}`
**Stack Técnica**: {', '.join(result['tech_stack'])}
**Database**: {result['database']}

## 🏗️ Estrutura Identificada
{chr(10).join([f"- {k}" for k in result['structure'].keys()])}

## 🚀 Pontos de Entrada (Entrypoints)
{chr(10).join([f"- `{f}`" for f in result['entry_points']])}

## 🔑 Variáveis de Ambiente (Mapeadas)
- {len(result['env_vars'])} variáveis detectadas (Secrets preservados).

---
"Eu já comi esse código. Estou pronto para expandir."
"""
    return report

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    res = deep_sweep(target)
    print(format_deep_sweep_report(res))
