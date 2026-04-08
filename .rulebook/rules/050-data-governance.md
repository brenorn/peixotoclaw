# Rule 050: Data Governance & Integrity Lock 🔒

**CRITICAL**: Este projeto utiliza um sistema de **Single Source of Truth (SSOT)** para evitar regressões e alucinações.

## 🛡️ O Mandamento de Ouro
**NUNCA** altere uma rota, nome de variável global, coluna de banco de dados ou estrutura de API sem antes consultar o arquivo `METADATA_MASTER.md`.

## 📋 Protocolo de Modificação (Obrigatório)
Antes de qualquer `replace_file_content` em arquivos core:

1.  **Verify (Verificação)**: Use `grep_search` para encontrar todas as ocorrências do termo a ser alterado em todo o repositório.
2.  **Governance Check**: Use a skill `data-governance` para validar se a alteração fere o `METADATA_MASTER.md`.
3.  **Architect Approval**: O `@Architect` deve realizar uma análise de impacto de regressão e documentar o "Cenário de Risco" no `PLAN.md`.
4.  **Dry-Run (Simulação)**: Explique ao usuário o impacto exato da alteração (Ex: *"Isso vai quebrar 3 rotas no frontend, deseja prosseguir?"*).

## 🚫 Proibições Estritas (Tier 1)
- **PROIBIDO**: Renomear variáveis por "estética" ou "preferência" sem motivo técnico documentado.
- **PROIBIDO**: Criar sinônimos para a mesma entidade (Ex: `user`, `cliente`, `usr`). Escolha o nome do SSOT e siga-o.
- **PROIBIDO**: Alterar o esquema de banco de dados (`.sql` ou `.json`) sem atualizar o `METADATA_MASTER.md` no mesmo commit.

---
*Falha neste protocolo resultará em rejeição imediata do código pelo @Architect.*
