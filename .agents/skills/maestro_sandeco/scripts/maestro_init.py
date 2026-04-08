import os
import json
import shutil
import sys
from pathlib import Path

# Adiciona o diretório de scripts ao path para importar path_utils
sys.path.append(os.path.dirname(__file__))
import path_utils

import sys
import io

# Forçar UTF-8 para evitar problemas com emojis no Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def init_maestro(project_name=None):
    print("🚀 Inicializando Maestro Environment...")
    
    root = path_utils.get_project_root()
    
    if project_name:
        project_path = root / "projects" / project_name
    else:
        # Tenta pegar do ambiente ou usa o root se for execução global
        project_path = Path(os.getenv("PEIXOTOCLAW_PROJECT_PATH", root))

    equipe_dir = project_path / ".antigravity" / "equipe"
    
    print(f"📂 Alvo: {equipe_dir}")

    # 1. Limpar travas
    travas_dir = equipe_dir / "travas"
    if travas_dir.exists():
        shutil.rmtree(travas_dir)
    travas_dir.mkdir(parents=True, exist_ok=True)
    print("✅ Travas limpas.")
    
    # 2. Limpar caixa de entrada
    inbox_dir = equipe_dir / "caixa_entrada"
    if inbox_dir.exists():
        shutil.rmtree(inbox_dir)
    inbox_dir.mkdir(parents=True, exist_ok=True)
    print("✅ Caixa de entrada limpa.")
    
    # 3. Resetar aviso geral
    aviso_file = equipe_dir / "aviso_geral.msg"
    with open(aviso_file, "w", encoding="utf-8") as f:
        f.write("Maestro online. Aguardando comandos.")
    print("✅ Aviso geral resetado.")
    
    print("\n[READY] O esquadrão está pronto para atuar.")

if __name__ == "__main__":
    p_name = sys.argv[1] if len(sys.argv) > 1 else None
    init_maestro(p_name)
