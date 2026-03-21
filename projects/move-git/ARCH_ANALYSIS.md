# Análise Arquitetural: Módulo Competências (Move-Git) 🧬

Após o scan inicial, identifiquei a estrutura do "Estado da Arte" do módulo.

## 🛠️ Componentes Identificados
- **Core Logic**: `llm_producao/chapters/chap_competencias.py`
    - Sistema baseado em **LangChain** e `StrOutputParser`.
    - Utiliza o padrão `ChapterHandler` assíncrono.
    - Suporte nativo para **Guardrails** e **PromptEngine**.
- **Prompt Engine**: `llm_producao/prompt_competencia.py`
    - Framework psicológico profundo baseado em **CNV** (Comunicação Não-Violenta).
    - Lógica de "Refreaming Radical" para scores baixos (< 30).
    - Matriz de estilos baseada no perfil **MOVE** (Motor, Observador, Visionário, Executor).
- **Visualização**: `js/charts/competency-radar.js` (Radar de competências para o dashboard).

## 🧩 Padrão de Design: "Chapter Pattern"
O Move-Git utiliza um padrão onde cada seção do relatório é um "Chapter" (Capítulo) isolado em Python. Isso permite uma **Manutenção Cirúrgica**: podemos atuar no `chap_competencias.py` sem risco de quebrar o Capítulo de PDI ou de Liderança.

## 🧐 Conclusões do @Architect
1.  **Estado da Arte**: O código está bem modularizado, mas a lógica de "Reframing" de competências é estática (templates de strings).
2.  **Oportunidade "Monster"**: O `@Builder` pode transformar esses templates em uma estrutura de dados JSON dinâmica, facilitando a internacionalização e a customização por cliente.
3.  **Segurança**: Os Guardrails são chamados opcionalmente; recomenda-se torná-los mandatórios.

---
*Relatório Consolidado pelo @Architect*

---
*Relatório em construção pelo @Architect*
