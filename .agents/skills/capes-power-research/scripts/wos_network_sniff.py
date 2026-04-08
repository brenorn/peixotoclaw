import asyncio
import os
import json
from playwright.async_api import async_playwright
from capes_specialized import CapesSpecialized

async def network_sniff():
    spe = CapesSpecialized()
    url = "https://www-webofscience-com.ez54.periodicos.capes.gov.br/wos/woscc/basic-search"
    query = "Artificial Intelligence Structural Engineering"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Interceptar respostas JSON
        async def handle_response(response):
            if "webofscience" in response.url and "json" in response.request.resource_type:
                print(f"📡 Interceptada resposta JSON: {response.url[:100]}...")
                try:
                    # Tentar ler o corpo da resposta
                    data = await response.json()
                    with open("wos_intercept_raw.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"✅ JSON salvo em: wos_intercept_raw.json")
                except:
                    pass

        page.on("response", handle_response)
        
        try:
            print("🔐 Iniciando Login...")
            await spe.login_cafe(page)
            
            print(f"🔗 Navegando para WoS...")
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            
            # Realizar a busca para disparar as requisições de rede
            results = await spe.search_web_of_science(page, query)
            print(f"🔎 Resultados (via scraper): {len(results)}")
            
        except Exception as e:
            print(f"❌ Erro: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(network_sniff())
