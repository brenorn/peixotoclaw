import asyncio
import os
from playwright.async_api import async_playwright
from capes_specialized import CapesSpecialized

async def deeplink_test():
    spe = CapesSpecialized()
    # Link direto sugerido pelo usuário
    url = "https://www-webofscience-com.ez54.periodicos.capes.gov.br/wos/woscc/basic-search"
    query = "Artificial Intelligence Structural Engineering"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            print("🔐 Iniciando Login...")
            await spe.login_cafe(page)
            
            print(f"🔗 Navegando para Deep Link: {url}")
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            
            # Screenshot de diagnóstico
            await page.screenshot(path="wos_deeplink_check.png")
            print(f"📸 Screenshot salvo: wos_deeplink_check.png")
            
            # Tentar a busca
            results = await spe.search_web_of_science(page, query)
            print(f"✅ Resultados: {len(results)}")
            
        except Exception as e:
            print(f"❌ Erro: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(deeplink_test())
