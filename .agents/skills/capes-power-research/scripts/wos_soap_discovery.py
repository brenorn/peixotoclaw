import sys
from wos import WosClient

def test_wos_connection():
    print("📡 Iniciando descoberta Web of Science (SOAP API)...")
    try:
        # Tentar autenticar usando apenas o IP da instituição (UnB)
        # O construtor sem argumentos tenta IP-based Auth
        with WosClient() as client:
            print("✅ Conexão estabelecida com sucesso!")
            # Tentar uma busca simples
            result = client.search('TS=Artificial Intelligence and TS=Structural Engineering')
            records_found = result.recordsFound
            print(f"📊 Busca direta via SOAP retornou {records_found} registros.")
            
            if records_found > 0:
                print("💎 Sucesso Total! O WWS SOAP está ativo para este IP.")
                # Se funcionar, salvaremos o SID para uso futuro
                print(f"🎫 Session ID (SID): {client.sid}")
            else:
                print("⚠️ Conectado, mas nenhum registro encontrado.")
                
    except Exception as e:
        print(f"❌ Erro na conexão SOAP: {e}")
        print("\n🔍 Dica: Se o erro for 'No matches returned', significa que o IP não tem permissão de API.")
        print("Buscando alternativa via SID extraído do Browser...")

if __name__ == "__main__":
    test_wos_connection()
