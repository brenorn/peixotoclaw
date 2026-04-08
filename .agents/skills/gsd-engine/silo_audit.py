import os
from pathlib import Path
from typing import List, Dict

# Configurações da Soberania de Silos
MAX_LINES = 500
PROJECTS_ROOTS = [
    Path("d:/OneDrive/aiproj/PeixotoClaw/projects"),
    Path("d:/OneDrive/aiproj/mind")
]

def audit_silos():
    print("🔍 Iniciando Auditoria de Soberania de Silos (PeixotoClaw)...")
    violations = []
    
    for root_path in PROJECTS_ROOTS:
        if not root_path.exists():
            continue
            
        print(f"--- Escaneando Raiz: {root_path} ---")
        
        for item in root_path.iterdir():
            if item.is_dir():
                # Auditar dentro do projeto (Silo)
                check_folder_isolation(item, violations)
            elif item.suffix == ".py":
                # Arquivo solto na raiz do projeto/projects
                violations.append({
                    "file": str(item),
                    "issue": "Silo Violation: Arquivo Python solto na raiz. Deve ser movido para um micro-módulo.",
                    "severity": "ALTA"
                })

    # Relatório Final
    if not violations:
        print("✅ Tudo limpo! A Soberania de Silos está preservada.")
    else:
        print(f"⚠️ Encontradas {len(violations)} violações:")
        for v in violations:
            print(f"- [{v['severity']}] {v['file']}: {v['issue']}")

def check_folder_isolation(folder: Path, violations: List[Dict]):
    """Verifica se os arquivos dentro de um silo respeitam as regras."""
    for item in folder.iterdir():
        if item.is_file() and item.suffix == ".py":
            # Check line count
            try:
                line_count = len(item.read_text(encoding="utf-8").splitlines())
                if line_count > MAX_LINES:
                    violations.append({
                        "file": str(item),
                        "issue": f"Arquivo Monolítico: {line_count} linhas (Limite: {MAX_LINES}). Modularização necessária.",
                        "severity": "MÉDIA"
                    })
            except Exception:
                pass
        
        # Heurística: se o projeto tem muitos arquivos .py na sua raiz sem subpastas, avisar.
        py_files_in_root = list(folder.glob("*.py"))
        if len(py_files_in_root) > 10:
            violations.append({
                "file": str(folder),
                "issue": "Silo Poluído: Muitos arquivos (.py) na raiz do projeto. Agrupe-os em sub-módulos.",
                "severity": "BAIXA"
            })
            break

if __name__ == "__main__":
    audit_silos()
