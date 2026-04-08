import asyncio
import os
from playwright.async_api import async_playwright
from capes_specialized import CapesSpecialized

async def precision_test():
    spe = CapesSpecialized()
    # Usar exatamente o nome sugerido pelo usuário
    base_name = "Web of Science - Coleção Principal (Clarivate)"
    query = "Academic Productivity in Construction Engineering"
    
    print(f"🚀 Iniciando Teste de Precisão: {base_name}")
    results = await spe.run_specialized_search(base_name, query)
    
    if results:
        print(f"✅ SUCESSO! Recuperados {len(results)} resultados.")
        for r in results[:3]:
            print(f" - {r['title']}")
    else:
        print("❌ FALHA: Nenhum resultado recuperado.")

if __name__ == "__main__":
    asyncio.run(precision_test())
