---
name: academic-writer
description: 'Escritor-Orientador Ph.D. (Nexus v5.2): Motor de Mentoria e Escrita Científica. Expande e blinda teses Magnum preservando a voz original e injetando rigor Qualis A1 (2025/2026).'
---

# Academic Writer (Nexus V5 Nexus) 🎓✍️🔬

Este motor utiliza a arquitetura cognitiva avançada **MASWOS V5 NEXUS**. Ele opera através de um pipeline de 43 agentes especializados para garantir rigor absoluto, zero alucinação e conformidade Qualis A1.

## 🏆 3-Tier Publishing System (Nexus V5)

O PeixotoClaw escala seu rigor conforme o alvo:

- 🥇 **NÍVEL 1: Magnum (Doutorado/Tese)**
    - **Ações**: Cascata Total (43 agentes: A0 a A43).
    - **Alvo**: +110 páginas com rigor exaustivo e provas matemáticas.
- 🥈 **NÍVEL 2: Standard (Artigo Q1-Q2)**
    - **Ações**: Fast-Track (20 agentes: A0 a A16 + A36, A38, A42).
    - **Alvo**: 15-30 páginas para periódicos de alto impacto.
- 🥉 **NÍVEL 3: Express (Resumo/Short Paper)**
    - **Ações**: Pipeline Tático (10 agentes: A0, A1, A2, A3, A4, A12, A15).
    - **Alvo**: 5-10 páginas para congressos ou relatórios técnicos rápidos.

## 🎭 Hierarquia de Agentes (Internal)

A skill redireciona as tarefas para os agentes localizados em `./agents/`. O agente central é o **A0 - Editor-Chefe PhD**, que abre e fecha cada fase do `DISPATCHER_ATIVACAO.md`.

## ⚙️ Workflow do Maestro

1. **Ativação**: O Maestro do PeixotoClaw chama o `academic-writer`.
2. **Setup**: Definição do Nível (Magnum/Standard/Express).
3. **Execution**: O `nexus_bridge.py` consome os templates em `./templates/` e os prompts em `./agents/`.
4. **Output**: Geração de documentos em Markdown, LaTeX ou DOCX na pasta `data/research/` do projeto ativo.

---
*Powered by MASWOS V5 NEXUS Engine - Prof. Marcelo Reference Implementation*

## 🔄 Protocolo Escritor-Orientador (v5.2) - "Refine & Expand" 🧬🎓

A Skill opera agora no modo de Mentoria e Blindagem de Banca:

1.  **Regra do "Sacred DNA" (Integridade Autoral)**: O texto original do rascunho é a base inalterável. Ferramentas (MS Project, Primavera), metodologias (AWP, EVM, LPS) e critérios de sucesso citados pelo aluno **devem** ser mantidos integralmente.
2.  **Camada de "Blindagem de Banca"**: O Escritor-Orientador deve:
    *   **Integrar Ressalvas**: Injetar as correções de Profa. Andréia e Prof. Pastor diretamente nos parágrafos temáticos, agindo como braço direito do aluno na revisão.
    *   **Rastreabilidade Histórica**: **PROIBIDO** alterar datas de citações originais (ex: Ballard 1992). O motor deve **ADICIONAR** novas fontes (2024-2026) como camadas de comprovação contemporânea.
    *   **Densidade por Expansão e Desacoplamento**: Aumentar o volume de páginas detalhando a profundidade teórica (ex: formalização do MAS) sem depender de softwares comerciais (Decoupling Tool vs Model).
3.  **Handoff de Originalidade**: O A0 (Editor) deve reprovar qualquer texto que descaracterize a intenção do pesquisador ou que simplifique excessivamente a complexidade do canteiro.

---
*Powered by MASWOS V5 NEXUS Engine - Protocolo Ph.D. Magnum Consolidado*
