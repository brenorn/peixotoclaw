---
name: refactor-twin-brain
description: Especialista em refatoração e limpeza de projetos legados ou em produção. Utiliza a lógica Twin-Brain para separar a análise de preservação (lógica/nomes) da execução técnica, garantindo que importações e constantes core não sejam destruídas. Use sempre que o usuário pedir para "limpar", "refatorar", "organizar código" ou "migrar pastas".
---

# Refactor Twin-Brain 🧠🧠

Esta habilidade implementa um protocolo de segurança em dois estágios para evitar que a refatoração por IA quebre sistemas complexos.

## 🛠️ Estágio 1: O Analista (Creation of Preservation Manifest)

Antes de alterar QUALQUER linha de código, você deve gerar um `PRESERVATION_MANIFEST.md` no diretório do projeto.

### Itens Obrigatórios no Manifesto:
1.  **Imutáveis (Core Constants)**: Nomes de variáveis, chaves de dicionário e constantes que NÃO podem ser alteradas (devido a dependências de banco ou API).
2.  **Lógica Sensível**: Trechos de cálculo matemático ou "prompts" de IA que foram refinados e não devem ser "simplificados".
3.  **Mapa de Importação**: Lista de arquivos que importam o arquivo atual e precisam ser atualizados se o arquivo mudar de lugar.

## 🏗️ Estágio 2: O Executor (Refactor with Context)

Com o manifesto em mãos, realize a limpeza seguindo estes limites:
- **Prioridade de Nome**: Se o manifesto diz "Mantenha o nome X", você não deve sugerir nomes "mais bonitos".
- **Grep-Check**: Após renomear um arquivo ou variável, rode um comando `grep` global no projeto para encontrar e corrigir referências perdidas.
- **Atomicidade**: Refatore um módulo por vez. Valide um antes de seguir para o próximo.

## 🔍 Verificação Final (QA)

Sempre entregue um `REFACTOR_REPORT.md` contendo:
1.  **Mudanças Realizadas**: Lista de arquivos e variáveis alteradas.
2.  **Consistência de Importação**: Confirmação de que o `grep` não encontrou referências ao caminho/nome antigo.
3.  **Preservação de Lógica**: Confirmação de que os cálculos marcados no manifesto foram mantidos idênticos.

---
"Limpar a casa não significa jogar fora as chaves."
