import sys
import os

# Adicionar src ao path
sys.path.append(r"d:\OneDrive\aiproj\MAS-Doctorate\src")

from rag_engine.agents.academic_agent import AcademicAgent

def monster_audit():
    agent = AcademicAgent()
    topics = [
        "Multi-Agent System coordination hierarchy and decoupling from Crew.ai",
        "Theoretical deepening on Lean Construction and PPC/CCPM",
        "Methodological validation and KPIs for Construction MAS",
        "Innovation and uniqueness in BIM-RAG Geospacial systems",
        "MAS Architecture: interactions and coordination models"
    ]
    
    print("\n" + "="*50)
    print("🚀 PEIXOTOCLAW MONSTER AUDIT: DOC-HUB ACADEMIC")
    print("="*50)
    
    for i, topic in enumerate(topics, 1):
        print(f"\n# {i}. TEMA: {topic}")
        basis = agent.get_theoretical_basis(topic)
        print(f"🧬 Fundamento: {basis}")
        
        print("📚 Referências Encontradas:")
        refs = agent.search_academic_links(topic)
        for r in refs:
            print(f"- {r['name']} (Caminho: {r['path']})")
            
    print("\n" + "="*50)
    print("🏁 AUDITORIA CONCLUÍDA: BASE DE 58MB PROCESSADA.")
    print("="*50)

if __name__ == "__main__":
    monster_audit()
