---
name: universal-db-maestro
description: |
  Habilidade global para explorar e analisar bancos de dados Neo4j e Postgres/PostGIS de qualquer projeto satélite.
  Utilize esta skill sempre que precisar "estudar a base de dados", "consultar o grafo" ou "extrair dados espaciais" de um projeto.
  Ela detecta automaticamente o .env do projeto ativo e utiliza conectores Python para execução segura.
---

# Skill: Universal DB Maestro (Exploração de Dados Multi-Projeto)

Esta habilidade permite ao Antigravity atuar como um engenheiro de dados e analista de grafos universal, conectando-se dinamicamente às bases de dados de qualquer projeto dentro do ecossistema PeixotoClaw.

## 🚀 Como Funciona

1.  **Identificação do Projeto**: A cada nova consulta, verifique em qual diretório de projeto (`projects/{PROJETO}`) o trabalho está sendo realizado.
2.  **Carga de Credenciais**: Localize o arquivo `.env` dentro da pasta do projeto alvo.
3.  **Análise de Esquema**: Antes de consultas complexas, peça ao `Executor` para listar as labels/relacionamentos (Neo4j) ou tabelas/colunas (Postgres) para entender a estrutura dos dados.
4.  **Execução de Consultas**: Utilize o script `scripts/db/universal_connector.py` via linha de comando.

## 🛠️ Comandos de Execução (via Terminal)

Sempre utilize o Python para executar as consultas através do conector universal:

### No Neo4j (Cypher):
```bash
python scripts/db/universal_connector.py --project_path "projects/{PROJECT_NAME}" --db_type neo4j --query "MATCH (n) RETURN n LIMIT 5"
```

### No Postgres/PostGIS (SQL):
```bash
python scripts/db/universal_connector.py --project_path "projects/{PROJECT_NAME}" --db_type postgres --query "SELECT * FROM my_table LIMIT 5"
```

## 📋 Regras de Ouro

- **.env Obrigatório**: Nunca tente conectar-se sem apontar para o `--project_path` correto que contenha o arquivo `.env`.
- **Segurança**: Priorize consultas de LEITURA. Se precisar de ESCRITA, valide o impacto com o `@Architect`.
- **PostGIS**: Ao lidar com dados espaciais, utilize funções como `ST_AsText()` ou `ST_AsGeoJSON()` para facilitar a leitura dos resultados.

## 🧬 Integração com SandecoMaestro

Esta skill deve ser orquestrada pelo `SandecoMaestro` quando fizer parte de um fluxo de trabalho em equipe. O **Explorador** utiliza esta skill para alimentar o **Projetista** com dados reais da infraestrutura.

---
**Versão**: 1.0 (Global & Python-Powered)
**Status**: Operacional.
