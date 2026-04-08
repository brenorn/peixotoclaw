from neo4j import GraphDatabase
import os

uri = "neo4j+s://1327d3fa.databases.neo4j.io"
user = "neo4j" # Aura default is usually neo4j, even if .env says otherwise
password = "6NYNHVr7ASQgbPxDpKtTkSOkCfnO3eOAt1JCu2Ow-h8"

def test_conn():
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session() as session:
            result = session.run("CALL db.labels() YIELD label RETURN label")
            labels = [record["label"] for record in result]
            print(f"[OK] Connection Successful! Labels: {labels}")
            
            result_rel = session.run("CALL db.relationshipTypes() YIELD relationshipType RETURN relationshipType")
            rels = [record["relationshipType"] for record in result_rel]
            print(f"[OK] Relationships: {rels}")
    except Exception as e:
        print(f"[ERROR] Failed with user neo4j: {str(e)}")
        # Try with the user from .env
        try:
            user_alt = "1327d3fa"
            driver = GraphDatabase.driver(uri, auth=(user_alt, password))
            with driver.session() as session:
                result = session.run("CALL db.labels() YIELD label RETURN label")
                labels = [record["label"] for record in result]
                print(f"[OK] Connection Successful (Alt User)! Labels: {labels}")
        except Exception as e2:
            print(f"[ERROR] Failed with user 1327d3fa: {str(e2)}")

if __name__ == "__main__":
    test_conn()
