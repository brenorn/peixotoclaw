---
name: academic-writer
description: 'Expert writing skill for high-impact journals (Q1). Use this to write, structure, or review scientific papers for Automation in Construction, CACEIE, ASCE J. of Computing, and Adv. Eng. Informatics. Strictly follows templates, performs RAG for evidence, and prevents hallucinations.'
---

# Academic Writer (Q1 Standard) 🎓✍️🔬

Esta habilidade transforma dados brutos e resultados de pesquisa em manuscritos de nível Q1, seguindo o rigor acadêmico e as normas específicas de cada revista.

## Princípios Fundamentais (PEIXOTO Rigor)
1. **Zero Hallucination**: Nunca invente dados. Se algo não estiver nos resultados fornecidos ou nos artigos recuperados (RAG), use placeholders ou peça ao usuário os dados reais.
2. **Template Fidelity**: Sempre leia e siga a estrutura, normas de citação e limites de palavras da revista alvo.
3. **Knowledge Primacy**: Em informática e engenharia civil, o foco é na representação do conhecimento e na escalabilidade dos métodos, não apenas no código ou na matemática.
4. **XAI Integration**: Sempre inclua a justificativa científica (Rationale) para as conclusões apresentadas.

## Arquitetura Interna (Padrão Sandeco) 🤖📚
A skill utiliza uma arquitetura de **Agentic RAG** para garantir precisão Q1 e evitar alucinações:
1.  **Memory Hub (`scripts/memory.py`)**: Mantém o contexto da tese e interações passadas para garantir coerência entre os capítulos.
2.  **Dataset Router (`scripts/agentic_academic_rag.py`)**: Um agente especialista em roteamento que decide qual base (Normas, IA, Resultados ou Estilo) consultar.
3.  **Knowledge Base (`scripts/datasets.py`)**: Catálogo estruturado de fontes de dados acadêmicas.

## Fluxo de Trabalho Acadêmico

### 1. Iniciação e Memória
Ao começar um novo artigo, a skill inicializa a `AcademicSessionMemory`.
- **Comando**: `python scripts/memory.py` para verificar o estado da sessão.

### 2. Pesquisa e RAG (Agentic)
Sempre que precisar embasar uma afirmação ou citar uma norma:
- **Ação**: A skill aciona o `scripts/agentic_academic_rag.py`.
- **Roteamento**: O sistema decide se consulta a `construction_norms` ou `ai_frameworks`.
- **Extração**: Retorna evidências concretas para o manuscrito.

### 3. Escrita com Templates
A skill deve ler o arquivo de template (`.docx` ou `.pdf`) fornecido pelo usuário antes de iniciar a escrita.
- **Estruturação**: Mapeia os estilos de cabeçalho, bibliografia e seções obrigatórias.

### 3. Escrita Estruturada
- **Abstract & Keywords**: Foco em impacto e contribuição original.
- **Introduction**: O "Funil Científico" (Contexto -> Problema -> Gap -> Objetivo).
- **Methodology**: Descrição detalhada do MAS (Multi-Agent System) e frameworks testados.
- **Results & Discussion**: Comparação objetiva PydanticAI vs Native vs LangGraph.
- **Practical Applications**: (Obrigatório para ASCE) Como a indústria pode usar isso hoje.

## Regras por Revista

### Automation in Construction (AiC)
- **Foco**: Tecnologia da informação no ciclo de vida da construção.
- **Exigência**: Reprodutibilidade e fluxos BIM.

### Computer-Aided Civil and Infrastructure Engineering (CACEIE)
- **Foco**: Algoritmos computacionais avançados (ex: IA poderosa).
- **Exigência**: Alta inovação matemática/algorítmica.

### Journal of Computing in Civil Engineering (ASCE)
- **Formatação**: Máximo 30 páginas, espaçamento duplo.
- **Estilo**: Sem numeração de seções. Referências ASCE.

### Advanced Engineering Informatics (AEI)
- **Foco**: Ciência da representação do conhecimento.
- **Exigência**: Demonstrar generabilidade e poder do método.

## Ferramentas de Apoio
- Se precisar verificar citações, use: `python scripts/rag_researcher.py --query "[TERMO]"`

---
"Rigor não é chatice, é a garantia de que o conhecimento será útil."
