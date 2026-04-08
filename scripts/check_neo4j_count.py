import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Try loading from both possible locations
load_dotenv("d:/OneDrive/aiproj/PeixotoClaw/.env")
load_dotenv("d:/OneDrive/aiproj/MAS-Doctorate/.env")

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
db = os.getenv("NEO4J_DATABASE")

print(f"Connecting to {uri} (DB: {db}) as {user}...")

driver = GraphDatabase.driver(uri, auth=(user, password))
try:
    with driver.session(database=db) as session:
        result = session.run("MATCH (a:AcademicDoc:MAS_Doc) RETURN count(a) as total")
        count = result.single()["total"]
        print(f"Total AcademicDoc:MAS_Doc found: {count}")
        
        # Also list first 5 names for verification
        result = session.run("MATCH (a:AcademicDoc:MAS_Doc) RETURN a.name AS name LIMIT 5")
        print("Sample names:")
        for record in result:
            print(f" - {record['name']}")
            
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.close()
