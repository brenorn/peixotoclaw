---
name: quality-assurance
description: 'Executa auditorias de qualidade, testes automatizados (unitários/integração) e garante o fechamento do ciclo PDCA/DMAIC. Use para validar funcionalidade e estabilidade.'
---

# Skill: Quality Assurance (QA) 🦞🧪

Esta habilidade foca na **Validação** e no **Controle** de qualidade do sistema, complementando a Governança de Dados. Enquanto a Governança define as leis (nomes), o QA garante que o motor funciona como o esperado.

## Ciclo de Controle (PDCA / DMAIC)

### 1. Check (PDCA) / Control (DMAIC)
Toda implementação deve passar por uma bateria de testes antes de ser considerada "concluída".
- **Teste Unitário**: Use `pytest` para lógica de backend.
- **Teste de UI**: Use `playwright` ou scripts de verificação manual para componentes React.
- **Linting**: Garanta que o código passa no `eslint` e `black/flake8`.

## Critérios de Aceitação (DoD - Definition of Done)

Para que uma tarefa seja movida para `[x]` no `TASKS.md`, o QA deve verificar:
1. **Funcionalidade**: O código faz o que foi pedido sem quebrar partes existentes?
2. **Nomenclatura**: Os logs e mensagens de erro são profissionais e úteis?
3. **Desempenho**: Há alguma query N+1 ou loop infinito óbvio?
4. **Resiliência**: Como o código lida com falhas (ex: banco offline)?

## Ferramentas de Auditoria
- `npm run lint` (Para o Dashboard).
- `pytest` (Para o Backend).
- `skill-auditor` (Para revisar a segurança das novas habilidades).

## Protocolo de Resposta
Ao encontrar um bug, o QA não deve apenas "reportar". Ele deve:
1. Criar um caso de teste que reproduza o erro.
2. Identificar se o erro é de **Nomenclatura** (chamar a Governança) ou de **Lógica** (chamar o Builder).
3. Validar a correção após o refactoring.

---
"Se não foi testado, está quebrado."
