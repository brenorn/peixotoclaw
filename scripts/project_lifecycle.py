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
BASE_PROJECTS_DIR = Path(r"d:\OneDrive\aiproj\PeixotoClaw\projects")
MAESTRO_INIT_SCRIPT = Path(r"d:\OneDrive\aiproj\PeixotoClaw\.agents\skills\maestro_sandeco\scripts\maestro_init.py")

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
    def __init__(self, projects_dir: Path = BASE_PROJECTS_DIR):
        self.projects_dir = projects_dir

    def create(self, project_name: str, goal: str = "Defina o objetivo central aqui"):
        project_path = self.projects_dir / project_name
        if project_path.exists():
            print(f"[ERRO] O projeto '{project_name}' já existe em {project_path}")
            return False

        print(f"🚀 Criando novo dossiê de projeto: {project_name}...")
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Criar subpastas padrão
        (project_path / "specs").mkdir(exist_ok=True)
        (project_path / "docs" / "management").mkdir(parents=True, exist_ok=True)
        (project_path / "data").mkdir(exist_ok=True)

        # Criar Arquivos Iniciais
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        (project_path / "PLAN.md").write_text(PLAN_TEMPLATE_PT.format(project_name=project_name, goal=goal, date=now), encoding="utf-8")
        (project_path / "TASKS.md").write_text(TASKS_TEMPLATE_PT.format(project_name=project_name), encoding="utf-8")
        (project_path / "CURRENT_CONTEXT.md").write_text(f"# Contexto Atual: {project_name}\n\nInicializado em {now}.", encoding="utf-8")

        print(f"✅ Estrutura criada em {project_path}")
        self.activate(project_name)
        return True

    def activate(self, project_name: str):
        project_path = self.projects_dir / project_name
        if not project_path.exists():
            print(f"[ERRO] Projeto '{project_name}' não encontrado.")
            return False

        print(f"📡 Ativando contexto para: {project_name}...")
        
        # Rodar Maestro Init
        os.system(f"python {MAESTRO_INIT_SCRIPT} {project_name}")
        
        # Setar variáveis de ambiente fictícias para o registro da sessão
        os.environ["PEIXOTOCLAW_PROJECT_PATH"] = str(project_path)
        
        print(f"📖 Lendo PLAN.md e TASKS.md para carga de contexto...")
        plan = (project_path / "PLAN.md").read_text(encoding="utf-8")
        tasks = (project_path / "TASKS.md").read_text(encoding="utf-8")
        
        print("-" * 30)
        print(f"RESUMO DO PROJETO: {project_name}")
        print("-" * 30)
        # Mostrar apenas as primeiras linhas para não inundar o terminal
        for line in plan.splitlines()[:5]: print(line)
        print("...")
        for line in tasks.splitlines()[:10]: print(line)
        
        print(f"\n[READY] Projeto {project_name} ativo e pronto para o Antigravity.")
        return True

    def persist_artifact(self, source_path: str, project_name: str, subfolder: str = "specs"):
        project_path = self.projects_dir / project_name
        if not project_path.exists():
            print(f"[ERRO] Não foi possível persistir artefato. Projeto {project_name} não existe.")
            return False

        dest_dir = project_path / subfolder
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        filename = os.path.basename(source_path)
        dest_path = dest_dir / filename
        
        shutil.copy2(source_path, dest_path)
        print(f"💾 Artefato espelhado com sucesso para: {dest_path}")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python project_lifecycle.py [create|activate|persist] [nome_projeto] [args...]")
        sys.exit(1)

    cmd = sys.argv[1]
    name = sys.argv[2]
    manager = ProjectLifecycleManager()

    if cmd == "create":
        goal = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "Defina o objetivo central aqui"
        manager.create(name, goal)
    elif cmd == "activate":
        manager.activate(name)
    elif cmd == "persist":
        if len(sys.argv) < 4:
            print("Erro: Caminho do artefato não especificado.")
            sys.exit(1)
        path = sys.argv[3]
        sub = sys.argv[4] if len(sys.argv) > 4 else "specs"
        manager.persist_artifact(path, name, sub)
