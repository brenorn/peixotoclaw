# scripts/test_neo4j_aura.py
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

def test_connection(user):
    uri = os.getenv("NEO4J_URI")
    password = os.getenv("NEO4J_PASSWORD")
    
    print(f"--- Testando Conexão ---")
    print(f"URI: {uri}")
    print(f"User: {user}")
    
    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Conexão OK' as msg")
            record = result.single()
            print(f"✅ SUCESSO: {record['msg']}")
            return True
    except Exception as e:
        print(f"❌ FALHA: {e}")
        return False
    finally:
        driver.close()

if __name__ == "__main__":
    # Testar padrão 'neo4j'
    if not test_connection("neo4j"):
        # Testar variante ID da instância
        instance_id = "1327d3fa"
        test_connection(instance_id)
