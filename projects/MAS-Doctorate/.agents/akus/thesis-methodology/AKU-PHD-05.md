# AKU-PHD-05: Ciclo de Aprendizado e Recompensa (MARL)

Este conhecimento governa como os agentes aprendem com as consequências de suas decisões.

## 🎯 Objetivo
Transformar o MAS de um executor de regras passivo em um sistema que otimiza sua própria política de decisão.

## 🔄 O Loop de Feedback
1. **Ação (Action)**: O agente executa uma tarefa ou propõe um ajuste no cronograma.
2. **Observação (Observation)**: O sistema observa o novo estado do cronograma (MS Project/Dashboard).
3. **Recompensa (Reward)**:
   - **Positiva (+1)**: Redução de folga negativa, aumento do PPC, remoção de restrições antes do prazo.
   - **Negativa (-1)**: Aumento do caminho crítico, atraso na entrega, conflito de recursos.

## 🧠 Evolução da Política
- Decisões com recompensa negativa devem ser enviadas ao `skill-evolver`.
- O `skill-evolver` deve gerar um **Aviso de Lição Aprendida** (Lesson Learned) que será injetado no contexto das próximas decisões similares.

## 📚 Referências (Seminário Peixoto)
- MARL (Multiagent Reinforcement Learning), Liang et al. (2025), Jain et al. (2024).
