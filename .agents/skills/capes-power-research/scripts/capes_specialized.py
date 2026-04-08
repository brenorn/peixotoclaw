import os
import asyncio
from playwright.async_api import async_playwright
from capes_bases_integration import CapesBasesIntegration
from capes_filters import CapesFilters

class CapesSpecialized(CapesBasesIntegration):
    async def search_scopus(self, page, query: str):
        print(f"🔬 Automação Scopus: Pesquisando '{query}'...")
        try:
            # Esperar pelo input de busca do Scopus
            search_input = await page.wait_for_selector("input[placeholder*='Search'], input#searchterminput", timeout=30000)
            await search_input.fill(query)
            await page.keyboard.press("Enter")
            
            print("⏳ Aguardando resultados do Scopus...")
            await page.wait_for_load_state("networkidle")
            
            results = []
            result_rows = await page.query_selector_all("tr.searchArea, .ddmDocTitle")
            
            for row in result_rows[:10]:
                title_elem = await row.query_selector("a")
                if title_elem:
                    title = await title_elem.inner_text()
                    url = await title_elem.get_attribute("href")
                    results.append({"title": title.strip(), "url": url, "source": "Scopus"})
            
            return results
        except Exception as e:
            print(f"⚠️ Erro ao automatizar Scopus: {e}")
            await page.screenshot(path="error_scopus.png")
            return []

    async def search_web_of_science(self, page, query: str):
        print(f"🔬 Automação Web of Science: Pesquisando '{query}'...")
        try:
            # 1. Resolver Banner de Cookies Clarivate (Verdejante no screenshot)
            try:
                cookie_btn = await page.wait_for_selector("#onetrust-accept-btn-handler, button:has-text('Accept all')", timeout=5000)
                if cookie_btn:
                    await cookie_btn.click()
                    print("✅ Cookies WoS aceitos.")
                    await page.wait_for_timeout(2000)
            except:
                pass

            # 2. Localizar Campo de Busca
            # Tentativa com placeholder, seletor de classe ou atributo de teste
            search_input = await page.wait_for_selector(".search-input, [data-testid='search-input'], textarea[placeholder*='Example'], input[placeholder*='Example']", timeout=20000)
            await search_input.click() 
            await search_input.fill(query)
            
            # 3. Clicar no botão Search
            # No screenshot o botão é roxo com texto 'Search'
            search_btn = await page.wait_for_selector("button:has-text('Search'), .search-button, [data-testid='search-button']", timeout=10000)
            await search_btn.click()
            
            # 4. Resultados
            print("⏳ Aguardando redirecionamento para resultados...")
            await page.wait_for_timeout(5000)
            await page.screenshot(path="wos_after_search_click.png")
            
            await page.wait_for_load_state("load")
            print("📊 Verificando página de resultados...")
            await page.wait_for_timeout(5000) # Estabilização final
            await page.screenshot(path="wos_results_render.png")
            
            results = []
            # Títulos costumam ter a classe 'title-link' ou similar
            result_titles = await page.query_selector_all("a[data-testid='title-link'], h3.title a")
            
            print(f"🧐 Localizados {len(result_titles)} candidatos a título.")
            
            for title_elem in result_titles[:10]:
                title = await title_elem.inner_text()
                url = await title_elem.get_attribute("href")
                results.append({"title": title.strip(), "url": url, "source": "Web of Science"})
            
            return results
        except Exception as e:
            print(f"⚠️ Erro ao automatizar Web of Science: {e}")
            await page.screenshot(path="error_wos_results.png")
            return []

    async def run_specialized_search(self, base_name: str, query: str):
        # Mapeamento de links diretos via Proxy CAPES (sugestão do usuário)
        direct_links = {
            "Web of Science - Coleção Principal (Clarivate)": "https://www-webofscience-com.ez54.periodicos.capes.gov.br/wos/woscc/basic-search",
            "Scopus": "https://www-scopus-com.ez54.periodicos.capes.gov.br"
        }
        
        intercepted_data = []

        async def handle_response(response):
            if "webofscience.com" in response.url and "json" in response.request.resource_type:
                try:
                    # Tentar capturar o JSON de resultados
                    if any(x in response.url.lower() for x in ["results", "records", "search"]):
                        data = await response.json()
                        intercepted_data.append(data)
                        print(f"📡 Metadata JSON interceptado: {response.url[:60]}...")
# Adiciona o diretório do maestro para pegar o path_utils
import sys
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "maestro_sandeco", "scripts")
sys.path.append(SCRIPTS_DIR)
import path_utils

                        # Salvar backup imediato (Dinâmico para o projeto ativo)
                        project_id = os.getenv("PEIXOTOCLAW_PROJECT", "MAS-Doctorate")
                        output_file = path_utils.resolve_path(os.path.join("projects", project_id, "data", "research", "intercepted_raw.json"))
                        os.makedirs(os.path.dirname(output_file), exist_ok=True)
                        with open(output_file, "w", encoding="utf-8") as f:
                            json.dump(intercepted_data, f, indent=2, ensure_ascii=False)
                except:
                    pass

        # Normalize input for matching
        normalized_base = base_name.lower().strip()
        found_link = None
        for key, link in direct_links.items():
            if key.lower() in normalized_base:
                found_link = link
                break

        async with async_playwright() as p:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=user_agent)
            page = await context.new_page()
            
            # Ativar interceptador
            page.on("response", handle_response)
            
            try:
                # 1. Login UnB via CAFe (Sempre necessário para ativar o Proxy)
                await self.login_cafe(page)
                
                # 2. Tentativa de Link Direto (Skip A-Z search)
                external_page = None
                if found_link:
                    print(f"🔗 Ativando link direto para '{base_name}': {found_link}")
                    await page.goto(found_link)
                    await page.wait_for_load_state("networkidle")
                    
                    # Verificar se estamos no domínio correto (Proxy CAPES troca . por -)
                    if "webofscience" in page.url or "scopus" in page.url:
                        external_page = page
                        print(f"✅ Deep Link validado: {page.url}")
                    else:
                        print("⚠️ Deep Link redirecionou para fora da base. Recorrendo à busca A-Z...")

                # 3. Fallback: Busca na lista A-Z se o deep link falhar
                if not external_page:
                    print(f"🔎 Recorrendo à busca A-Z para: {base_name}")
                    external_page = await self.search_and_open_base(page, base_name)
                
                if not external_page:
                    return []

                # 4. Interceptores Específicos
                results = []
                if "webofscience" in base_name.lower() or "science" in base_name.lower():
                    results = await self.search_web_of_science(external_page, query)
                elif "scopus" in base_name.lower():
                    results = await self.search_scopus(external_page, query)
                
                # Se interceptamos JSON, podemos tentar enriquecer ou substituir os resultados do scrap
                if intercepted_data:
                    print(f"💎 {len(intercepted_data)} blobs de dados interceptados. Processando metadados brutos...")
                    # Aqui poderíamos injetar lógica para converter o JSON interno do WoS em nosso formato padrão
                
                return results
            except Exception as e:
                print(f"❌ Erro na busca especializada de {base_name}: {e}")
                await page.screenshot(path=f"error_specialized_{base_name.lower().replace(' ', '_')}.png")
                return []
            finally:
                await browser.close()

if __name__ == "__main__":
    spe = CapesSpecialized()
    asyncio.run(spe.run_specialized_search("Web of Science - Coleção Principal (Clarivate)", "Artificial Intelligence in House Construction"))
