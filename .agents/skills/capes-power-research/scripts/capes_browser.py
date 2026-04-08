import os
import asyncio
import json
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

class CapesBrowser:
    def __init__(self):
        self.user_unb = os.getenv("USER_UNB")
        self.key_unb = os.getenv("KEY_UNB")
        self.base_url = "https://www.periodicos.capes.gov.br/index.php/acesso-cafe.html"
        self.search_url = "https://www-periodicos-capes-gov-br.ez54.periodicos.capes.gov.br/index.php/acervo/buscador.html"

    async def accept_cookies(self, page):
        """Identifica e aceita o banner de cookies se estiver presente."""
        print("🍪 Verificando banner de cookies...")
        try:
            # Seletores identificados no screenshot e variações comuns
            selectors = [
                "button#consent-accept", 
                "button#onetrust-accept-btn-handler",
                "button:has-text('Aceitar')", 
                "button:has-text('Accept all')",
                "button:has-text('Concordo')",
                "button:has-text('Fechar')",
                ".br-button.primary:has-text('Aceitar')"
            ]
            selector = ", ".join(selectors)
            cookie_accept = await page.wait_for_selector(selector, timeout=5000)
            if cookie_accept:
                await cookie_accept.click()
                print("✅ Cookies aceitos.")
                await page.wait_for_timeout(2000) # Wait for overlay to vanish
        except:
            print("ℹ️ Banner de cookies não detectado ou já aceito.")

    async def login_cafe(self, page):
        print("🔐 Iniciando Login CAFe (UnB)...")
        await page.goto(self.base_url)
        
        # 1. Selecionar Instituição
        print("🔍 Pesquisando Universidade de Brasília...")
        await page.wait_for_selector("input#select-simple", timeout=60000)
        await page.fill("input#select-simple", "Universidade de Brasília")
        await page.wait_for_timeout(1000)
        
        # Clicar na opção que contém "UNB"
        print("👆 Selecionando opção da UnB...")
        await page.click("div[role='option']:has-text('UNB')")
        
        # Clicar em Enviar (Usando seletor de texto para estabilidade)
        await page.click("button:has-text('Enviar')")
        
        # 2. Página de Login UnB (Shibboleth)
        print("🆔 Preenchendo credenciais UnB...")
        # Usar seletores flexíveis
        await page.wait_for_selector("input[name='j_username'], input#username", timeout=30000)
        await page.fill("input[name='j_username'], input#username", self.user_unb)
        await page.fill("input[name='j_password'], input#password", self.key_unb)
        # Clicar no botão de submissão (Login ou Acessar)
        await page.click("button[type='submit'], button:has-text('Login'), button:has-text('Acessar')")
        
        # 3. Esperar redirecionamento e reconhecimento
        print("⏳ Aguardando reconhecimento institucional...")
        try:
            await page.wait_for_selector("text=/acessando .* portal por: UNB/i", timeout=30000)
        except:
            # Fallback caso a frase varie ou mostre apenas o logo da UnB
            await page.wait_for_selector("img[alt*='UNB'], text='UNB'", timeout=15000)
        
        print("✅ Login UnB Realizado com Sucesso!")
        await page.screenshot(path="login_success.png")

    async def download_pdf(self, page, article_url, filename):
        """Tenta navegar até o artigo e realizar o download do PDF."""
        print(f"📥 Tentando baixar PDF de: {article_url}")
        try:
            await page.goto(article_url)
            # Procurar por botões de PDF (Texto: 'Texto completo em PDF', 'Download PDF', etc)
            pdf_button = await page.wait_for_selector("text=/PDF/i", timeout=15000)
            
            if pdf_button:
                async with page.expect_download() as download_info:
                    await pdf_button.click()
                download = await download_info.value
# Adiciona o diretório do maestro para pegar o path_utils
import sys
import os
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "maestro_sandeco", "scripts")
sys.path.append(SCRIPTS_DIR)
try:
    import path_utils
except ImportError:
    path_utils = None

                if path_utils:
                    path = path_utils.resolve_path(os.path.join("data", "pdfs", filename))
                else:
                    path = os.path.join("data", "pdfs", filename)
                
                os.makedirs(os.path.dirname(path), exist_ok=True)
                await download.save_as(str(path))
                print(f"✅ PDF salvo em: {path}")
                return True
            else:
                print("⚠️ Botão de PDF não encontrado.")
                return False
        except Exception as e:
            print(f"❌ Falha no download: {e}")
            return False

    async def search_with_filters(self, page, filters: dict):
        print(f"🔍 Buscando por: {filters['keywords']}")
        await page.goto(self.search_url)
        
        # Preencher termo de busca
        await page.wait_for_selector("input#input-busca")
        await page.fill("input#input-busca", " ".join(filters['keywords'])) 
        await page.click("button[aria-label='Buscar']")
        
        # Esperar carregar resultados para os filtros aparecerem
        await page.wait_for_selector(".filtro-lateral", timeout=15000)
        
        print("⚙️ Aplicando filtros avançados...")
        
        # Ano
        if filters.get('start_year'):
            await page.fill("input.ano.mr-1", str(filters['start_year']))
            await page.fill("input.ano.ml-1", str(filters['end_year'] or 2026))

        # Acesso Aberto (Sim)
        if filters.get('open_access'):
            # Localizar o container de Acesso Aberto e clicar no Sim
            await page.click("text='Acesso aberto' >> xpath=.. >> label:has-text('Sim')")

        # Revisado por Pares (Sim)
        if filters.get('peer_reviewed'):
            await page.click("text='Revisado por pares' >> xpath=.. >> label:has-text('Sim')")

        # Botão Filtrar
        await page.click("button.br-button.block.primary.w-100")
        await page.wait_for_timeout(3000) # Esperar recarregar

    async def scrape_results(self, page):
        print("📄 Extraindo metadados...")
        results = []
        
        # Esperar pelos itens de busca
        await page.wait_for_selector("div.item-busca", timeout=20000)
        cards = await page.query_selector_all("div.item-busca")
        
        for i, card in enumerate(cards[:10]):
            try:
                title_el = await card.query_selector("a.titulo-busca")
                title = await title_el.inner_text() if title_el else "Sem título"
                url = await title_el.get_attribute("href") if title_el else None
                
                author_el = await card.query_selector("a.view-autor")
                author = await author_el.inner_text() if author_el else "Autor desconhecido"
                
                abstract_el = await card.query_selector("div.text-description")
                abstract = await abstract_el.inner_text() if abstract_el else "Resumo não disponível"
                
                results.append({
                    "id": f"CAPES_{i+1:02d}",
                    "title": title.strip(),
                    "author": author.strip(),
                    "abstract": abstract.strip()[:300] + "...",
                    "url": url,
                    "local_path": None
                })
            except Exception as e:
                print(f"⚠️ Erro ao processar card: {e}")
            
        return results

    async def run(self, filters):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                await self.login_cafe(page)
                await self.search_with_filters(page, filters)
                results = await self.scrape_results(page)
                return results
            except Exception as e:
                print(f"❌ Erro na automação: {e}")
                await page.screenshot(path="error_capes.png")
                return []
            finally:
                await browser.close()

if __name__ == "__main__":
    # Teste rápido
    mock_filters = {
        "keywords": ["Multi-Agent Systems", "Construction Engineering"],
        "start_year": 2021,
        "end_year": 2026,
        "open_access": True,
        "peer_reviewed": True
    }
    browser = CapesBrowser()
    asyncio.run(browser.run(mock_filters))
