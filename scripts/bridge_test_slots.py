import sys
import os
import asyncio
import logging

# Configuração de Logs para captura de métricas
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("BridgeST")

# A PONTE: Injeta o projeto mind no runtime operacional
PROJECT_PATH = r'd:\OneDrive\aiproj\mind\vpn_mind'
sys.path.append(PROJECT_PATH)

# Altera diretório de trabalho para que o SlotEngine encontre o .env do mind
os.chdir(PROJECT_PATH)

try:
    from scripts.stress_test_slots import run_stress_test
    logger.info("🌉 [BRIDGE] Conexão estabelecida com SlotEngine (mind).")
except ImportError as e:
    logger.error(f"❌ [BRIDGE] Falha ao importar SlotEngine: {e}")
    sys.exit(1)

if __name__ == "__main__":
    logger.info("🔥 [STRESS] Disparando 100 agendamentos (Ingrid/Kethyly/Fulvio)...")
    asyncio.run(run_stress_test(100))
