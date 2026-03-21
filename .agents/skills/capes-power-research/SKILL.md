---
name: capes-power-research
description: 'Advanced search and download tool for the CAPES Periodicals portal. Supports deep filtering (Q1/Q2, Last 5 Years, Open Access) and automated CAFe login. Integrated with academic-writer for RAG-ready scientific evidence.'
---

# CAPES Power Research 📚🔍☕

Esta skill transforma o Portal de Periódicos CAPES em um motor de busca automatizado e inteligente para sua tese ou artigos científicos.

## 🚀 Funcionalidades Principais

1.  **Filtros Inteligentes (NLP)**: Digite um parágrafo sobre seu tema e o sistema extrai automaticamente as keywords e aplica filtros de:
    -   Recência (últimos 5 anos).
    -   Qualidade (Q1/Q2 via busca de editoras de elite).
    -   Peer-Reviewed & Open Access.
2.  **Busca Multi-Campo Avançada**: Suporte a lógica complexa (Topic, Title, Author) com operadores E, OU, NÃO.
3.  **Acesso Direto à Bases (Scopus/WoS)**: Se você pedir por uma base específica, o sistema faz o login institucional e abre o editor externo para você.
4.  **Login CAFe Automático**: Usa suas credenciais UnB do `.env` para garantir acesso a conteúdos pagos.
5.  **Seleção por Resumo**: O sistema apresenta os abstracts em Markdown; você marca o que quer e o download é feito em background.

## 🛠️ Como Usar

### Gatilho de Busca
"Quero artigos sobre 'Multi-Agent Systems na construção civil' dos últimos 5 anos, apenas Q1 e com acesso aberto."

### Fluxo de Trabalho
1.  **Maestro Process**: O `sandeco-maestro` coordena a extração de termos.
2.  **Deep Search**: O sistema navega até o buscador avançado da CAPES.
3.  **Curadoria**: Você recebe uma lista no chat:
    - [ ] Artigo A - Resumo...
    - [x] Artigo B - Resumo...
4.  **Download**: Após sua marcação, o PDF é baixado para `academic-writer/base_k/`.

## 📂 Estrutura da Skill
- `scripts/capes_orchestrator.py`: Lógica central de coordenação.
- `scripts/capes_filters.py`: Extração de filtros via Gemini.
- `scripts/capes_browser.py`: Automação Playwright para login e busca.

---
"Pesquisa de alto nível exige ferramentas de alto nível."
