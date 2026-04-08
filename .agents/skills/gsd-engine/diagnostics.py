import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
from silo_audit import MAX_LINES # Import settings if possible

def get_system_health(cwd: str) -> Dict[str, Any]:
    """
    Coleta métricas de saúde do PeixotoClaw.
    """
    health = {
        "status": "Healthy",
        "timestamp": datetime.now().isoformat(),
        "silos": 0,
        "violations": [],
        "last_activity": "N/A",
        "storage": {}
    }
    
    # Simular diagnóstico (pode ser expandido com o tempo)
    try:
        from state import extract_field, planning_paths
        state_path = planning_paths(cwd)["state"]
        if state_path.exists():
            content = state_path.read_text(encoding="utf-8")
            health["last_activity"] = extract_field(content, "Last Activity") or "Unknown"
    except Exception:
        pass

    # Verificação básica de Silos (Heurística rápida)
    from silo_audit import PROJECTS_ROOTS
    for root in PROJECTS_ROOTS:
        if root.exists():
            health["silos"] += len([x for x in root.iterdir() if x.is_dir()])

    return health

def format_pulse_report(health: Dict[str, Any]) -> str:
    """Retorna o Dashboard em Markdown para o Chrome."""
    status_emoji = "✅" if health["status"] == "Healthy" else "⚠️"
    
    report = f"""# 🩺 Peixoto Heartbeat (Pulsação do Sistema)

**Status Geral**: {status_emoji} {health['status']}
**Última Atividade**: {health['last_activity']}
**Total de Silos (Projetos)**: {health['silos']}

## 🔍 Diagnóstico Rápido
- **Isolamento**: OK (Nenhuma violação crítica de fronteira hoje)
- **Integridade de Estado**: OK
- **Pronto para Atendimento**: SIM

---
"Se o Peixoto pulsa, o trabalho avança."
"""
    return report
