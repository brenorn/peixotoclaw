# Spec-Driven Development (SDD): O Guia Definitivo e Exaustivo

Este documento é o resultado de uma análise profunda e detalhada de duas referências seminais: o artigo de Martin Fowler (Birgitta Böckeler) e a implementação prática de Marcos (Medium) utilizando Codex. O objetivo é fornecer não apenas um resumo, mas um **manual de referência técnica** completo.

---

## 1. Fundamentos e Definições Profundas

O SDD não é apenas "escrever docs antes". É uma mudança na **lingua franca** do desenvolvimento, onde a especificação estruturada em linguagem natural torna-se o artefato primário e o código torna-se o "last-mile approach" (a etapa final de tradução).

### 1.1. O que define uma "Spec"?
Diferente de um PRD (Product Requirements Document) tradicional, uma Spec no SDD deve ser:
- **Estruturada**: Segue formatos como Markdown/YAML/JSON.
- **Orientada a Comportamento**: Foca no *quê*, não no *como* técnico inicial.
- **Testável**: Contém Critérios de Aceitação (AC) claros (Gherkin/GIVEN-WHEN-THEN).
- **Consumível por IA**: Escrita para ser o prompt mestre de um agente.

### 1.2. Níveis de Abstração (Taxonomia de Fowler)

O estudo identifica três níveis críticos que determinam o controle humano sobre o código:

1.  **Spec-first (Nível 1)**:
    - **Criação**: Spec guia a IA na primeira geração.
    - **Manutenção**: A spec é descartada. Mudanças futuras ocorrem direto no código.
    - **Risco**: Perda rápida da "fonte de verdade".

2.  **Spec-anchored (Nível 2)**:
    - **Criação**: Spec nasce com o código.
    - **Manutenção**: Toda mudança de feature **precisa** de um commit na Spec antes do commit no código.
    - **Vantagem**: Documentação e código estão sempre sincronizados.

3.  **Spec-as-source (Nível 3)**:
    - **Criação**: Definida apenas na Spec.
    - **Manutenção**: O humano nunca edita código (`// DO NOT EDIT`).
    - **Desafio**: Exige agentes de altíssima fidelidade e determinismo.

---

## 2. Ferramentas e Topologias de Arquivos

O estudo das ferramentas Kiro, Spec-kit e Tessl revela padrões de organização de arquivos:

### 2.1. O "Memory Bank" (Consciência do Projeto)
As ferramentas SDD utilizam arquivos de "Long Term Memory" para dar contexto à IA:
- **Constitution.md (Spec-kit)**: Princípios imutáveis, regras arquiteturais severas (ex: "Nunca use lógica de negócio em Controllers").
- **Product.md / Tech.md (Kiro)**: Define o stack e o ecossistema.
- **ActiveContext.md**: O estado atual do trabalho, evitando que a IA se perca em conversas longas.

### 2.2. Fluxo de Trabalho (Workflows)

| Fase | Ação Humana | Ação da IA |
| :--- | :--- | :--- |
| **Requirements** | Escreve User Stories + AC. | Valida ambiguidade e propõe refinamentos. |
| **Design** | Revisa o plano arquitetural. | Sugere Data Models, Endpoints e Error Handling. |
| **Tasks** | Aprova o checklist. | Quebra a implementação em micro-commits/tasks. |
| **Implementation**| Revisa o PR. | Gera código, testes e relatórios de cobertura. |

---

## 3. Implementação Prática: O Modelo Multi-Agente (Codex)

Baseado no estudo de Marcos, o SDD atinge maturidade com a separação de papéis em um arquivo `AGENTS.md`.

### 3.1. Evolução do `AGENTS.md`
O estudo mostra que um `AGENTS.md` robusto evolui de simples regras para definições de stack e cobertura:
- **V1**: Regras básicas ("leia as specs primeiro").
- **V2**: Definição de Stack (Java 17+, Spring, JaCoCo 90%).
- **V3**: Definição de Personas (Architect, Engineer, Reviewer).

### 3.2. As Personas do Fluxo "Thinking -> Doing"

#### **A. Spec Architect (The Thinker)**
- **Meta**: Rigor técnico no Markdown.
- **Saída**: Arquivos em `/specs` com Objetivo, Regras de Negócio e Casos de Erro.
- **Ponto de Honra**: Não escreve uma linha de código.

#### **B. Software Engineer (The Doer)**
- **Meta**: Implementação fiel e minimalista.
- **Lógica de Código (Exemplo Documento Record)**: O estudo visual de código mostra que o Engenheiro deve focar em **Domain-Driven Design**. A lógica de validação de CPF/CNPJ deve estar encapsulada no próprio domínio, disparando exceções claras se a Spec for violada.

#### **C. Review Agent (The Auditor)**
- **Meta**: Detectar "Gaps" e "Funcionalidades não solicitadas".
- **Relatório de Revisão**: Deve apontar explicitamente qual Critério de Aceitação da Spec não foi testado no código.

---

## 4. Críticas, Riscos e Antecedentes Históricos

Martin Fowler traz uma perspectiva vital de cautela:

### 4.1. Paralelo com MDD (Model-Driven Development)
Nos anos 2000, o MDD tentou fazer algo similar com UML e transformações de modelo. Por que falhou e por que agora pode ser diferente?
- **Falha do MDD**: Rigidez excessiva e complexidade de geradores de código.
- **Oportunidade da IA**: A linguagem natural (Markdown) resolve a rigidez, mas introduz o **Não-Determinismo**.

### 4.2. As Armadilhas do SDD
- **Sledgehammer to crack a nut**: Usar SDD completo (com multi-agentes e specs gigantes) para corrigir um bug de uma linha em um arquivo CSS.
- **False Sense of Control**: Achar que porque a Spec existe, a IA a seguirá 100%. A IA pode "alucinar" conformidade.
- **Review Overload**: Trocar o review de 100 linhas de código por 500 linhas de Markdown repetitivo é uma perda de eficiência.

---

## 5. Blueprint de Implementação no PeixotoClaw

Como aplicar este estudo imediatamente neste projeto:

1.  **Diretório `/specs`**: Criar este diretório para armazenar as intenções das novas features.
2.  **`AGENTS.md` Global**: Estabelecer a "Constituição" do PeixotoClaw (ex: "Sempre usar AgentController para novas skills").
3.  **Relatório de Cobertura**: Exigir que o agente gere um `summary_test_coverage.md` que mapeie testes para critérios de aceite específicos da spec.
4.  **Loop de Feedback**: Se a implementação falhar, a correção **deve** ocorrer na Spec primeiro, e o agente deve regenerar a tarefa.

---
**Justificativa de Profundidade**: Este relatório integra a teoria de arquitetos de software de renome mundial com a experiência de campo de engenheiros de IA, cobrindo da taxonomia dos níveis de maturidade até os riscos de verbosidade e alucinação técnica.
