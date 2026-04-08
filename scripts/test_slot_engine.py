import sys
import io
from datetime import date
from src.database.db_factory import DatabaseFactory
from src.modules.scheduling.slot_engine import SlotEngine

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_slot_engine():
    print("-" * 50)
    print("🔬 INICIANDO TESTE B: INTEGRIDADE DE SLOTS (NEXUS v2.0)")
    print("-" * 50)
    
    try:
        # Deixar o SlotEngine usar a Factory padrão internamente
        engine = SlotEngine(None)
        
        # Dados de teste baseados no sucesso do Teste A
        # Médico 216 em 2025-02-07 (Sexta-feira)
        doctor_id = 216
        test_date = date(2025, 2, 7)
        
        print(f"🔍 Gerando slots para Médico ID {doctor_id} em {test_date}...")
        
        slots = engine.get_available_slots(doctor_id, test_date)
        
        if slots:
            print(f"✅ SUCESSO: Motor gerou {len(slots)} slots disponíveis!")
            print(f"📌 Amostra de horários: {slots[:10]} ...")
            
            # Verificação de Conflito (Sabemos que 11:00 estava ocupado no Teste A)
            if "11:00" in slots:
                print("❌ FALHA: O horário 11:00 deveria estar filtrado (ocupado), mas apareceu na lista.")
            else:
                print("💎 CRITERIO DE OURO: O horário 11:00 foi filtrado corretamente como OCUPADO.")
        else:
            print("⚠️ AVISO: Nenhum slot gerado. Verifique se o médico possui escala para este dia da semana (Sexta).")

        print("-" * 50)
        print("🏁 FINAL DE TESTE: Auditoria de Algoritmo Concluída.")
        print("-" * 50)
        
    except Exception as e:
        print(f"💥 ERRO FATAL NO MOTOR: {e}")

if __name__ == "__main__":
    test_slot_engine()
