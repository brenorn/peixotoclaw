import asyncio
import sys
import json
from dotenv import load_dotenv
from capes_filters import FilterExtractor, CapesFilters
from capes_multi_field import CapesMultiFieldBrowser
from capes_bases_integration import CapesBasesIntegration

load_dotenv()

async def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python capes_orchestrator.py \"Seu parágrafo de busca aqui\"")
        return

    user_input = sys.argv[1]
    
    # 1. Extrair Intenção e Filtros
    print("🤖 Analisando seu pedido...")
    extractor = FilterExtractor()
    filters: CapesFilters = extractor.extract(user_input)
    
    # 2. Roteamento: Base Específica vs Busca Geral
    # Se houver apenas um termo e ele parecer ser o nome de uma base conhecida
    known_bases = ["scopus", "web of science", "sciencedirect", "ieee", "acm"]
    found_base = None
    
    # Heurística simples: se o input contém o nome de uma base
    for base in known_bases:
        if base in user_input.lower():
            found_base = base
            break

    if found_base:
        print(f"🔗 Detectada intenção de acessar base específica: {found_base}")
        base_browser = CapesBasesIntegration()
        success = await base_browser.run_base_workflow(found_base)
        if success:
            print(f"✅ Sucesso! A base {found_base} foi aberta via Proxy CAPES.")
        else:
            print(f"⚠️ Não foi possível abrir a base {found_base} automaticamente.")
        return

    # 3. Busca Multi-Campo
    print(f"🎯 Filtros Extraídos para Busca Avançada:")
    print(json.dumps(filters.model_dump(), indent=2, ensure_ascii=False))
    
    browser = CapesMultiFieldBrowser()
    results = await browser.run_advanced(filters)
    
    if not results:
        print("\n⚠️ Nenhum resultado encontrado ou erro na automação.")
        return

    print("\n✅ Resultados Encontrados (Top 10):")
    print("-" * 50)
    for i, res in enumerate(results, 1):
        print(f"{i}. **{res['title']}**")
        print(f"   👤 {res['author']}")
        # print(f"   📝 {res['abstract']}") # Opcional: mostrar resumo
        print(f"   [ ] Selecionar para download")
        print("-" * 50)

    print("\n💡 Copie este Markdown para seu chat e marque [x] nos artigos que deseja baixar.")

if __name__ == "__main__":
    asyncio.run(main())
