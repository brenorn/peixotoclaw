import shutil
import json
import sys
from pathlib import Path

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuração de Caminhos
PROJECT_ROOT = Path(__file__).parent.parent
ACTIVE_SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"
RESERVE_SKILLS_DIR = Path(r"d:\OneDrive\aiproj\sandeco-prompts")

def get_reserve_skills():
    """Busca todas as skills (pastas com SKILL.md) na pasta de reserva."""
    skills = {}
    for skill_file in RESERVE_SKILLS_DIR.rglob("SKILL.md"):
        skill_dir = skill_file.parent
        # Chave é o nome da pasta, valor é o caminho completo
        skills[skill_dir.name] = skill_dir
    return skills

def list_skills():
    """Lista skills ativas e disponíveis na reserva."""
    active = [d.name for d in ACTIVE_SKILLS_DIR.iterdir() if d.is_dir()]
    reserve = get_reserve_skills()
    
    print("\n🚀 --- SKILLS ATIVAS ---")
    for s in sorted(active):
        status = " (Main)" if s in reserve else ""
        print(f" ✅ {s}{status}")
        
    print("\n📦 --- SKILLS NA RESERVA ---")
    for s in sorted(reserve.keys()):
        if s not in active:
            print(f" 💤 {s}")
    print("-" * 30)

def summon(skill_name):
    """Traz uma skill da reserva para a pasta principal."""
    reserve = get_reserve_skills()
    if skill_name not in reserve:
        print(f"[ERRO] Skill '{skill_name}' não encontrada na reserva.")
        return

    src = reserve[skill_name]
    dest = ACTIVE_SKILLS_DIR / skill_name
    
    if dest.exists():
        print(f"[AVISO] A skill '{skill_name}' já está ativa.")
        return

    print(f"📡 Convocando {skill_name} da reserva...")
    shutil.copytree(src, dest)
    print(f"✅ Skill '{skill_name}' ativada com sucesso.")

def dismiss(skill_name):
    """Move uma skill da pasta principal para a reserva (mantendo backup na reserva)."""
    target = ACTIVE_SKILLS_DIR / skill_name
    
    if not target.exists():
        print(f"[ERRO] Skill '{skill_name}' não encontrada na pasta ativa.")
        return

    print(f"🧹 Desativando {skill_name}...")
    # Como a reserva é o repositório oficial, apenas removemos da pasta ativa
    # para não poluir o prompt, já que a cópia mestre está na sandeco-prompts.
    shutil.rmtree(target)
    print(f"✅ Skill '{skill_name}' retornou para a reserva.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python scripts/skill_manager.py [list|summon|dismiss] [nome_skill]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    
    if cmd == "list":
        list_skills()
    elif cmd == "summon":
        if len(sys.argv) < 3:
            print("Erro: Especifique o nome da skill.")
        else:
            summon(sys.argv[2])
    elif cmd == "dismiss":
        if len(sys.argv) < 3:
            print("Erro: Especifique o nome da skill.")
        else:
            dismiss(sys.argv[2])
