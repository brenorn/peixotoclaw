---
name: data-governance
description: 'Garante a consistência de nomenclatura (variáveis, tabelas, colunas), integridade de esquemas e padrões de importação. Use para validar qualquer alteração de código ou banco de dados antes da implementação real.'
---

# Skill: Governança de Dados 🦞🛡️

Esta habilidade é o "Guardião da Verdade" do projeto. Seu objetivo é erradicar alucinações de nomenclatura, inconsistências em bancos de dados e erros de importação, utilizando um sistema de **Single Source of Truth (SSOT)**.

## O Coração da Governança: METADATA_MASTER.md

Toda inteligência de dados reside no arquivo `METADATA_MASTER.md` na raiz do projeto. Este arquivo contém a definição canônica de:
1. **Entidades & Tabelas**: Nomes exatos no banco de dados.
2. **Atributos & Colunas**: Tipagem, nomenclatura e restrições.
3. **Variáveis Globais**: Convenções de nomenclatura (CamelCase, snake_case, etc.).
4. **Dependências Core**: Versões de bibliotecas para evitar erros de importação.

## Fluxo de Trabalho DMAIC/PDCA

### 1. Define (Definição)
Antes de criar qualquer nova estrutura, consulte o `METADATA_MASTER.md`. Se a estrutura não existir, **proponha** a adição ao arquivo antes de codar.

### 2. Measure & Analyze (Medição e Análise)
Verifique se a nova proposta fere alguma regra de nomenclatura existente (ex: misturar inglês e português em nomes de colunas).

### 3. Improve (Melhoria)
Gere o código utilizando **EXATAMENTE** os termos do SSOT.
- **PROIBIDO**: Criar sinônimos (ex: usar `user_id` se o SSOT define `id_usuario`).
- **PROIBIDO**: Usar importações "cegas". Verifique o `package.json` ou `requirements.txt`.

### 4. Control (Controle)
Realize uma auditoria final:
- O código segue o `METADATA_MASTER.md`?
- As importações refletem as bibliotecas instaladas?
- O esquema do banco de dados está sincronizado?

## Regras de Ouro
- **NUNCA** assuma um nome de coluna. Leia o esquema.
- **NUNCA** use `import *`. Seja específico.
- Se encontrar uma inconsistência no sistema, sua primeira tarefa é reportar e sugerir a correção no `METADATA_MASTER.md`.

---
"A qualidade do dado é a base da inteligência."
