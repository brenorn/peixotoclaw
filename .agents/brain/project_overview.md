# PeixotoClaw: Arquitetura e Funcionamento 🦞

PeixotoClaw é um ecossistema de agentes de IA modular, local e expansível, projetado para operar via Telegram e uma interface web (Neural Dashboard).

## 🚀 Tecnologias Principais
- **Backend**: Node.js v20+, TypeScript, Express.
- **IA**: Google Gemini 2.0 (via SDK) e DeepSeek.
- **Interface**: [grammY](https://grammy.dev/) (Telegram), React/Vite (Dashboard).
- **Persistência**: SQLite (via `better-sqlite3`).
- **Multimodalidade**: Whisper (STT), Edge-TTS (TTS), PDF-Parse.

## 🏗️ Arquitetura do Sistema

O projeto segue um padrão de **Agentic Loop (ReAct)**, onde o agente "pensa" antes de executar ações.

### 1. Camada de Interface
- **Telegram (`TelegramInputHandler`)**: Recebe textos, áudios (transcritos via Whisper) e documentos (PDF/Markdown).
- **Dashboard (`server.ts`)**: API REST que permite interagir com o robô via web, gerenciar conversas e instalar novas habilidades.

### 2. Camada de Orquestração (`AgentController`)
- Gerencia o ciclo de vida de uma mensagem.
- Realiza o **Skill Routing**: identifica automaticamente qual habilidade especializada deve ser ativada com base no input do usuário.
- Enriquece o prompt com contexto de conversas passadas e conteúdo de anexos.

### 3. Loop de Execução (`AgentLoop`)
- Implementa o ciclo **Thought -> Action -> Observation**.
- Utiliza ferramentas (Tools) registradas para interagir com o sistema de arquivos ou APIs externas.

### 4. Sistema de Skills
Localizadas em `.agents/skills/`, as habilidades são carregadas dinamicamente (Hot-Reload).
- Cada skill é definida em um arquivo `SKILL.md` com metadados YAML.
- **Segurança**: Novas skills instaladas via API passam por uma auditoria automática realizada por uma skill especializada (`skill-auditor`).

## 📂 Estrutura de Pastas
- `src/core/`: Lógica central (AgentLoop, SkillLoader, SkillRouter, Memory).
- `src/infra/`: Provedores de LLM, Database e serviços de Voz (STT/TTS).
- `src/interfaces/`: Ponto de entrada do Telegram.
- `dashboard/`: Aplicação frontend moderna para controle do agente.
- `.agents/skills/`: O "cérebro" expandível do sistema.

## 🛠️ Recursos Diferenciados
- **Local-First**: Foco em privacidade e execução local.
- **Multilíngue**: Detecção automática e resposta no idioma do usuário.
- **Auditoria de Código**: Proteção contra skills maliciosas durante a instalação.
- **Memória de Longo Prazo**: Histórico persistente e context-aware.
