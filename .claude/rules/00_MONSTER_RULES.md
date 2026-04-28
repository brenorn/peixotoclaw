# 🦞 PeixotoClaw Claude Rules (Monster Edition)

Este repositório utiliza uma arquitetura **Sandeco Monster Centralizada**.

## 🛡️ Regra de Ouro (MANDATÓRIO)
1. **SSOT**: A única fonte da verdade é o [**AGENTS.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/AGENTS.md).
2. **TIER 1**: Siga as proibições em [**TIER1_PROHIBITIONS.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/brain/TIER1_PROHIBITIONS.md).
3. **Segurança de Produção**: Antes de qualquer entrega, acione o `cyber-production-guardian` para auditoria LGPD e Hardening.
4. **Economia de Tokens**: Monitore o peso do contexto. Acima de 8k tokens, sugira a skill `sandeco-token-reduce`.

## 🏗️ Operação Industrial
- **Fluxo Sequencial**: Trabalhe em uma tarefa por vez.
- **Twin-Brain Refactor**: Refatorações EXIGEM `PRESERVATION_MANIFEST.md` antes da ação.
- **Sabedoria Global**: Sempre consulte `.agents/brain/wisdom/` ao iniciar novos projetos para evitar retrabalho.
- **Dossiê Automático**: Use `scripts/project_lifecycle.py` para gestão de contexto.
- **Protocolo de Fluxo (Anti-Freeze)**: Siga rigorosamente a Lei dos 300 (chunking) e Lei da Migalha (discovery stream) em tarefas densas.
- **Nomenclatura**: Arquivos de doc/spec EXIGEM o prefixo `YYYY_MM_DD_`.
- **Hermeticidade**: JAMAIS salve dados de clientes no root. Use o `_peixotoclaw` local do módulo.

Para qualquer dúvida operacional, consulte as **Referências de Alto Valor** em `.agents/brain/references/`.
