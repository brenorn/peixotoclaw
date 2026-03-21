# PeixotoClaw: A Pequena Máquina de Estudo e Execução (SDD)

Este documento é a **Constituição** do projeto. Ele define as diretrizes inegociáveis que todos os agentes (Arquiteto, Construtor, PM) devem seguir.

---

## 1. Visão Arquitetural
- **Core**: Sistema de agentes distribuídos e modularizados.
- **Paradigma**: Spec-Driven Development (SDD) Nível 2 (Spec-anchored).
- **Referência Técnica**: [.agents/brain/estudo_sdd.md](file:///.agents/brain/estudo_sdd.md).
- **Modelo de Trabalho**: Plataforma Engine (Core) + Implementações (Projects).

---

## 2. Regras de Ouro (Constituição)
1.  **Nenhuma linha de código sem Spec**: Não implemente nada que não esteja detalhado na pasta `/specs` (ou em tarefas explícitas em `TASKS.md`).
2.  **Modularidade Extrema**: Novas capacidades devem ser Skills isoladas no diretório `.agents/skills`.
3.  **TDD Obligatório**: Toda feature nova deve- [x] Final Consolidation and Archival <!-- id: 6 -->
    - [x] Create detailed study files in D:\OneDrive\aiproj\PeixotoClaw\diego <!-- id: 7 -->
    - [x] Create PLAN.md, TASKS.md and CURRENT_CONTEXT.md at root <!-- id: 18 -->
    - [x] Setup .agents/rules/ directory with specialists <!-- id: 19 -->
    - [x] Setup Skill Map and Project Isolation Architecture <!-- id: 24 -->
este projeto, utilizamos as personas definidas em `.agents/rules/`:
- **Lead Architect**: Responsável por este arquivo e pelo `PLAN.md`.
- **Senior Builder**: Traduz planos em código TypeScript/Python eficiente.
- **Technical PM**: Garante que o `TASKS.md` reflita exatamente o estado do software.

---

## 4. Tecnologias e Stack
- **Run**: Node.js / Python.
- **AI Sync**: @hivehub/rulebook.
- **Context Opt**: LessTokens (API Base: https://lesstokens.hive-hub.ai).

---
> [!IMPORTANT]
> Se houver conflito entre o prompt e este PLAN.md, a decisão deste arquivo prevalece.
