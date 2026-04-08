import os
import asyncio
from playwright.async_api import async_playwright
from capes_browser import CapesBrowser

class CapesBasesIntegration(CapesBrowser):
    async def search_and_open_base(self, page, base_name: str):
        print(f"🔎 Pesquisando base: {base_name} na Lista de Bases...")
        url_bases = "https://www-periodicos-capes-gov-br.ez54.periodicos.capes.gov.br/index.php/acervo/lista-a-z-bases.html"
        await page.goto(url_bases)
        
        # Aceitar cookies se houver banner bloqueando
        print("🍪 Verificando cookies na lista de bases...")
        await self.accept_cookies(page)
        
        # Preencher termo da base (usar apenas o nome principal para a busca)
        short_name = base_name.split(' - ')[0] if ' - ' in base_name else base_name
        print(f"⌨️ Digitanto '{short_name}' no buscador A-Z...")
        await page.wait_for_selector("input#termo")
        await page.fill("input#termo", short_name)
        
        # Clicar em Pesquisar
        await page.click("button.br-button.primary.float-end")
        await page.wait_for_timeout(2000)
        
        # Verificar se a base apareceu nos resultados
        print(f"🎯 Aguardando renderização dos resultados...")
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path="az_list_debug.png")
        
        # Procurar por um bloco que contém o título específico
        print(f"🎯 Buscando container para '{base_name}'...")
        
        try:
            # Tentar match exato primeiro, depois substring se falhar
            container_selector = f"div.resultado-bases:has-text('{base_name}')"
            base_container = await page.wait_for_selector(container_selector, timeout=10000)
            
            if not base_container:
                 # Fallback substring
                 base_container = await page.wait_for_selector(f"div.resultado-bases:has-text('{base_name.split(' - ')[0]}')", timeout=10000)

            if base_container:
                ver_no_editor = await base_container.query_selector("a:has-text('Ver no editor')")
                if ver_no_editor:
                    print(f"🚀 Base '{base_name}' localizada. Abrindo editor externo...")
                    async with page.expect_popup() as popup_info:
                        await ver_no_editor.click()
                    
                    external_page = await popup_info.value
                    await external_page.wait_for_load_state("load")
                    print(f"🌍 Direcionado para: {external_page.url}")
                    return external_page
        except Exception as e:
            print(f"⚠️ Erro ao localizar base: {e}")
            await page.screenshot(path="error_az_selection.png")
            
        print(f"❌ Base '{base_name}' não encontrada ou link indisponível.")
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
