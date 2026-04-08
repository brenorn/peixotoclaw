import os
from pathlib import Path

def get_project_root() -> Path:
    """Retorna a raiz do projeto PeixotoClaw de forma dinâmica."""
    # Assume-se que este arquivo está em .agents/skills/maestro_sandeco/scripts/path_utils.py
    # Subir 4 níveis para chegar em PeixotoClaw/
    return Path(__file__).resolve().parent.parent.parent.parent.parent

def resolve_path(relative_path: str) -> Path:
    """Resolve um caminho relativo à raiz do projeto."""
    return get_project_root() / relative_path

if __name__ == "__main__":
    print(f"Raiz detectada: {get_project_root()}")
