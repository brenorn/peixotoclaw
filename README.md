# peixotoclaw (Monster Edition) 🦖

> [!CAUTION]
> **ATENÇÃO IA**: Este projeto utiliza uma arquitetura de Multi-Agentes complexa e reativa.
> LEIA O ARQUIVO [**HANDOVER.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/docs/management/HANDOVER.md) ANTES DE QUALQUER AÇÃO.

---

## 🏗️ Visão Geral
PeixotoClaw é uma plataforma engine para desenvolvimento automatizado de agentes e orquestração de processos complexos. Controlado via **Telegram** ou interfaces especializadas de IA (como Antigravity), ele combina a inteligência de LLMs de ponta com a capacidade de interagir diretamente com o sistema de arquivos e executar habilidades especializadas.

---

## ⚡ O que você pode fazer com o PeixotoClaw?

### 🤖 Orquestração Reativa (Novo!)
O sistema agora é capaz de reconhecer intenções de linguagem natural para gerenciar o ciclo de vida de projetos satélites:
- **Ativação de Contexto**: *"Vamos trabalhar com o projeto [Nome]"*
- **Criação de Dossiê**: *"Vamos iniciar o projeto [Nome]"*
- **Persistência de Artefatos**: Todo planejamento é espelhado automaticamente no dossiê local em `projects/`.

### 📂 Habilidades Integradas
- **💻 Coder**: Criação, refatoração e arquitetura de código local.
- **📄 Analista de Documentos**: Processamento de PDFs e extração de dados.
- **🎓 Academic Writer (Nexus V5)**: Motor de mentoria e escrita acadêmica Q1.
- **🦖 SandecoMaestro**: Coordenação de times de agentes (Architect, Builder, PM).

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
