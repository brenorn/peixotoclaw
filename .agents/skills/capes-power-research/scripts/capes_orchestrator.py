import os
import asyncio
import json
import sys
from dotenv import load_dotenv
from capes_filters import FilterExtractor, CapesFilters
from capes_multi_field import CapesMultiFieldBrowser
from capes_specialized import CapesSpecialized

load_dotenv()

def generate_bibtex(results):
    """Gera uma string no formato BibTeX a partir dos resultados."""
    bib_content = ""
    for i, res in enumerate(results):
        cite_key = f"{res.get('id', 'CAPES_00')}_{res['title'][:10].replace(' ', '')}"
        bib_content += f"@article{{{cite_key},\n"
        bib_content += f"  title = {{{res['title']}}},\n"
        bib_content += f"  author = {{{res.get('author', 'Unknown')}}},\n"
        bib_content += f"  url = {{{res.get('url', '')}}},\n"
        bib_content += f"  year = {{2024}},\n"
        bib_content += f"  note = {{Source: {res.get('source', 'CAPES Portal')}}}\n"
        bib_content += "}\n\n"
    return bib_content

async def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python capes_orchestrator.py \"Busca temática\"")
        return

    user_input = sys.argv[1]
    
    # 1. Extrair Intenção e Filtros
    print("🤖 Analisando seu pedido...")
    extractor = FilterExtractor()
    filters: CapesFilters = extractor.extract(user_input)
    
    # 2. Roteamento: Base Específica vs Busca Geral
    known_bases = {
        "scopus": "Scopus",
        "science": "Web of Science - Coleção Principal (Clarivate)",
        "web of science": "Web of Science - Coleção Principal (Clarivate)"
    }
    
    target_base = None
    for key, val in known_bases.items():
        if key in user_input.lower():
            target_base = val
            break

    results = []
    if target_base:
        print(f"🔗 Usando busca especializada para: {target_base}")
        # Simplificar query para a base nativa (apenas o termo principal)
        query = filters.search_rows[0].term if filters.search_rows else user_input
        spec_browser = CapesSpecialized()
        results = await spec_browser.run_specialized_search(target_base, query)
    else:
        # 3. Busca Multi-Campo (Portal CAPES)
        print(f"🎯 Filtros Extraídos para Busca Avançada:")
        print(json.dumps(filters.model_dump(), indent=2, ensure_ascii=False))
        browser = CapesMultiFieldBrowser()
        results = await browser.run_advanced(filters)
    
    if not results:
        print("\n⚠️ Nenhum resultado encontrado.")
        return

# Adiciona o diretório do maestro para pegar o path_utils
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "maestro_sandeco", "scripts")
sys.path.append(SCRIPTS_DIR)
import path_utils

    # 4. Salvar Resultados para Integração (Satélite MAS-Doctorate)
    project_id = os.getenv("PEIXOTOCLAW_PROJECT", "MAS-Doctorate")
    output_dir = path_utils.resolve_path(os.path.join("projects", project_id, "data", "research"))
    os.makedirs(output_dir, exist_ok=True)
    
    output_json = os.path.join(output_dir, "results.json")
    output_bib = os.path.join(output_dir, "results.bib")
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    with open(output_bib, 'w', encoding='utf-8') as f:
        f.write(generate_bibtex(results))
        
    print(f"\n💾 {len(results)} resultados salvos em: {output_dir}")

if __name__ == "__main__":
    asyncio.run(main())
