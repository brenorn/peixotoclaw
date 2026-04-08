# scripts/final_audit_report.py
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load credentials from root .env
load_dotenv("d:/OneDrive/aiproj/PeixotoClaw/.env")

def count_on_disk():
    targets = [
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Estatistica',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Inovaçao em Servicos',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Metodologia Científica',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Métodos Matemáticos para Engenharia',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/ENGENHARIA DE CONFIABILIDADE',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Transporte',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/AVALIAÇÃO DE DESEMPENHO DE EDIFICAÇÕES',
        'd:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Gestao/Artigo'
    ]
    extensions = ['.pdf', '.pptx', '.docx']
    count = 0
    for target in targets:
        for root, dirs, files in os.walk(target):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    count += 1
    return count

def count_in_neo4j():
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")
    db = os.getenv("NEO4J_DATABASE")
    
    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        with driver.session(database=db) as session:
            # Contar apenas nós com label de isolamento :MAS_Doc
            result = session.run("MATCH (n:AcademicDoc:MAS_Doc) RETURN count(n) as total")
            return result.single()["total"]
    except Exception as e:
        print(f"Erro Neo4j: {e}")
        return -1
    finally:
        driver.close()

if __name__ == "__main__":
    disk_total = count_on_disk()
    cloud_total = count_in_neo4j()
    
    print(f"--- RELATÓRIO DE INGESTÃO ---")
    print(f"Total de Arquivos no Disco: {disk_total}")
    print(f"Total Indexado na Nuvem (Neo4j): {cloud_total}")
    
    if disk_total == cloud_total:
        print("✅ SINCRONIZAÇÃO COMPLETA: 100%")
    else:
        progress = (cloud_total / disk_total * 100) if disk_total > 0 else 0
        print(f"⏳ EM PROGRESSO: {progress:.1f}% ({cloud_total}/{disk_total})")
