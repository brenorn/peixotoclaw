import asyncio
import os
from playwright.async_api import async_playwright
from capes_specialized import CapesSpecialized

async def wos_bridge(query):
    print("🚀 Iniciando Monster Bridge (Sessão Visível)...")
    
    async with async_playwright() as p:
        # Lançar navegador VISÍVEL (headless=False)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        spec = CapesSpecialized()
        
        try:
            # 1. Login Automático via CAFe
            print("🔐 Realizando login automático na UnB...")
            await spec.login_cafe(page)
            
            # 2. Ir para Web of Science
            wos_url = "https://www-webofscience-com.ez54.periodicos.capes.gov.br/wos/woscc/basic-search"
            print(f"🔗 Navegando para: {wos_url}")
            await page.goto(wos_url)
            
            print("\n" + "="*50)
            print("⚠️ AÇÃO REQUERIDA DO USUÁRIO:")
            print("1. Se o hCaptcha aparecer, resolva-o manualmente na janela do navegador.")
            print("2. Certifique-se de que a página de busca da Web of Science carregou.")
            print("3. NÃO FECHE o navegador ainda.")
            print("="*50 + "\n")
            
            input("✅ Após resolver o Captcha e ver a tela de busca, aperte ENTER aqui no terminal para continuar...")
            
            # 3. Agora o PeixotoClaw assume o controle para a pesquisa temática
            query = "Artificial Intelligence Structural Engineering"
            print(f"🔬 Iniciando pesquisa temática: {query}")
            
            # Re-utilizar a lógica de busca que já temos, mas na página aberta
            results = await spec.search_web_of_science(page, query)
            
            if results:
                print(f"✨ Sucesso! {len(results)} resultados extraídos.")
                # Salvar no Datacenter do Projeto Ativo
                project_id = os.getenv("PEIXOTOCLAW_PROJECT", "MAS-Doctorate")
                output_dir = f"d:\\OneDrive\\aiproj\\PeixotoClaw\\projects\\{project_id}\\data\\research"
                os.makedirs(output_dir, exist_ok=True)
                
                import json
                output_file = os.path.join(output_dir, "results_real.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                print(f"💾 Resultados salvos em: {output_file}")
            else:
                print("⚠️ Falha na extração. Verifique a janela do navegador.")
                
            input("\n🏁 Tarefa concluída. Analise os resultados e aperte ENTER para fechar o navegador...")

        except Exception as e:
            print(f"❌ Erro na Ponte: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "Artificial Intelligence Structural Engineering"
    asyncio.run(wos_bridge(query))
