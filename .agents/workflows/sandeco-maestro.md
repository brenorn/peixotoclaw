---
description: PeixotoClaw SandecoMaestro (Orquestração Multi-Agente) 🦖
---

Este workflow formaliza o ciclo de vida de desenvolvimento do ecossistema PeixotoClaw, utilizando a lógica do **SandecoMaestro** para coordenar esquadrões de agentes inteligentes em projetos satélites.

> [!CAUTION]
> NUNCA inicie alterações sem executar a **Fase 1: Handover & Inicialização**.

## Fase 1: Handover & Inicialização 🦞

1.  **Seleção de Projeto Ativo**:
    - Liste os subdiretórios de `projects/`.
    - Pergunte ao usuário qual projeto será o foco desta sessão (ex: `MAS-Doctorate`, `SafeAssessment`).
    - Defina a variável de ambiente (fictícia para contexto): `SET PEIXOTOCLAW_PROJECT_PATH=D:\OneDrive\aiproj\PeixotoClaw\projects\{PROJECT_NAME}`

2.  **Sanitização do Ambiente**:
    // turbo
    - Execute o script de inicialização para limpar inboxes e locks antigos:
      ```bash
      python .agents/skills/maestro_sandeco/scripts/maestro_init.py {PROJECT_NAME}
      ```

3.  **Carga de Contexto**:
    - Leia o `PLAN.md` e `TASKS.md` do projeto selecionado (dentro da pasta do projeto).
    - Verifique o Ledger de atividades em `projects/{PROJECT_NAME}/.antigravity/equipe/registro_atividades.json`.

## Fase 2: Design & Atribuição de Personas 🎭

1.  **Definição do Esquadrão**:
    - Assuma a persona necessária para a tarefa atual conforme o arquivo `HANDOVER.md`:
        - `@Architect`: Design e Especificações (Proibido codar).
        - `@Builder`: Implementação TDD e Código Limpo.
        - `@PM`: Gestão de Backlog e Sincronização.
        - `@Academic`: Escrita Científica Nexus V5.

2.  **Validar Atividades**:
    - Verifique se a próxima tarefa prioritária no `TASKS.md` possui pré-requisitos pendentes no `registro_atividades.json`.

## Fase 3: Orquestração Ativa 🛠️

1.  **Criação de Atividades**:
    - Quando uma nova subtarefa for iniciada, registre-a no Ledger central:
      ```bash
      python .agents/skills/maestro_sandeco/scripts/gerenciador_equipe.py criar_atividade "{TITULO}" "{RESPONSAVEL}"
      ```

2.  **Gerenciamento de Locks e Mensagens**:
    - Antes de editar arquivos críticos, verifique se há travas no diretório `.antigravity/equipe/travas/`.
    - Utilize comunicados em `aviso_geral.msg` para sincronizar mudanças que afetam outros componentes.

3.  **Notificações (Opcional)**:
    - Se o usuário habilitar, utilize a conexão Telegram para disparar avisos de status. Caso contrário, reporte o status localmente no chat.

## Fase 4: Entrega, Auditoria & Commit ✅

1.  **Ciclo de Qualidade (MANDATÓRIO)**:
    - Execute Type Check, Lint (0 warnings), Format e Tests (100% pass + 95% coverage).

2.  **Cierre da Atividade**:
    - Atualize o estado no Ledger:
      ```bash
      python .agents/skills/maestro_sandeco/scripts/gerenciador_equipe.py atualizar_estado {ID_ATIVIDADE} CONCLUIDO
      ```
    - Calcule a economia gerada (exemplo: 1000 tokens):
      ```bash
      python .agents/skills/maestro_sandeco/scripts/gerenciador_equipe.py registrar_economia {ID_ATIVIDADE} 1000
      ```

3.  **Documentação e Git**:
    - **Regra do Tempo (MANDATÓRIO)**: Todos os artefatos de documentação, planos e logs criados ou arquivados DEVEM seguir o padrão `YYYY-MM-DD-nome_do_arquivo.ext` (ex: `2026-04-01-PLAN.md`).
    - Atualize o `PLAN.md` e `TASKS.md` do projeto.
    - Gere mensagem de commit em **Inglês** seguindo Padrão Conventional Commits.
    - Adicione o link para o walkthrough da entrega se solicitado pelo usuário.

---
**Assinado**: @Maestro (Orquestrador PeixotoClaw)
**Status**: Operacional v1.0 🚀
