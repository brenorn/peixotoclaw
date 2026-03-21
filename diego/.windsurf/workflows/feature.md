## name: feature

Adote a persona definida em `@builder.md` (leia este arquivo de regra agora).

description: Implementa tarefas do TASKS.md (Código + Testes)
model: Claude 3.7 Sonnet

# Workflow de Desenvolvimento

1. **Seleção de Tarefa**
   * Leia o `TASKS.md` e identifique a próxima tarefa pendente `[ ]`.
   * Leia as regras de **@builder.md** para manter o padrão de código.
   * Confirme com o usuário: "Vou implementar. Confirma?"
2. **Implementação (TDD)**
   * Crie/Atualize os arquivos necessários.
   * Siga estritamente o que foi desenhado no plano.
   * **Regra de Ouro:** Crie ou atualize um teste unitário para validar essa mudança específica.
3. **Validação**
   * Rode os testes.
   * Se passar: Marque a tarefa como `[x]` no `TASKS.md`.
