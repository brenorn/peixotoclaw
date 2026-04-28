# peixotoclaw (Monster Edition) 🦖

> [!CAUTION]
> **ATENÇÃO IA**: Este projeto utiliza uma arquitetura de Multi-Agentes complexa e reativa.
> LEIA O ARQUIVO [**HANDOVER_MONSTER.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/docs/HANDOVER_MONSTER.md) ANTES DE QUALQUER AÇÃO.

---

## 🏗️ Visão Geral
PeixotoClaw é uma plataforma engine para desenvolvimento automatizado de agentes e orquestração de processos complexos. Agora em sua **Versão Industrial (Lean)**, ele utiliza uma infraestrutura ultra-leve baseada nos protocolos do Professor Sandeco, garantindo mínima latência e máxima eficácia.

---

## ⚡ O que você pode fazer com o PeixotoClaw?

### 🤖 Automação Industrial e Proatividade (Novo!)
O sistema agora é capaz de reconhecer intenções e agir de forma autônoma:
- **Diagnóstico Automático**: Ao ativar um projeto, o Maestro analisa a maturidade (`auto_pipeline.py`) e sugere o próximo passo (PRD -> Spec -> Código).
- **Cofre de Habilidades (Skill Vault)**: Gerenciamento de memória ativa. Mantenha apenas o essencial no prompt e chame o resto da reserva quando necessário (`skill_manager.py`).
- **Ativação de Contexto**: *"Vamos trabalhar com o projeto [Nome]"*
- **Criação de Dossiê**: *"Vamos iniciar o projeto [Nome]"* em conformidade com a Engenharia de Software Pragmática.

### 📂 Habilidades Integradas (Highlights)
- **💻 Coder**: Implementação técnica de elite seguindo a "Regra dos 500".
- **🦖 SandecoMaestro (Raiz)**: Orquestração de esquadrão com 14 papéis especializados, unificada na raiz para sincronia total.
- **🎬 YouTube Creative Suite**: Suite completa (Pesquisa, Roteiro, SEO) integrada em um único silo.
- **🧠 Token Reduce (Sandeco Special)**: Compressão generativa de prompts para economia de tokens e latência.
- **🛡️ Auto-Fallback**: Alternância automática de provedores para resiliência 24/7.

---

## 🚀 Quick Start & Installation

If you just cloned this repository, you **MUST** initialize the environment structure before running the system:

1. **Run Bootstrap**:
   ```bash
   python scripts/bootstrap.py
   ```
   *This will create the necessary folders (`projects/`, `data/`, etc.) and set up your `.env` template.*

2. **Configure Credentials**:
   Edit the generated `.env` file with your API keys (Gemini, Claude, Telegram, etc.).

3. **Install Dependencies**:
   ```bash
   npm install
   cd dashboard && npm install
   ```

4. **Launch**:
   Run `peixotoclaw.bat` or `npm run ui:dev`.

---

## 🧠 AI Workflow

O uso operacional de Codex, Claude, Antigravity, Ollama, skills locais e smoke visual esta documentado em [AI_WORKFLOW_PEIXOTOCLAW.md](file:///d:/OneDrive/aiproj/PeixotoClaw/docs/AI_WORKFLOW_PEIXOTOCLAW.md).

---

## 🚀 Como Iniciar uma Sessão (Tutorial)

Para começar a trabalhar de forma eficiente, você possui duas formas de interação:

### 1. Comandos de Barra (Slash Commands)
Digite `/` no chat para ver a lista de habilidades rápidas:
- `/project-activate`: Para retomar um dossiê de projeto existente.
- `/project-create`: Para iniciar um novo dossiê de planejamento.
- `/sandeco-maestro`: Para orquestrar tarefas complexas com múltiplos agentes.

### 2. Gatilhos de Linguagem Natural (Recomendado)
Eu (seu assistente) estou treinado para reagir proativamente. Você pode simplesmente dizer:
- *"Vamos iniciar o projeto Simulador-Obras"* -> Eu criarei a pasta, os planos (Fast/Secure/Scalable) e as tarefas iniciais em **Português**.
- *"Vamos trabalhar com o projeto MAS-Doctorate"* -> Eu limparei o ambiente e carregarei todo o contexto histórico do projeto.

---

## 📂 Estrutura de Diretórios
- `.agents/`: Motor, regras globais e habilidades.
- `projects/`: **Dossiês dos Projetos** (Históricos, Planos, Documentos e Contexto).
- `scripts/`: Utilitários de gerenciamento e ciclo de vida.
- `docs/`: Documentação técnica e manuais de Handover.

---

## 🎖️ Créditos e Agradecimentos
- **Prof. Sandeco** ([@sandeco](https://github.com/sandeco)): Pela visão mestre e mentoria.
- **Breno Peixoto**: Desenvolvimento e Manutenção.

**Status:** Alpha v1.0 - PeixotoClaw Monster Ready 🚀🦾
