import sys
import re
from pathlib import Path

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Mapeamento de traduções para garantir qualidade técnica e contextos do projeto
TRANSLATIONS = {
    "algorithmic-art": "Criação de arte algorítmica usando p5.js, flow fields e sistemas de partículas com sementes de aleatoriedade.",
    "architecture-blueprint-generator": "Gerador de blueprints arquiteturais detalhados. Analisa o código e gera diagramas e padrões de implementação.",
    "autoresearch-diagrams": "Otimização auto-melhorável de diagramas usando o padrão Karpathy. Gera, avalia e refina prompts de diagramas Mermaid.",
    "brainstorming": "Parceiro para exploração de ideias, definição de escopo e decisões arquiteturais de alto nível.",
    "brand-guidelines": "Aplica cores e tipografias oficiais da Anthropic (ou marca definida) em qualquer artefato visual do projeto.",
    "canvas-design": "Criação de artes visuais premium (PNG/PDF) seguindo filosofias modernas de design para posters e documentos estáticos.",
    "capes-power-research": "Ferramenta avançada de busca e download no portal de Periódicos CAPES com suporte a filtros Q1/Q2 e login CAFe.",
    "claude-api": "Assistente especializado em construir aplicações usando o SDK da Anthropic ou Claude API.",
    "docx": "Criação, leitura e manipulação profissional de documentos Word (.docx) com formatação complexa e letterheads.",
    "editor-video": "Edição automática de vídeo via análise de SRT, removendo erros de fala e silêncios de forma inteligente.",
    "frontend-design": "Criação de interfaces web de alto padrão (React/Tailwind) que evitam a estética genérica de IA.",
    "internal-comms": "Criação de comunicações internas corporativas (status reports, newsletters, incidentes) seguindo padrões da empresa.",
    "mcp-builder": "Guia para criação de servidores MCP (Model Context Protocol) de alta qualidade em Python ou Node.",
    "pdf": "Manipulação completa de arquivos PDF: extração de texto, tabelas, OCR, mesclagem e preenchimento de formulários.",
    "pptx": "Criação e edição profissional de apresentações e decks de slides (.pptx) com foco em design e fluxo narrativo.",
    "slack-gif-creator": "Criação de GIFs animados otimizados para o Slack seguindo restrições de tamanho e performance.",
    "theme-factory": "Toolkit para estilização de artefatos com temas visuais coordenados (slides, docs, landing pages).",
    "web-artifacts-builder": "Criação de artefatos HTML/JSX complexos com React, Tailwind e shadcn/ui para dashboards e apps interativos.",
    "webapp-testing": "Toolkit para testes automatizados de aplicações web locais usando Playwright e captura de logs/screenshots.",
    "xlsx": "Manipulação avançada de planilhas (.xlsx, .csv, .tsv): limpeza de dados, fórmulas complexas e geração de gráficos.",
    "youtube-creative": "Suite completa para YouTube: pesquisa estratégica, roteirização, ganchos magnéticos, tags SEO e descrições otimizadas.",
    "reversa_frontend": "Engenharia Reversa de Frontends: Mapeamento de fluxos de usuário e descoberta de lógicas de cálculo complexas."
}

def translate_skill_files():
    skills_dir = Path(r"d:\OneDrive\aiproj\PeixotoClaw\.agents\skills")
    
    for skill_md in skills_dir.rglob("SKILL.md"):
        content = skill_md.read_text(encoding="utf-8")
        
        # Encontrar a descrição no YAML
        match = re.search(r"description:\s*(.*?)\n", content)
        if match:
            current_desc = match.group(1).strip().strip('"').strip("'")
            skill_name = ""
            
            # Tentar pegar o nome do YAML
            name_match = re.search(r"name:\s*(.*?)\n", content)
            if name_match:
                skill_name = name_match.group(1).strip()

            # Se temos uma tradução mapeada ou se a descrição parece inglês
            # (Heurística simples: se contiver palavras comuns de inglês e não comuns de PT)
            needs_translation = False
            if skill_name in TRANSLATIONS:
                new_desc = TRANSLATIONS[skill_name]
                needs_translation = True
            elif any(word in current_desc.lower() for word in ["creating", "build", "guide", "whenever", "use this"]):
                # Aqui poderíamos usar uma API de tradução, mas usaremos uma tradução genérica para os principais
                # e manteremos o código aberto para o Antigravity fazer as específicas.
                needs_translation = False # Evitar tradução automática genérica ruim

            if needs_translation:
                print(f"Traduzindo: {skill_name} -> {new_desc}")
                # Substituir no arquivo
                new_content = content.replace(match.group(0), f"description: {new_desc}\n")
                skill_md.write_text(new_content, encoding="utf-8")

if __name__ == "__main__":
    translate_skill_files()
