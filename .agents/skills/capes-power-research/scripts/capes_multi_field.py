import os
import asyncio
from playwright.async_api import async_playwright
from capes_browser import CapesBrowser
from capes_filters import CapesFilters, SearchRow

class CapesMultiFieldBrowser(CapesBrowser):
    async def search_with_multi_field(self, page, filters: CapesFilters):
        print(f"🔍 Iniciando busca multi-campo...")
        await page.goto(self.search_url)
        
        # Garantir que estamos na aba de Busca Avançada
        print("⚙️ Verificando estado do formulário...")
        # Verificar se os campos avançados já estão visíveis (usando o seletor verificado select.campo)
        is_advanced = await page.query_selector("select.campo")
        
        # Fechar banner de Cookies se existir (Utilizando o método da classe base)
        await self.accept_cookies(page)

        if not is_advanced:
            print("⚙️ Ativando formulário de Busca Avançada...")
            try:
                # Tentar clicar no link de busca avançada
                await page.click("a:has-text('Busca Avançada'), #btn-busca-avancada", timeout=10000, force=True)
                print("⏳ Aguardando renderização do formulário...")
                await page.wait_for_timeout(3000) # Wait for animation
                await page.wait_for_selector("select.campo", timeout=15000, state="visible")
                print("✅ Formulário de Busca Avançada detectado.")
            except Exception as e:
                print(f"⚠️ Falha ao ativar Busca Avançada via clique: {e}")
                await page.screenshot(path="failed_advanced_click.png")
                # Forçar redirecionamento se o clique falhar
                print("🔗 Forçando redirecionamento direto para o buscador avançado...")
                await page.goto("https://www-periodicos-capes-gov-br.ez54.periodicos.capes.gov.br/index.php/acervo/buscador.html?advanced=true")
                await page.wait_for_selector("select.campo", timeout=20000, state="visible")
        else:
            print("✅ Formulário de Busca Avançada já está ativo.")
        
        # Esperar pela primeira linha de busca (garantia usando seletor verificado)
        await page.wait_for_selector("select.campo", timeout=10000)
        
        # Mapeamento de nomes de campos para os valores do dropdown
        field_map = {
            "Any": "Qualquer campo",
            "Title": "Título",
            "Author": "Autor",
            "Subject": "Assunto"
        }

        # Preencher cada linha
        # Obter todas as linhas de busca
        rows = await page.query_selector_all("div.linha-busca")
        
        for i, row_data in enumerate(filters.search_rows):
            # Se precisarmos de mais linhas do que as que já existem
            if i >= len(rows):
                print(f"➕ Adicionando campo {i+1} ({row_data.operator})...")
                await page.click("#add-field", force=True)
                await page.wait_for_timeout(1000)
                # Re-selecionar as linhas para pegar a nova
                rows = await page.query_selector_all("div.linha-busca")

            current_row = rows[i]
            print(f"✍️ Preenchendo linha {i+1}...")
            
            # Preencher a linha atual
            if i > 0:
                # Selecionar Operador Lógico
                op_selector = "select.op-logico"
                await current_row.wait_for_selector(op_selector, state="visible", timeout=5000)
                await current_row.select_option(op_selector, row_data.operator)

            # Selecionar Tipo de Campo
            campo_selector = "select.campo"
            await current_row.wait_for_selector(campo_selector, state="visible", timeout=5000)
            await current_row.select_option(campo_selector, row_data.field)
            
            # Preencher Termo
            input_selector = "input.form-control"
            await current_row.wait_for_selector(input_selector, state="visible", timeout=5000)
            await current_row.fill(input_selector, row_data.term)

        # Clicar em Buscar
        await page.click("button.btn-busca-avancada")
        
        # Aplicar filtros de sidebar (Copiado da classe base e adaptado)
        await page.wait_for_selector(".filtro-lateral", timeout=15000)
        
        if filters.start_year:
            await page.fill("input.ano.mr-1", str(filters.start_year))
            await page.fill("input.ano.ml-1", str(filters.end_year or 2026))

        if filters.open_access:
            await page.click("text='Acesso aberto' >> xpath=.. >> label:has-text('Sim')")

        if filters.peer_reviewed:
            await page.click("text='Revisado por pares' >> xpath=.. >> label:has-text('Sim')")

        await page.click("button.br-button.block.primary.w-100")
        await page.wait_for_timeout(3000)

    async def run_advanced(self, filters: CapesFilters):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                await self.login_cafe(page)
                await self.search_with_multi_field(page, filters)
                results = await self.scrape_results(page)
                return results
            except Exception as e:
                print(f"❌ Erro na automação avançada: {e}")
                await page.screenshot(path="error_multi_field.png")
                return []
            finally:
                await browser.close()

if __name__ == "__main__":
    # Teste rápido
    test_filters = CapesFilters(
        search_rows=[
            SearchRow(term="Artificial Intelligence", field="Subject"),
            SearchRow(term="Civil Engineering", field="Any", operator="AND"),
            SearchRow(term="Wood", field="Any", operator="NOT")
        ],
        start_year=2021,
        open_access=True
    )
    browser = CapesMultiFieldBrowser()
    asyncio.run(browser.run_advanced(test_filters))
