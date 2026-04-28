---
name: security-auditor-domain
description: "Auditoria de segurança para módulos de domínio, prevenindo vazamento de dados, SQL injection e falhas de isolamento tenant."
---

# Skill: Security Auditor Domain 🛡️🔍

Especialista em Auditoria de Segurança para módulos de domínio no ecossistema PeixotoClaw. Focado em prevenir Vazamento de Dados (Data Leakage) e Injeção.

## Quando Ativar (Triggers)
- Sempre que um novo domínio (folder em `src/domains`) for criado.
- Ao refatorar arquivos de infraestrutura de banco (`db_client.py`).
- Ao adicionar novas rotas de API em `router.py`.

## Fluxo de Auditoria Técnica

### 1. Camada de Dados (SQL Security)
- Verifique se todas as queries usam parâmetros (psycopg2). **PROIBIDO** f-strings em queries SQL.
- Valide se o `search_path` está isolado por esquema (Domínio Silo).
- Verifique se há verificações explícitas de `company_id` em cláusulas `WHERE`.

### 2. Camada API (Fronteira)
- Audite se os headers de autenticação e tenant (`X-Company-ID`) são obrigatórios.
- Verifique se erros 500 não estão vazando o stack trace para o frontend (Information Disclosure).

### 3. Camada IA (Prompt Safety)
- Verifique o uso de delimitadores (`<tags>`) para separar o conteúdo do usuário das instruções do sistema.
- Procure por vulnerabilidades de "Pretend you are..." ou "Ignore original rules".

## Estrutura do Relatório de Auditoria
Sempre entregue no formato:
1. **Critical Findings**: Riscos de vazamento Cross-Tenant ou SQLi.
2. **Standard Non-Compliance**: Violação das regras PeixotoClaw.
3. **Actionable Patches**: Código pronto para corrigir a falha.

---
**Selo de Qualidade**: PeixotoClaw Industrial System v3.0
