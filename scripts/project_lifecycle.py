import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import sys

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Caminhos Base de Configuração
PEIXOTOCLAW_ROOT = Path(r"d:\OneDrive\aiproj\PeixotoClaw")
LEGACY_PROJECTS_DIR = PEIXOTOCLAW_ROOT / "projects"
REGISTRY_PATH = PEIXOTOCLAW_ROOT / "projects.json"
SKILLS_MANIFEST_PATH = PEIXOTOCLAW_ROOT / "skills_manifest.json"
MAESTRO_INIT_SCRIPT = PEIXOTOCLAW_ROOT / ".agents" / "skills" / "maestro_sandeco" / "scripts" / "maestro_init.py"

PLAN_TEMPLATE_PT = """# 🧪 PLANO: {project_name}

**Objetivo Central**: {goal}

---

## 🚀 Cenário 1: O Mais Rápido (MVP)
*Foco: Validação imediata da prova de conceito.*
- [ ] Definir requisitos mínimos.
- [ ] Implementar esqueleto funcional.
- [ ] Teste de fumaça inicial.

## 🛡️ Cenário 2: O Mais Seguro (Auditável)
*Foco: Governança, logs e segurança.*
- [ ] Todas as ações passam pelo auditor.
- [ ] Logs detalhados em cada interação.
- [ ] Validação contra injeção de prompt e vazamento de dados.

## 🏗️ Cenário 3: O Mais Escalável (SaaS Factory)
*Foco: Industrialização e crescimento.*
- [ ] Arquitetura modular e reaproveitável.
- [ ] Documentação completa para handover.
- [ ] Preparação para múltiplos usuários/instâncias.

---
**SSOT (Dossiê do Projeto)**: [CURRENT_CONTEXT.md](./CURRENT_CONTEXT.md)
**Status**: Inicializado em {date}
"""

TASKS_TEMPLATE_PT = """# ✅ TAREFAS: {project_name}

## Fase 1: Inicialização e Setup
- [ ] Configuração do diretório de projeto
- [ ] Criação do Plano Estratégico (Cenários 1, 2, 3)
- [ ] Primeira sanitização via Maestro

## Fase 2: Desenvolvimento
- [ ] (Aguardando definição de escopo...)

## Fase 3: Auditoria e Entrega
- [ ] Verificação de qualidade final
- [ ] Geração de Walkthrough
"""

