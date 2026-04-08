## name: status

Adote a persona definida em `@pm.md` (leia este arquivo de regra agora).

description: Atualiza o status do projeto e organiza o backlog
model: Claude 3.7 Sonnet

# Check-in de Gerenciamento

1. **Auditoria**
   * Leia `CURRENT_CONTEXT.md` e `TASKS.md`.
   * Analise os arquivos modificados recentemente (git status).
   * Ative a persona  **@pm.md** 
2. **Sincronização**
   * Verifique se o que foi codado bate com as tarefas marcadas.
   * Se houver discrepância (código feito mas tarefa desmarcada), corrija o `TASKS.md`.
3. **Relatório**
   * Gere um resumo curto: "Hoje completamos X e Y. O próximo passo lógico é Z."
   * Atualize o `CURRENT_CONTEXT.md` com este resumo.
