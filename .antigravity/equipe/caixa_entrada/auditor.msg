===== CAIXA DE ENTRADA — Auditor =====
De: Condutor (SandecoMaestro)
Data: 2026-04-19

Sua responsabilidade: rodar os criterios de aceite APOS cada bloco concluido.
Se qualquer criterio falhar, bloqueie a liberacao do proximo bloco.

--- APOS BLOCO-0 ---
python -c "import src.api.server_v3; print('server OK')"
curl http://localhost:8010/ | python -m json.tool
# Verificar: "total_routers": 27

--- APOS BLOCO-A ---
grep -rn "from src\.database" src/modules/ --include="*.py"
# Deve retornar ZERO
python -c "from src.modules.core.persistence.db_factory import DatabaseFactory; print('BLOCO-A OK')"
# Testar que a importacao NAO abre conexao com banco:
python -c "
import os; os.environ.pop('DB_HOST', None)
from src.modules.core.persistence.db_factory import DatabaseFactory
print('Lazy init OK — sem conexao no import')
"

--- APOS BLOCO-B ---
grep -rn "from src\.services\.whatsapp\.cloud_service" src/modules/ --include="*.py"
# Deve retornar ZERO
python -c "from src.modules.operacional.communication.cloud_service import WhatsAppCloudService; print('BLOCO-B OK')"

--- APOS BLOCO-C ---
grep -rn "from src\.utils" src/workers/ --include="*.py"
# Deve retornar ZERO (exceto workers v1 legados — aceitavel)
python -c "from src.modules.core.utils.worker_utils import BusinessHoursGuard; print('BLOCO-C OK')"

--- APOS BLOCO-D ---
grep -rn "from src\.services\." src/modules/ --include="*.py"
# Deve retornar ZERO

--- APOS BLOCO-E (AUDITORIA FINAL) ---
echo "=== AUDITORIA FINAL ==="
grep -rn "from src\.database" src/modules/ --include="*.py" | grep -v __pycache__
grep -rn "from src\.services\." src/modules/ --include="*.py" | grep -v __pycache__
grep -rn "from src\.utils" src/modules/ --include="*.py" | grep -v __pycache__
grep -rn "from src\.logic" src/modules/ --include="*.py" | grep -v __pycache__
echo "=== Se todos os blocos acima estao VAZIOS: MISSAO CUMPRIDA ==="

--- SEC-001 (pode auditar a qualquer momento) ---
grep -rn "f\"SELECT\|f'SELECT\|f\"UPDATE\|f'UPDATE\|f\"INSERT\|f'INSERT" src/modules/ --include="*.py"
# Deve retornar ZERO apos a correcao

ARQUIVOS COM VULNERABILIDADE CONFIRMADA:
  src/modules/core/audit/data_extractor.py:39
  src/modules/core/persistence/sis_repository.py:86
  src/modules/core/persistence/template_repository.py:22,37
  src/modules/operacional/scheduling/calendar_service.py:51
  src/modules/tatico/analytics_dashboard/analytics_routes.py:73
  src/modules/core/persistence/journey_journal_service.py:127

PADRAO CORRETO:
  # ANTES (vulneravel)
  cursor.execute(f"SELECT * FROM {table} LIMIT 1")

  # DEPOIS (seguro)
  from psycopg2 import sql
  cursor.execute(sql.SQL("SELECT * FROM {} LIMIT 1").format(sql.Identifier(table)))

Atualize o registro_atividades.json alterando "status" de cada bloco para "CONCLUIDO" apos validacao.
===== FIM =====
