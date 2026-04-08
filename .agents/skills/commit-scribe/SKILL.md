---
name: commit-scribe
description: 'Analisa mudanças em PLAN.md, TASKS.md e specs/ para gerar mensagens de commit profissionais e precisas. Utilize após finalização de tarefas ou marcos do projeto, integrando-se ao PipelineMaestro.'
---

# Skill: commit-scribe (Escriba de Commits)

Esta habilidade automatiza a geração de mensagens de commit de alta qualidade, baseando-se na evolução da "Single Source of Truth" do projeto (PLAN.md, TASKS.md e Specs).

## 🎯 Missão

Garantir que o histórico do Git reflita fielmente as decisões arquiteturais e o progresso das tarefas, facilitando a auditoria técnica e a colaboração no Squad.

## 🚀 Como Funciona

### 1. Coleta de Contexto (Discovery)
O Escriba deve analisar:
- **PLAN.md**: Mudanças em decisões arquiteturais (ADRs), novos marcos ou revisões de roadmap.
- **TASKS.md**: Tarefas marcadas como concluídas `[x]` e novas tarefas adicionadas.
- **Directório `specs/`**: Novas especificações técnicas ou revisões em especificações existentes.
- **Deltas Físicos (Git)**: Analisar `git status` e `git diff --staged` (ou `git diff`) para verificar se os arquivos modificados condizem com as tarefas concluídas. Se houver mudanças no código não mapeadas no `TASKS.md`, alerte o usuário ou sugira a atualização de tarefas.

### 2. Integração com PipelineMaestro
Se acionado dentro de um fluxo de squad:
- Leia `.skills/pipeline-maestro/.antigravity/equipe/registro_atividades.json` para identificar a atividade corrente e seu estado.
- Relacione o commit à atividade do Maestro (ex: "SDD-T1", "SDD-T2").

### 3. Síntese da Mensagem (Synthesis)
Gere a mensagem seguindo o padrão **Conventional Commits**:
- `feat`: Novas funcionalidades.
- `fix`: Correção de bugs.
- `docs`: Mudanças apenas em documentação.
- `refactor`: Mudanças no código que não corrigem bugs nem adicionam funcionalidades.
- `chore`: Atualização de tarefas, manutenção, etc.

**Estrutura Esperada:**
```
[tipo]([escopo]): [descrição curta e imperativa]

[corpo detalhando as mudanças principais]

Ref: [ID da Task ou Decisão no PLAN.md]
```

## 📋 Regras de Ouro

1. **Seja Preciso**: Não invente mudanças. Se uma tarefa foi marcada como `[x]` mas o código não reflete isso, alerte o usuário.
2. **Contexto Arquitetural**: Commits que impactam o `PLAN.md` devem destacar a mudança de decisão técnica.
3. **Specs First**: Se uma spec foi criada, o commit deve mencionar a especificação que guiou a implementação.

## 🛠️ Exemplo de Uso

**Input:** "commit-scribe, gere o texto para o commit das mudanças de hoje."

**Processo:**
1. Analisa `PLAN.md` -> Detecta nova seção "Workflow Antigravity".
2. Analisa `TASKS.md` -> Detecta `[x] Workflow SkillCreator`.
3. Analisa `specs/` -> Detecta `specs/feature-x.md`.

**Output:**
```
feat(workflow): implementa skill-creator e documenta no PLAN.md

- Criação do workflow nativo .agent/workflows/skill-creator.md.
- Atualização do PLAN.md com a decisão arquitetural #16.
- Registro de conclusão da tarefa na seção de Gestão de Skills no TASKS.md.

Ref: SDD-T1, PLAN:Section16
```

---
> [!TIP]
> Use esta skill sempre antes de realizar o `git commit` para garantir que a mensagem esteja alinhada com os documentos de gestão do projeto.
