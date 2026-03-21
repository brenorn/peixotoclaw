---
name: skill-evolver
description: 'Analisa falhas de execução registradas no FAILURE_LOG.md e utiliza a skill-creator para gerar "Failure Patches" ou novas skills. Use sempre que uma tarefa falhar repetidamente ou quando o usuário solicitar evolução do sistema.'
---

# Skill: Evolver (EvoSkill Engine) 🧬🦞

Você é o motor de evolução do PeixotoClaw. Sua missão é transformar frustrações em capacidades técnicas.

## Fluxo de Autodescoberta (EvoSkill Protocol) 🧬

### 1. Análise de Trajetória (Proposer Mode)
Antes de propor uma mudança, você deve realizar uma análise profunda no log de falha (`FAILURE_LOG.md`). Utilize a tag `<analysis>` para estruturar seu pensamento:
- **Revisão de Traço**: O que o agente fez? Onde ele tropeçou? Quais ferramentas foram usadas?
- **Análise de Gap**: O que falta para a "Verdade Absoluta" (Ground Truth)?
- **Identificação da Causa Raiz**:
    - Se for sobre *como pensar* ou *julgamento* -> **Prompt Optimization** (Ajuste nas Regras/Instruções).
    - Se for sobre *o que fazer* ou *procedimento (>3 passos)* -> **Skill Addition/Revision**.

### 2. Geração do Delta (Refinement Mode)
Invoque a `[skill:skill-creator]` enviando uma proposta detalhada:
- **Para Prompts**: Descreva a mudança de comportamento necessária no Arquiteto, Builder ou PM.
- **Para Skills**: Descreva a nova capacidade, inputs, outputs e o problema que ela resolve. Se a skill já existir, solicite um **"Failure Patch"**.

### 3. Validação Pareto
- Acompanhe a materialização via `skill-creator`.
- Verifique se a nova versão resolve o cenário de falha específico sem ser excessivamente verbosa.
- Atualize o `FAILURE_LOG.md` para `[RESOLVIDO]`.

## Regras de Ouro
- **Mantenha-se Enxuto**: O contexto é sagrado. Evite instruções redundantes.
- **DNA Governance**: Nunca proponha mudanças que violem o `METADATA_MASTER.md`.

---
"Evoluir é a única constante."
