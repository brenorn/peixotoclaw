# 🧬 FAILURE_LOG: EvoSkill Discovery Engine

Este log é o combustível para a evolução do PeixotoClaw. Toda vez que um agente (ou o usuário) identificar uma falha repetitiva, lacuna de conhecimento ou erro de execução, ele deve ser registrado aqui.

## 🚨 Falhas Recentes (Queue for Evolution)
| ID | Timestamp | Contexto (Projeto/Skill) | Descrição da Falha | Causa Raiz (Hipótese) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FL-000 | 2026-03-17 | MAS-Doctorate | Exemplo: Erro de importação no FastAPI. | Versão da lib mudou no ambiente local. | `[PENDENTE]` |
| FL-001 | 2026-03-17 | MAS-Doctorate | Agente permitiu desforma de laje com 3 dias, violando a NBR 12721. | AKU-BC-01 não foi específica o suficiente sobre lajes estruturais. | `[RESOLVIDO]` |

---

## 🛠️ Instruções para Agentes (EvoSkill Protocol)
1. **Detectar**: Se uma tarefa falhar >2 vezes ou exigir intervenção manual do usuário para corrigir nomes/logica básica.
2. **Registrar**: Adicione uma linha na tabela acima.
3. **Evoluir**: Chame a skill `[skill:skill-evolver]` passando o ID da falha.

---

## 📈 Histórico de Evolução (Pareto Frontier)
| ID Falha | Skill Gerada/Editada | Melhoria Medida (%) | Data |
| :--- | :--- | :--- | :--- |
| FL-001 | AKU-BC-01 (Patch) | 100% de Compliance NBR | 2026-03-17 |

---
"O erro é o primeiro passo da maestria."
