# 🦞 PeixotoClaw Claude Rules (Monster Edition)

Este repositório utiliza uma arquitetura **Sandeco Monster Centralizada**.

## 🛡️ Regra de Ouro (MANDATÓRIO)
1. **SSOT**: A única fonte da verdade para padrões de arquitetura, qualidade e gatilhos é o arquivo [**AGENTS.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/AGENTS.md) na raiz.
2. **TIER 1**: Siga estritamente as proibições em [**TIER1_PROHIBITIONS.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/brain/TIER1_PROHIBITIONS.md).
3. **Sem Duplicação**: Não crie novas regras aqui. Use as Skills em `.agents/skills/`.

## 🏗️ Operação Industrial
- **Fluxo Sequencial**: Trabalhe em uma tarefa por vez.
- **Dossiê Automático**: Use `scripts/project_lifecycle.py` para gerenciar o contexto do projeto.
- **Higiene**: Mantenha o workspace limpo. Scripts temporários vão para `/scripts/trash/`.

Para qualquer dúvida operacional, consulte as **Referências de Alto Valor** em `.agents/brain/references/`.
