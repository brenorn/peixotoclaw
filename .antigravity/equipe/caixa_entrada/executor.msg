===== CAIXA DE ENTRADA — Executor =====
De: Condutor (SandecoMaestro)
Data: 2026-04-19

Sua responsabilidade: implementar cada bloco EXATAMENTE na ordem abaixo.
NAO pule blocos. NAO reordene. NAO comece o proximo sem o Auditor validar o atual.

=== ORDEM DE EXECUCAO ===

[BLOCO-0] — URGENTE — Zero pre-requisitos
  Spec: src/modules/dossie/2026_04_17_BLOCO_0_server_reconexao_spec.md
  Acao: Descomentar routers em server_v3.py em 4 grupos + testar boot apos cada grupo
  Regra: Se qualquer grupo falhar com ImportError, consultar RF-0-06 (guia de debug)
  Nao prossiga para o Grupo 3 sem o banco migrado (BLOCO-A necessario)

[BLOCO-C] — 10 minutos — Zero pre-requisitos
  Spec: src/modules/dossie/2026_04_17_BLOCO_C_worker_utils_spec.md
  Acao:
    mkdir -p src/modules/core/utils/
    cp src/utils/worker_utils.py src/modules/core/utils/worker_utils.py
    Editar retention_worker_v2.py linha 6: trocar import
    Editar noshow_worker_v2.py linha 6: trocar import

[BLOCO-A] — Aguardar aprovacao do Projetista para lazy init
  Spec: src/modules/dossie/2026_04_17_BLOCO_A_database_migration_spec.md
  ATENCAO CRITICA: db_factory.py tem singleton no import — OBRIGATORIO refatorar para lazy:
    REMOVER as 2 linhas no final do arquivo:
      legacy_db = DatabaseFactory.get_legacy_db()
      app_db = DatabaseFactory.get_app_db()
    Isso impede que o sistema quebre ao iniciar sem VPN

[BLOCO-B] — Pre-requisito: BLOCO-A concluido e auditado
  Spec: src/modules/dossie/2026_04_17_BLOCO_B_cloud_service_spec.md
  PRIMEIRO passo obrigatorio (RF-B01): verificar se whatsapp_adapter.py ja tem WhatsAppCloudService
    head -20 src/modules/operacional/communication/whatsapp_adapter.py
  So depois decidir: copiar cloud_service.py ou criar re-export

[BLOCO-D] — Pre-requisito: BLOCO-A + BLOCO-B concluidos
  Spec: src/modules/dossie/2026_04_17_BLOCO_D_services_migration_spec.md
  AGUARDAR aprovacao do Projetista com mapa de destinos validado
  Migrar na ORDEM EXATA (menor dependencia primeiro):
    btn_detector → template_service → messages_service → patient_service →
    appointment_updater → nps_repository → ... → confirmation_brain (ultimo)

[BLOCO-E] — Pre-requisito: TODOS os anteriores concluidos
  Spec: src/modules/dossie/2026_04_17_BLOCO_E_workers_migration_spec.md
  REGRA DE OURO: copiar antes de deletar. Nao apague os originais ate o teste funcionar.
  Apos mover: atualizar 4 linhas no start_guardian_v5.py (linhas 94, 98, 102, 106)

=== REGRAS DO EXECUTOR ===
  - Editar um arquivo por vez (TIER1_PROHIBITIONS PROHIBITION 5)
  - Testar importacao apos cada arquivo editado
  - Nunca usar --no-verify no git
  - Nunca deletar sem confirmar que o novo caminho funciona
  - Registrar conclusao de cada bloco no registro_atividades.json (status → "CONCLUIDO")

===== FIM =====
