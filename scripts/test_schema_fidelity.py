import sys
import io
import os
from datetime import date
from src.database.db_factory import DatabaseFactory
from src.modules.persistence.schema_registry import SchemaRegistry

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_schema_fidelity():
    print("-" * 50)
    print("🔬 INICIANDO TESTE A: FIDELIDADE DE SCHEMA (NEXUS v2.0)")
    print("-" * 50)
    
    try:
        db = DatabaseFactory.get_legacy_db()
        conn = db.get_connection()
        if not conn:
            print("❌ ERRO: Falha na conexão com o Banco Konsist.")
            return

        cur = conn.cursor(cursor_factory=None)
        
        # 1. Teste de Agendamento (arq_agendal)
        print("🔍 Buscando amostra real: arq_agendal...")
        cur.execute("SELECT * FROM arq_agendal LIMIT 1")
        row = cur.fetchone()
        
        if row:
            # Pegar nomes das colunas para simular um dicionário
            colnames = [desc[0] for desc in cur.description]
            legacy_dict = dict(zip(colnames, row))
            
            print("⚙️ Executando Mapeamento Semântico...")
            mapped = SchemaRegistry.map_appointment(legacy_dict)
            
            print("\n✅ RESULTADO DO MAPEAMENTO (AGENDAMENTO):")
            for k, v in mapped.items():
                print(f"   - {k}: {v} (Original: {SchemaRegistry.APPOINTMENT_MAP.get(k, 'N/A')})")
        
        # 2. Teste de Paciente (arq_paciente)
        print("\n🔍 Buscando amostra real: arq_paciente...")
        cur.execute("SELECT * FROM arq_paciente LIMIT 1")
        row_p = cur.fetchone()
        
        if row_p:
            colnames_p = [desc[0] for desc in cur.description]
            legacy_dict_p = dict(zip(colnames_p, row_p))
            mapped_p = SchemaRegistry.map_patient(legacy_dict_p)
            
            print("\n✅ RESULTADO DO MAPEAMENTO (PACIENTE):")
            for k, v in mapped_p.items():
                print(f"   - {k}: {v} (Original: {SchemaRegistry.PATIENT_MAP.get(k, 'N/A')})")

        conn.close()
        print("-" * 50)
        print("🏁 FINAL DE TESTE: Auditoria Concluída.")
        print("-" * 50)
        
    except Exception as e:
        print(f"💥 ERRO FATAL NA AUDITORIA: {e}")

if __name__ == "__main__":
    test_schema_fidelity()
