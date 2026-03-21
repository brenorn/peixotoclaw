# Spec-Driven Development (SDD): O Guia Definitivo e Exaustivo (Master)

Este documento consolidado é o resultado do "Deep Learning" sobre o paradigma SDD, cruzando as visões de Martin Fowler, arquiteturas reais de mercado (Codex/Medium) e o ecossistema HiveHub.

---

## 1. Fundamentos e Taxonomia (Visão Martin Fowler)

O SDD propõe que a **especificação estruturada** é o artefato primário do desenvolvimento, movendo a "língua franca" da engenharia para o Markdown/YAML.

### 1.1. Níveis de Maturidade
1.  **L1 - Spec-first**: A spec guia a criação inicial, mas é abandonada. Risco: Dívida técnica e obsolescência da documentação.
2.  **L2 - Spec-anchored**: Toda mudança no código exige um commit anterior na Spec. Mantém a síncrona eterna entre intenção e código.
3.  **L3 - Spec-as-source**: O humano nunca edita código. O código é gerado (ex: Tessl) e marcado como `// GENERATED`.

### 1.2. O Problema da "Vibe Coding"
A codificação baseada apenas em prompts soltos gera código inconsistente e arquiteturas frágeis. O SDD resolve isso ao introduzir **âncoras de contexto**.

---

## 2. Orquestração Multi-Agente (Modelo Codex/Marcos)

A implementação prática utiliza a divisão de responsabilidades para evitar que o agente se perca.

### 2.1. O Ciclo "Thinking -> Doing -> Review"
- **Spec Architect (Thinking)**: Foca em regras de negócio e critérios de aceitação. Proibido escrever código.
- **Software Engineer (Doing)**: Implementa o código baseado na Spec e gera `tasks.md`.
- **Review Agent (Reviewing)**: Audita se o Engenheiro seguiu a Spec ou se houve "alucinação de requisitos".

### 2.2. O Memory Bank (`AGENTS.md`)
O arquivo `AGENTS.md` atua como a constituição do projeto, definindo:
- **Stack Tecnológica**: Versões de linguagens e ferramentas.
- **Regras de Engajamento**: Fluxos obrigatórios (ex: "Sempre ler /specs antes de codar").
- **Métricas de Qualidade**: Ex: Cobertura de testes unitários mínima de 90%.

---

## 3. Ferramentas de Ecossistema

- **Kiro/Spec-kit**: Focam na topologia de arquivos de "contexto ativo" vs "contexto legado".
- **LessTokens**: Essencial para SDD em larga escala. Utiliza compressão semântica e *Smart Anchoring* para manter o custo baixo e a precisão alta em specs extensas.
- **@hivehub/rulebook**: Garante que as especificações sejam síncronas entre diferentes ferramentas de IA (Cursor, Claude, Gemini).

---

## 4. Críticas e Antecedentes
- **MDD (Model-Driven Development)**: O SDD é a evolução natural do MDD, mas usando linguagem natural em vez de UML rígida.
- **Verschlimmbesserung**: O risco de burocratizar demais o fluxo e gastar mais tempo revisando Markdown do que código.

---
**Conclusão**: O SDD transforma o desenvolvedor de um "escritor de funções" em um "comandante de generais IA". A chave do sucesso é a disciplina na manutenção da Spec como única fonte de verdade.
