---
description: Criação Automática de Projeto (Dossiê PeixotoClaw) 🚀
---

Este workflow é disparado automaticamente quando o usuário diz: `"Vamos iniciar o projeto XXX"`.

> [!CAUTION]
> - Não é necessária confirmação para a criação em `d:\OneDrive\aiproj\PeixotoClaw\projects\`.
> - O idioma padrão de todos os documentos gerados é **Português**.

## 🚀 Protocolo de Criação (Reactive)

1.  **Extração de Nome**:
    - Identifique o nome do novo projeto (ex: `SafeAssessment`).

2.  **Criação Automática**:
    // turbo
    - Execute o comando de criação para gerar a estrutura:
      ```bash
      python d:\OneDrive\aiproj\PeixotoClaw\scripts\project_lifecycle.py create {PROJECT_NAME} "{USUARIO_DESCREVE_OBJETIVO_AO_ANUNCIAR}"
      ```

3.  **Sanitização Maestro**:
    - O comando de criação já chama a sanitização e cria os arquivos `PLAN.md` (3 cenários) e `TASKS.md`.

4.  **Carga de Contexto Imediata**:
    - Leia a estrutura recém-criada e informe ao usuário:
      *"Dossiê {PROJECT_NAME} criado e inicializado em projects/. Já configurei os cenários de Planejamento e as primeiras Tarefas. Qual o primeiro passo técnico?"*

5.  **Persistência de Artefatos**:
    - Qualquer artefato gerado DEVE ser espelhado no Dossiê:
      ```bash
      python d:\OneDrive\aiproj\PeixotoClaw\scripts\project_lifecycle.py persist {PROJECT_NAME} {ARTIFACT_PATH}
      ```

---
**Status**: Projeto Novo Online e Estruturado.
