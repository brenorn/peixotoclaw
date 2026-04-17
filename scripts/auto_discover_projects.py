import os
import sys
from pathlib import Path
import json

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

AIPROJ_ROOT = Path(r"d:\OneDrive\aiproj")
PEIXOTOCLAW_ROOT = AIPROJ_ROOT / "PeixotoClaw"
REGISTRY_PATH = PEIXOTOCLAW_ROOT / "projects.json"

def discover():
    registry = {}
    if REGISTRY_PATH.exists():
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    # Pastas em aiproj que são projetos em potencial
    potentials = [d for d in AIPROJ_ROOT.iterdir() if d.is_dir() and not d.name.startswith(".") and d.name != "PeixotoClaw"]
    
    # Pastas em legacy que precisam de um lar
    legacy_dir = PEIXOTOCLAW_ROOT / "projects"
    legacies = [d.name for d in legacy_dir.iterdir() if d.is_dir() and not d.name.endswith(".migrated")]

    print(f"🔍 Encontrados {len(potentials)} diretórios em aiproj.")
    
    for p in potentials:
        if p.name not in registry:
            # Tentar match exato ou parcial com legado
            registry[p.name] = str(p)
            print(f"🆕 Sugerindo mapeamento: {p.name} -> {p}")

    # Salvar
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding="utf-8")
    print("\n✅ projects.json atualizado com descobertas.")

if __name__ == "__main__":
    discover()
