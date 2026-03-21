# AKU-PHD-03: LLM-MA & Perfilamento de Agentes

Define a estrutura cognitiva e a persona dos agentes baseados em IA.

## 🎯 Objetivo
Padronizar a criação de novos agentes no MAS-Doctorate para garantir que ajam como especialistas.

## 👤 Perfilamento (Agent Profiling)
Todo agente deve ser definido por:
1. **Role (Papel)**: Ex: "Analista de Riscos de Prazo".
2. **Goal (Objetivo)**: Ex: "Garantir que o caminho crítico não sofra desvios".
3. **Backstory (Contexto)**: Sua experiência prévia e viés comportamental (ex: "Cauteloso", "Proativo").
4. **Tools (Ferramentas)**: APIs de busca (CRAG), Leitura de XML, Cálculo de PPC.

## 🧠 Motor de Raciocínio (LLM + MARL)
- **LLM**: Responsável pelo raciocínio semântico, interpretação de atas e e-mails.
- **MARL (Aprendizado por Reforço Multiagente)**: Responsável pelas decisões de alocação de recursos em cenários competitivos/cooperativos.
- **Sinergia**: O LLM planeja o texto, o MARL otimiza o número.

## 📚 Referências (Seminário Peixoto)
- Guo et al. (2024), Macedo (2024), Kalyuzhnaya et al. (2025).
