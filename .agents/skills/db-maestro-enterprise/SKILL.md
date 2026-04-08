---
name: db-maestro-enterprise
description: 'Skill para gestão de bancos de dados multitenant, segurança IAM e isolamento de dados de nível corporativo no ecossistema PeixotoClaw.'
---

# Skill: DB Maestro Enterprise (Scale Hub) 🏗️🔐

Esta habilidade especializa o Antigravity no design e operação de bancos de dados corporativos (Neo4j, ChromaDB, PG) em cenários de **Alta Escala e Multitenancy**. Foca na estrutura de Empresas, Gerentes e Equipes.

## 🚀 Camadas Operacionais

1.  **Auth & IAM (Identity Access Management)**: Implementar fluxos de Login/Registro baseados em JWT e RBAC (Role-Based Access Control).
2.  **Isolamento de Tenant**: Aplicar padrões de separação de dados (Namespace, Schema ou Banco Físico) para garantir que uma empresa nunca veja dados de outra.
3.  **Migrações de Esquema**: Coordenar mudanças estruturais em bases de dados distribuídas sem perda de integridade.
4.  **Auditoria de Logs**: Rastrear quem acessou o quê (Compliance Ph.D.).

## 🛠️ Padrões Recomendados

- **Tenant-per-Collection (Chroma)**: Usar coleções dinâmicas injetando o `CompanyID` no nome da coleção.
- **Prefix Isolation (Neo4j)**: Usar labels ou propriedades prefixadas (ex: `ORG_A_PROJECT_B`) para buscas rápidas e seguras.
- **Shared Context**: Permitir que bases de conhecimento "Públicas" (ex: NBRs) sejam acessadas por todos, mas "Privadas" (ex: Orçamentos) sejam isoladas.

## 📋 Regras de Ouro (Security First)

- **SQL/Cypher Injection Prevention**: Nunca concatenar IDs de Tenant diretamente em queries. Sempre usar parâmetros.
- **Validation Middleware**: Toda requisição de dados no backend deve passar por um validador de "Pertencimento" (O usuário X pertence ao Projeto Y da Empresa Z?).
- **Double Ledger**: Registrar mudanças estruturais no Dossiê de Governança corporativa.

---
**Versão**: 1.0 (Enterprise Tier)
**Status**: Operacional. 🔐
