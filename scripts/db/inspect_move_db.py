
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Carregar o .env da ai_engine
env_path = r"D:\OneDrive\aiproj\move_git\backend\ai_engine\.env"
load_dotenv(env_path)

def inspect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv('PGHOST', 'localhost'),
            port=os.getenv('PGPORT', '5432'),
            database=os.getenv('PGDATABASE', 'move_profile_db'),
            user=os.getenv('PGUSER', 'postgres'),
            password=os.getenv('PGPASSWORD', 'admin')
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        print("--- LISTA DE TABELAS (Schema Public) ---")
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cur.fetchall()
        for t in tables:
            print(f"\n[Tabela: {t['table_name']}]")
            cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{t['table_name']}';")
            columns = cur.fetchall()
            for c in columns:
                print(f"  - {c['column_name']} ({c['data_type']})")
                
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    inspect_db()
