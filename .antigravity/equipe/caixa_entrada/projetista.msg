===== CAIXA DE ENTRADA — Projetista =====
De: Condutor (SandecoMaestro)
Data: 2026-04-19

Sua responsabilidade nesta missao:

BLOCO-A (Banco de Dados):
  Antes do Executor agir, valide:
  1. Destino correto: src/modules/core/persistence/ (nao core/database, nao core/db)
  2. Lazy init: db_factory.py NAO pode criar conexoes no import — confirme que o Executor
     vai refatorar as linhas:
       legacy_db = DatabaseFactory.get_legacy_db()  ← REMOVER (singleton no import)
       app_db = DatabaseFactory.get_app_db()         ← REMOVER (singleton no import)
     para retorno sob demanda apenas quando get_legacy_db() for chamado
  3. __init__.py deve re-exportar: DatabaseFactory, NexusBridge, PostgresBridge

BLOCO-D (15 Services WhatsApp):
  Antes do Executor agir, valide o mapeamento de destino:

  | Service | Destino em modules/ |
  |---|---|
  | btn_detector.py | modules/operacional/scheduling/ |
  | template_service.py | modules/operacional/communication/ |
  | messages_service.py | modules/operacional/communication/ |
  | patient_service.py | modules/operacional/scheduling/ |
  | appointment_updater.py | modules/operacional/scheduling/ |
  | nps_repository.py | VERIFICAR: ja existe duplicata em modules/? |
  | booster_service.py | VERIFICAR: ja existe versao em modules/tatico/? |
  | appointment_service.py | modules/operacional/scheduling/ (ja migrado?) |
  | behavior_analyzer.py | modules/operacional/whatsapp/ |
  | strategy_engine.py | modules/operacional/whatsapp/ |
  | retention_service.py | modules/operacional/whatsapp/ (ja existe? verificar) |
  | confirmation_brain.py | modules/operacional/orchestrator/ |
  | secretaria_brain.py | modules/operacional/orchestrator/ |
  | revenue_hunter.py | modules/tatico/analytics_dashboard/ |
  | attendant_service.py | modules/operacional/atendimento/ |

  IMPORTANTE: Confirme com o Executor que ele vai verificar duplicatas ANTES de sobrescrever.
  Ver RF-D-06 (nps_repository) e RF-D-07 (booster_service).

Responda nesta caixa quando aprovar o plano de cada bloco.
===== FIM =====
