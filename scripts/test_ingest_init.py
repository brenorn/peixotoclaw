# scripts/test_ingestor_init.py
import sys
import os

# Add src to path
sys.path.append("d:/OneDrive/aiproj/MAS-Doctorate/src")

print("--- Iniciando Teste de Inicialização ---")
try:
    from rag_engine.database.chroma_connector import ChromaConnector
    from rag_engine.knowledge_graph.connector import Neo4jConnector
    print("✅ Imports Básicos OK")
    
    from markitdown import MarkItDown
    import pdfplumber
    print("✅ Bibliotecas de Extração OK")
    
    # Testar inicialização
    from scripts.batch_ingest_disciplinas import AcademicMassIngestor
    print("⏳ Inicializando Ingestor (pode demorar)...")
    ingestor = AcademicMassIngestor()
    print("✅ Ingestor Inicializado com Sucesso!")
    
except Exception as e:
    print(f"❌ FALHA: {e}")
