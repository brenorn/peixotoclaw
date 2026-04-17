
import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Carregar o .env da ai_engine
env_path = r"D:\OneDrive\aiproj\move_git\backend\ai_engine\.env"
load_dotenv(env_path)

def extract_full_schema():
    try:
        conn = psycopg2.connect(
            host=os.getenv('PGHOST', 'localhost'),
            port=os.getenv('PGPORT', '5432'),
            database=os.getenv('PGDATABASE', 'move_profile_db'),
            user=os.getenv('PGUSER', 'postgres'),
            password=os.getenv('PGPASSWORD', 'admin')
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Query para pegar tudo: Esquema, Tabela, Coluna e Tipo
        query = """
        SELECT 
            table_schema, 
            table_name, 
            column_name, 
            data_type, 
            is_nullable,
            column_default
        FROM 
            information_schema.columns 
        WHERE 
            table_schema NOT IN ('information_schema', 'pg_catalog')
        ORDER BY 
            table_schema, table_name, ordinal_position;
        """
        
        cur.execute(query)
        rows = cur.fetchall()
        
        schema_dict = {}
        for row in rows:
            s = row['table_schema']
            t = row['table_name']
            
            if s not in schema_dict:
                schema_dict[s] = {}
            if t not in schema_dict[s]:
                schema_dict[s][t] = []
                
            schema_dict[s][t].append({
                "column": row['column_name'],
                "type": row['data_type'],
                "nullable": row['is_nullable'],
                "default": row['column_default']
            })
            
        output_path = r"D:\OneDrive\aiproj\move_git\backend\ai_engine\src\domains\competency\_dossie\ESTRUTURA_BANCO_COMPLETA_2026-04-17.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(schema_dict, f, indent=4, ensure_ascii=False)
            
        print(f"Sucesso: Mapa de banco gerado em {output_path}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro na extração: {e}")

if __name__ == "__main__":
    extract_full_schema()
