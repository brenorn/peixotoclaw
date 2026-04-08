---
name: gsd-engine
description: 'Motor de orquestração universal PeixotoClaw baseado no framework Get-Shit-Done (GSD). Versão Python Pro.'
---

# Skill: GSD-Engine (Monster Edition) 🐉🦾

Este é o sistema nervoso central do PeixotoClaw. Ele implementa a lógica de automação de alto nível para planejamento, execução e verificação de qualquer projeto (SaaS, Documentos, IA, etc).

## 🚀 Funcionalidades (Python First)
1. **Governança Estrita**: Gestão de `ROADMAP.md` e `STATE.md` via `state.py`.
2. **Segurança de Prompt**: Sanitização e proteção contra injeção via `security.py`.
3. **Padrão Goal-Backward**: Metodologia de planejamento reverso para zero ambiguidade.
4. **HMR (Hybrid Model Router)**: Mixagem de Claude e Gemini para economia e performance.

## 🛠️ Comandos (Orquestração)
- **Init**: Inicializa a estrutura `.planning/` em qualquer diretório.
- **Plan**: Conduz o ciclo de planejamento de fases.
- **Execute**: Gerencia a implementação atômica com commits automáticos.
- **Validate**: Roda a auditoria Nyquist para garantir 100% de cobertura de testes.

## 📁 Estrutura
- `lib/`: Drivers fundamentais em Python 3.10+.
- `agents/`: Prompts de sistema para subagentes especializados.
- `workflows/`: Fluxos de trabalho sequenciais.
- `templates/`: Modelos para PLAN, SUMMARY e STATE.

---
"Rigor é o segredo da autonomia AI."
