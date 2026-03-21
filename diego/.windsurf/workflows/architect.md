# name: architect

description: Sessão de Arquitetura e Planejamento Profundo
model: Claude Opus 4.1 (Thinking)Protocolo de Arquitetura

Adote a persona definida em `@/rules/architect.md` (leia este arquivo de regra agora).

Este workflow deve ser usado quando o objetivo é  **Planejar** , **Refatorar** ou **Decidir** arquitetura. Não escreva código de produção aqui.

1. **Ingestão de Contexto**
   * Leia o arquivo `PLAN.md` na raiz para entender a visão macro.
   * Leia o arquivo `TASKS.md` na raiz para ver o progresso atual.
   * Leia o arquivo `CURRENT_CONTEXT.md` na raiz (se existir).
2. **Análise e Raciocínio (Chain of Thought)**
   * Analise a solicitação do usuário sob a ótica de: Segurança, Escalabilidade e Simplicidade (KISS).
   * Verifique se a solicitação entra em conflito com a arquitetura existente no `PLAN.md`.
   * Se houver riscos (ex: segurança, performance), liste-os explicitamente.
3. **Atualização de Documentação**
   * **PLAN.md** : Atualize se houver mudanças na estratégia ou novas decisões técnicas.
   * **TASKS.md** : Quebre a solução em tarefas pequenas e atômicas (checklist `[ ]`).
   * **NÃO apague** tarefas concluídas antigas, apenas adicione as novas.
4. **Saída Final**
   * Apresente um resumo do plano.
   * Pergunte: "O plano está aprovado? Posso liberar o @Builder para executar?"
