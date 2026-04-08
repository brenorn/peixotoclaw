---
description: Ativação Automática de Projeto (Dossiê PeixotoClaw) 📡
---

Este workflow é disparado automaticamente quando o usuário diz: `"Vamos trabalhar com o projeto XXX"`.

> [!IMPORTANT]
> - O agente DEVE extrair o nome do projeto (XXX).
> - O agente DEVE carregar o contexto do `PLAN.md` e `TASKS.md` local para garantir continuidade.

## 📡 Protocolo de Ativação (Reactive)

1.  **Extração de Identidade**:
    - Identifique o nome do projeto (ex: `MAS-Doctorate`).

2.  **Sanitização e Carga Invisível**:
    // turbo
    - Execute o comando de ativação para preparar o ambiente:
      ```bash
      python d:\OneDrive\aiproj\PeixotoClaw\scripts\project_lifecycle.py activate {PROJECT_NAME}
      ```

3.  **Sincronização de Estado**:
    - Informe ao usuário o status atual do `PLAN.md` (Objetivo) e a próxima tarefa do `TASKS.md`.
    - Ative as Personas correspondentes (@Architect, @Builder, etc.) conforme necessário para a tarefa pendente.

4.  **Persistência Reativa**:
    - A partir deste momento, todo artefato gerado DEVE ser espelhado no Dossiê:
      ```bash
      python d:\OneDrive\aiproj\PeixotoClaw\scripts\project_lifecycle.py persist {PROJECT_NAME} {ARTIFACT_PATH}
      ```

---
**Status**: Pronto para Ocupação Operacional.
