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
        
        # Clicar em Enviar
        await page.click("button#enviarInstituicaoCafe")
        
        # 2. Página de Login UnB (Shibboleth)
        print("🆔 Preenchendo credenciais UnB...")
        await page.wait_for_selector("input#username", timeout=30000)
        await page.fill("input#username", self.user_unb)
        await page.fill("input#password", self.key_unb)
        await page.click("button.btn-primary") # Ajustado para .btn-primary conforme pesquisa
        
        # 3. Esperar redirecionamento e reconhecimento
        print("⏳ Aguardando reconhecimento institucional...")
        # O portal costuma mostrar uma barra ou mensagem confirmando o acesso UnB
        try:
            # Usar regex para ser mais flexível (este/esse/portal/periódicos)
            await page.wait_for_selector("text=/acessando .* portal por: UNB/i", timeout=30000)
        except:
            # Fallback caso a frase varie
            await page.wait_for_selector("text='UNB'", timeout=15000)
        
        print("✅ Login UnB Realizado com Sucesso!")
        await page.screenshot(path="login_success.png")

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
        print("📄 Extraindo resumos...")
        results = []
        
        # Esperar pelos itens de busca
        await page.wait_for_selector("div.item-busca")
        cards = await page.query_selector_all("div.item-busca")
        
        for card in cards[:10]:
            try:
                title_el = await card.query_selector("a.titulo-busca")
                title = await title_el.inner_text() if title_el else "Sem título"
                
                author_el = await card.query_selector("a.view-autor")
                author = await author_el.inner_text() if author_el else "Autor desconhecido"
                
                abstract_el = await card.query_selector("div.text-description")
                abstract = await abstract_el.inner_text() if abstract_el else "Resumo não disponível"
                
                results.append({
                    "title": title.strip(),
                    "author": author.strip(),
                    "abstract": abstract.strip()[:300] + "..."
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
