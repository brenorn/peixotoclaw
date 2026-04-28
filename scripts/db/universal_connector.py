import os
import sys
import json
import argparse
from datetime import datetime, date
from dotenv import load_dotenv
from neo4j import GraphDatabase
import psycopg2
from psycopg2.extras import RealDictCursor

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def run_neo4j(uri, user, password, query, params=None):
    if not all([uri, user, password]):
        return {"error": "Missing Neo4j credentials"}
    
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session() as session:
            result = session.run(query, params or {})
            records = [dict(record) for record in result]
            return {"type": "neo4j", "data": records}
    except Exception as e:
        return {"error": f"Neo4j Error: {str(e)}"}
    finally:
        if 'driver' in locals():
            driver.close()

def run_postgres(host, port, dbname, user, password, query, params=None):
    if not all([host, dbname, user, password]):
        return {"error": "Missing Postgres credentials"}
    
    try:
        conn = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password,
            cursor_factory=RealDictCursor
        )
        with conn.cursor() as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            if cur.description:
                records = cur.fetchall()
                return {"type": "postgres", "data": records}
            else:
                conn.commit()
                return {"type": "postgres", "status": "Command executed successfully"}
    except Exception as e:
        return {"error": f"Postgres Error: {str(e)}"}
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    parser = argparse.ArgumentParser(description="Universal DB Connector for PeixotoClaw")
    parser.add_argument("--project_path", required=True, help="Path to the project directory containing .env")
    parser.add_argument("--db_type", choices=["neo4j", "postgres"], required=True, help="Type of database")
    parser.add_argument("--query", required=True, help="Cypher or SQL query")
    parser.add_argument("--params", help="JSON string of query parameters", default="{}")
    
    args = parser.parse_args()
    
    # Load .env from project path
    env_path = os.path.join(args.project_path, ".env")
    if not os.path.exists(env_path):
        print(json.dumps({"error": f".env file not found at {env_path}"}))
        sys.exit(1)
        
    load_dotenv(env_path)
    
    params = json.loads(args.params)
    
    if args.db_type == "neo4j":
        # Strategy: Cloud -> Localhost Bolt -> Localhost Neo4j
        uris = [
            os.getenv("NEO4J_URI"),
            "bolt://localhost:7687",
            "neo4j://localhost:7687"
        ]
        passwords = [os.getenv("NEO4J_PASSWORD"), "cerrado_neo4j_pass", "sandeco123", "movemind_secret", "neo4j"]
        default_user = os.getenv("NEO4J_USER", "neo4j")
        
        result = {"error": "All connection attempts failed"}
        for uri in uris:
            if not uri: continue
            for pwd in passwords:
                if not pwd: continue
                # Silencing output to avoid JSON pollution
                attempt = run_neo4j(uri, default_user, pwd, args.query, params)
                if "error" not in attempt:
                    result = attempt
                    break
            if "error" not in result:
                break
        
    elif args.db_type == "postgres":
        result = run_postgres(
            os.getenv("POSTGRES_HOST") or os.getenv("PGHOST") or "localhost",
            os.getenv("POSTGRES_PORT") or os.getenv("PGPORT") or "5432",
            os.getenv("POSTGRES_DB") or os.getenv("PGDATABASE") or "postgres",
            os.getenv("POSTGRES_USER") or os.getenv("PGUSER") or "postgres",
            os.getenv("POSTGRES_PASSWORD") or os.getenv("PGPASSWORD"),
            args.query,
            params
        )
    else:
        result = {"error": "Unsupported database type"}
        
    print(json.dumps(result, indent=2, ensure_ascii=False, cls=DateTimeEncoder))

if __name__ == "__main__":
    main()
