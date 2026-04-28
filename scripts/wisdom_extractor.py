import json
import os
import sys
from pathlib import Path

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except:
        pass

# Configuração de Caminhos
PROJECT_ROOT = Path(__file__).parent.parent
WISDOM_DIR = PROJECT_ROOT / ".agents" / "brain" / "wisdom"
PATTERNS_FILE = WISDOM_DIR / "global_patterns.json"

def init_wisdom():
    """Inicializa os arquivos de sabedoria se não existirem."""
    WISDOM_DIR.mkdir(parents=True, exist_ok=True)
    if not PATTERNS_FILE.exists():
        initial_data = {
            "insights": [],
            "security_alerts": [],
            "performance_tips": []
        }
        PATTERNS_FILE.write_text(json.dumps(initial_data, indent=2, ensure_ascii=False), encoding="utf-8")

def add_insight(category, project_name, insight_text):
    """Adiciona um insight à base de conhecimento global."""
    init_wisdom()
    data = json.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
    
    entry = {
        "project": project_name,
        "content": insight_text,
        "recorded_at": Path().absolute().as_posix() # Apenas para contexto
    }
    
    if category in data:
        data[category].append(entry)
        # Manter apenas os últimos 50 por categoria para não explodir o contexto
        data[category] = data[category][-50:]
        
    PATTERNS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"🧠 [BRAIN] Insight registrado na categoria '{category}' vindo de '{project_name}'.")

def get_relevant_wisdom():
    """Retorna os insights globais para o Maestro usar como contexto."""
    if not PATTERNS_FILE.exists():
        return "Nenhum insight global registrado ainda."
    return PATTERNS_FILE.read_text(encoding="utf-8")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        # Modo leitura se não houver args suficientes
        print(get_relevant_wisdom())
    else:
        # Modo escrita: python wisdom_extractor.py [category] [project] [text]
        add_insight(sys.argv[1], sys.argv[2], " ".join(sys.argv[3:]))