class ProjectLifecycleManager:
    def __init__(self):
        self.registry = self._load_registry()

    def _load_registry(self):
        if REGISTRY_PATH.exists():
            return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        return {}

    def get_project_path(self, project_name: str, module_name: str = None) -> Path:
        """Resolve o caminho do projeto ou de um módulo específico."""
        # 1. Check Registry
        if project_name in self.registry:
            entry = self.registry[project_name]
            
            # Se for um dicionário (Projeto Composto)
            if isinstance(entry, dict):
                modules = entry.get("modules", {})
                default_mod = entry.get("default")
                
                # Se um módulo foi solicitado
                if module_name and module_name in modules:
                    return Path(modules[module_name])
                
                # Se não há módulo, mas há um default
                if default_mod and default_mod in modules:
                    return Path(modules[default_mod])
                
                # Se não há nada, tenta o primeiro módulo ou a chave 'root' (retrocompatibilidade)
                if modules:
                    return Path(list(modules.values())[0])
                if "root" in entry:
                    return Path(entry["root"])
                    
            # Se for apenas uma string (Projeto Simples)
            return Path(entry)
        
        # 2. Check Legacy Folder
        legacy_path = LEGACY_PROJECTS_DIR / project_name
        if legacy_path.exists():
            return legacy_path
            
        # 3. Default to sibling directory (heuristic)
        sibling_path = PEIXOTOCLAW_ROOT.parent / project_name
        return sibling_path

    def get_dossier_path(self, project_root: Path) -> Path:
        """Retorna o caminho da pasta de dossiê (_peixotoclaw)"""
        # Se o root for a pasta central de projetos, o dossiê é a própria pasta
        if LEGACY_PROJECTS_DIR in project_root.parents or project_root.parent == LEGACY_PROJECTS_DIR:
            return project_root
        return project_root / "_peixotoclaw"

    def create(self, project_name: str, goal: str = "Defina o objetivo central aqui"):
        root_path = self.get_project_path(project_name)
        dossier_path = self.get_dossier_path(root_path)

        if dossier_path.exists():
            print(f"[ERRO] O dossiê para '{project_name}' já existe em {dossier_path}")
            return False

        print(f"🚀 Criando novo dossiê de projeto em: {dossier_path}...")
        dossier_path.mkdir(parents=True, exist_ok=True)
        
        # Criar subpastas padrão
        (dossier_path / "specs").mkdir(exist_ok=True)
        (dossier_path / "docs" / "management").mkdir(parents=True, exist_ok=True)
        (dossier_path / "data").mkdir(exist_ok=True)

        # Criar Arquivos Iniciais
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        (dossier_path / "PLAN.md").write_text(PLAN_TEMPLATE_PT.format(project_name=project_name, goal=goal, date=now), encoding="utf-8")
        (dossier_path / "TASKS.md").write_text(TASKS_TEMPLATE_PT.format(project_name=project_name), encoding="utf-8")
        (dossier_path / "CURRENT_CONTEXT.md").write_text(f"# Contexto Atual: {project_name}\n\nInicializado em {now}.", encoding="utf-8")

        print(f"✅ Estrutura criada com sucesso.")
        self.activate(project_name)
        return True

    def activate(self, project_name: str, module_name: str = None):
        # Detectar se é composto e qual módulo focar
        entry = self.registry.get(project_name)
        active_module = module_name
        
        if isinstance(entry, dict) and "modules" in entry:
            modules = entry["modules"]
            if not active_module:
                if len(modules) > 1:
                    print(f"\n📂 O projeto '{project_name}' possui múltiplos módulos:")
                    for i, mod in enumerate(modules.keys(), 1):
                        print(f"  {i}. {mod} -> {modules[mod]}")
                    
                    try:
                        # Tentar ler do TTY se disponível, senão falhar para manual
                        choice = input(f"\nEscolha o módulo para focar (1-{len(modules)}) [ou nome]: ").strip()
                        if choice.isdigit() and 1 <= int(choice) <= len(modules):
                            active_module = list(modules.keys())[int(choice)-1]
                        elif choice in modules:
                            active_module = choice
                        else:
                            active_module = entry.get("default", list(modules.keys())[0])
                    except EOFError:
                        active_module = entry.get("default", list(modules.keys())[0])
                else:
                    active_module = list(modules.keys())[0]

        root_path = self.get_project_path(project_name, active_module)
        dossier_path = self.get_dossier_path(root_path)

        # Tentar migração se a pasta legacy existir e o alvo não
        legacy_path = LEGACY_PROJECTS_DIR / project_name
        if legacy_path.exists() and not dossier_path.exists() and legacy_path != root_path:
            self.migrate(project_name, module_name=active_module)

        if not dossier_path.exists():
            print(f"[ERRO] Dossiê não encontrado em {dossier_path}")
            print(f"Dica: Tente 'python project_lifecycle.py create {project_name}' para inicializar.")
            return False

        print(f"📡 Ativando contexto para: {project_name}" + (f" (Módulo: {active_module})" if active_module else ""))
        print(f"📂 Root: {root_path}")
        print(f"📂 Dossiê: {dossier_path}")
        
        # Rodar Maestro Init (usando o nome do módulo se presente)
        maestro_id = f"{project_name}.{active_module}" if active_module else project_name
        os.system(f"python \"{MAESTRO_INIT_SCRIPT}\" {maestro_id}")
        
        # Setar variáveis de ambiente
        os.environ["PEIXOTOCLAW_PROJECT_PATH"] = str(root_path)
        os.environ["PEIXOTOCLAW_DOSSIER_PATH"] = str(dossier_path)
        os.environ["PEIXOTOCLAW_ACTIVE_MODULE"] = str(active_module or "")
        
        print(f"📖 Lendo PLAN.md e TASKS.md...")
        plan_content = (dossier_path / "PLAN.md").read_text(encoding="utf-8")
        tasks_content = (dossier_path / "TASKS.md").read_text(encoding="utf-8")
        
        print("-" * 30)
        print(f"RESUMO DO PROJETO: {project_name.upper()} ({active_module or 'ROOT'})")
        print("-" * 30)
        for line in plan_content.splitlines()[:5]: print(line)
        print("...")
        for line in tasks_content.splitlines()[:10]: print(line)
        
        self.show_skills_inventory()
        
        print(f"\n[READY] Projeto {project_name} ativo e pronto para o Antigravity.")
        return True

    def show_skills_inventory(self):
        if SKILLS_MANIFEST_PATH.exists():
            print("\n🛠️  INVENTÁRIO DE SKILLS (Resumo):")
            manifest = json.loads(SKILLS_MANIFEST_PATH.read_text(encoding="utf-8"))
            for skill in manifest.get("skills", [])[:15]: # Mostrar as primeiras 15
                print(f" - {skill['name']}: {skill['description'][:60]}...")
            if manifest.get("total", 0) > 15:
                print(f" ... e mais {manifest['total'] - 15} habilidades disponíveis.")

    def migrate(self, project_name: str, module_name: str = None):
        legacy_path = LEGACY_PROJECTS_DIR / project_name
        root_path = self.get_project_path(project_name, module_name)
        dossier_path = self.get_dossier_path(root_path)

        if legacy_path.exists() and not dossier_path.exists():
            print(f"🚚 Migrando dossiê de {legacy_path} para {dossier_path}...")
            shutil.copytree(legacy_path, dossier_path)
            # Marcar legacy como migrado (apenas se for o root ou o único módulo)
            migrated_name = legacy_path.parent / (legacy_path.name + ".migrated")
            if not migrated_name.exists():
                os.rename(legacy_path, migrated_name)
            print(f"✅ Migração concluída.")
            return True
        return False

    def add_module(self, project_name: str, module_name: str, module_path: str):
        """Adiciona um novo módulo a um projeto existente."""
        module_path = Path(module_path).absolute()
        
        # Carregar registro atual
        if project_name not in self.registry:
            # Se o projeto não existe no registro, cria como simples primeiro
            self.registry[project_name] = str(module_path.parent)
            
        entry = self.registry[project_name]
        
        # Converter string para dict se necessário
        if isinstance(entry, str):
            self.registry[project_name] = {
                "default": "root",
                "modules": {
                    "root": entry
                }
            }
            entry = self.registry[project_name]

        # Adicionar o módulo
        entry["modules"][module_name] = str(module_path)
        
        # Salvar registro
        REGISTRY_PATH.write_text(json.dumps(self.registry, indent=2), encoding="utf-8")
        print(f"✅ Módulo '{module_name}' adicionado ao projeto '{project_name}' em {module_path}")
        
        # Bootstrap do modulo
        self.activate(project_name, module_name=module_name)
        return True

    def persist_artifact(self, source_path: str, project_name: str, subfolder: str = "specs"):
        root_path = self.get_project_path(project_name)
        dossier_path = self.get_dossier_path(root_path)

        if not dossier_path.exists():
            print(f"[ERRO] Não foi possível persistir. Dossiê {dossier_path} não existe.")
            return False

        dest_dir = dossier_path / subfolder
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        filename = os.path.basename(source_path)
        dest_path = dest_dir / filename
        
        shutil.copy2(source_path, dest_path)
        print(f"💾 Artefato espelhado para: {dest_path}")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python project_lifecycle.py [create|activate|persist|migrate] [nome_projeto] [args...]")
        sys.exit(1)

    cmd = sys.argv[1]
    name = sys.argv[2]
    manager = ProjectLifecycleManager()

    if cmd == "create":
        goal = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "Defina o objetivo central aqui"
        manager.create(name, goal)
    elif cmd == "activate":
        module = None
        for arg in sys.argv:
            if arg.startswith("--module="):
                module = arg.split("=")[1]
        manager.activate(name, module_name=module)
    elif cmd == "add-module":
        if len(sys.argv) < 5:
            print("Uso: python project_lifecycle.py add-module [projeto] [nome_modulo] [caminho]")
            sys.exit(1)
        mod_name = sys.argv[3]
        mod_path = sys.argv[4]
        manager.add_module(name, mod_name, mod_path)
    elif cmd == "persist":
        if len(sys.argv) < 4:
            print("Erro: Caminho do artefato não especificado.")
            sys.exit(1)
        path = sys.argv[3]
        sub = sys.argv[4] if len(sys.argv) > 4 else "specs"
        manager.persist_artifact(path, name, sub)
    elif cmd == "migrate":
        manager.migrate(name)
