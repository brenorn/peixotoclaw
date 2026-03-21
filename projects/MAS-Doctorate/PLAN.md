# 🧪 PLAN: MAS-Doctorate AI Framework

**Objetivo Central**: Desenvolver um Sistema Multi-Agente (MAS) para gestão de prazos na construção civil, focado em escalabilidade SaaS e evolução contínua da inteligência.

---

## 🚀 Cenário 1: O Mais Rápido (MVP)
*Foco: Validação imediata da arquitetura de agentes.*
- Implementar o `AgentController` básico com FastAPI.
- Criar um agente de "Cronograma" que lê arquivos MS Project/Excel.
- Interface simples em React para chat e visualização de prazos.

## 🛡️ Cenário 2: O Mais Seguro (Auditável)
*Foco: Governança de dados e segurança de tese.*
- Todas as skills passam pelo `skill-auditor` MANDATÓRIO.
- Implementação de auditoria log-by-log das decisões dos agentes.
- Criptografia de dados de projetos sensíveis no PostgreSQL.

## 🏗️ Cenário 3: O Mais Escalável (SaaS Factory)
*Foco: Industrialização e Multi-tenancy.*
- Arquitetura de microserviços (Event-driven).
- **Auto-Evolução (EvoSkill)**: O sistema aprende com cada atraso de obra registrado no log.
- Deploy via Docker Compose / K8s ready.

---
**Status Atual**: `[INITIALIZING]`
**Verdade Absoluta (SSOT)**: [METADATA_MASTER.md](file:///d:/OneDrive/aiproj/PeixotoClaw/METADATA_MASTER.md)
