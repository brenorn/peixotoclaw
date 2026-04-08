# scripts/audit_ingestion_sync.py
import os
import sys

# Add path to the satellite project src
sys.path.append("d:/OneDrive/aiproj/MAS-Doctorate/src")

# Set env variables if possible or rely on .env in MAS-Doctorate root
from dotenv import load_dotenv
load_dotenv("d:/OneDrive/aiproj/MAS-Doctorate/.env")

from rag_engine.knowledge_graph.connector import Neo4jConnector

def list_files_recursive(root_path, extensions=('.pdf', '.pptx', '.docx')):
    """Lista todos os arquivos válidos recursivamente."""
    valid_files = []
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith(extensions):
                valid_files.append({
                    "name": file,
                    "path": os.path.join(root, file)
                })
    return valid_files

def get_ingested_files_from_neo4j():
    """Busca todos os arquivos já ingeridos no Neo4j Aura (Namespace :MAS_Doc)."""
    try:
        connector = Neo4jConnector()
        # Filtrar pelo label de isolamento :MAS_Doc
        query = "MATCH (a:AcademicDoc:MAS_Doc) RETURN a.name AS name, a.path AS path"
        results = connector.run_query(query)
        ingested = [record["name"] for record in results]
        connector.close()
        return ingested
    except Exception as e:
        print(f"⚠️ Erro ao conectar ao Neo4j Aura: {e}")
        return []

def run_audit(target_paths):
    print("🔍 Iniciando Auditoria de Ingestão (PeixotoClaw Sync)...\n")
    
    ingested_names = get_ingested_files_from_neo4j()
    print(f"✅ Total de arquivos detectados no Neo4j: {len(ingested_names)}")
    
    for label, path in target_paths.items():
        print(f"\n📂 Analisando Disciplina: {label}")
        print(f"📍 Caminho: {path}")
        
        disk_files = list_files_recursive(path)
        print(f"📄 Total no Disco (PDF/PPTX/DOCX): {len(disk_files)}")
        
        missing = [f for f in disk_files if f["name"] not in ingested_names]
        
        if missing:
            print(f"❌ GAPS ENCONTRADOS ({len(missing)} arquivos faltando):")
            for m in missing:
                print(f"   - {m['name']} (em {os.path.dirname(m['path'])})")
        else:
            print("✨ Sincronização 100%! Nenhum arquivo faltando.")

if __name__ == "__main__":
    targets = {
        "Estatistica": "d:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Estatistica",
        "Inovacao em Servicos": "d:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Inovaçao em Servicos"
    }
    run_audit(targets)
