import os
import asyncio
from playwright.async_api import async_playwright
from capes_browser import CapesBrowser

class CapesBasesIntegration(CapesBrowser):
    async def search_and_open_base(self, page, base_name: str):
        print(f"🔎 Pesquisando base: {base_name} na Lista de Bases...")
        url_bases = "https://www-periodicos-capes-gov-br.ez54.periodicos.capes.gov.br/index.php/acervo/lista-a-z-bases.html"
        await page.goto(url_bases)
        
        # Preencher termo da base
        await page.wait_for_selector("input#termo")
        await page.fill("input#termo", base_name)
        
        # Clicar em Pesquisar
        await page.click("button.br-button.primary.float-end")
        await page.wait_for_timeout(2000)
        
        # Verificar se a base apareceu nos resultados
        # Procurar pelo link "Ver no editor" da primeira base que combine
        ver_no_editor = await page.query_selector("a.br-button.small.link-default.add-metrics")
        
        if ver_no_editor:
            print(f"🚀 Base '{base_name}' encontrada. Abrindo editor externo...")
            async with page.expect_popup() as popup_info:
                await ver_no_editor.click()
            
            external_page = await popup_info.value
            await external_page.wait_for_load_state("networkidle")
            
            print(f"🌍 Direcionado para: {external_page.url}")
            return external_page
        else:
            print(f"❌ Base '{base_name}' não encontrada na lista.")
            return None

    async def run_base_workflow(self, base_name: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False) # Headless=False para ver o "pulo" para a base
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                await self.login_cafe(page)
                external_page = await self.search_and_open_base(page, base_name)
                
                if external_page:
                    # Aqui poderíamos injetar automação específica para WoS ou Scopus
                    # Por enquanto, apenas confirmamos o acesso
                    await external_page.screenshot(path=f"base_{base_name.lower()}_access.png")
                    print(f"🎯 Acesso à base {base_name} confirmado via Proxy CAPES.")
                
                return external_page is not None
            except Exception as e:
                print(f"❌ Erro na integração de bases: {e}")
                return False
            finally:
                await browser.close()

if __name__ == "__main__":
    # Teste: Scopus ou Web of Science
    browser = CapesBasesIntegration()
    asyncio.run(browser.run_base_workflow("Web of Science"))
