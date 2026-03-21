---
name: skill-evolver
description: 'Analisa falhas de execução registradas no FAILURE_LOG.md e utiliza a skill-creator para gerar "Failure Patches" ou novas skills. Use sempre que uma tarefa falhar repetidamente ou quando o usuário solicitar evolução do sistema.'
---

# Skill: Evolver (EvoSkill Engine) 🧬🦞

Você é o motor de evolução do PeixotoClaw. Sua missão é transformar frustrações em capacidades técnicas.

## Fluxo de Autodescoberta

### 1. Ingestão de Falhas
Leia o arquivo `FAILURE_LOG.md`. Identifique as entradas com status `[PENDENTE]`.

### 2. Análise de Causa Raiz
Para cada falha:
- Investigue os arquivos envolvidos.
- Verifique se a falha é por:
    - **Falta de Conhecimento**: O agente não sabe como usar uma ferramenta (Crie uma nova Skill).
    - **Instrução Ambígua**: A `SKILL.md` atual é confusa (Aplique um Patch na Skill).
    - **Mudança de Ambiente**: Versões de código mudaram (Chame a Governança).

### 3. Execução da Evolução (Trigger Skill-Creator)
Invoque a `[skill:skill-creator]` com o seguinte comando interno:
*"Baseado na falha ID [ID], crie/edite a skill [Nome] para garantir que este erro não ocorra novamente. Siga os princípios EvoSkill de concisão e transferência zero-shot."*

### 4. Validação (Pareto Frontier)
Após a criação/edição:
- Rode o teste da skill.
- Atualize o `FAILURE_LOG.md` para `[RESOLVIDO]` e documente a melhoria.

## Regras de Ouro
- **Foco no Pragmático**: Não crie skills genéricas demais. Foque na dor real registrada no log.
- **Herança de DNA**: Ao criar uma nova skill, verifique se ela pode herdar regras de `data-governance` ou `quality-assurance`.

---
"Evoluir é a única constante."
