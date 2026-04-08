---
name: token-optimization
description: Regra para otimização de contexto usando LessTokens.
---

# Otimização de Contexto: LessTokens

## 📉 Objetivo
Maximizar a eficiência de custos e a precisão do raciocínio da IA, reduzindo o ruído do contexto em 60% sem perda de sinal técnico.

## 📜 Diretrizes
1.  **Identificação de Ambiente**: Verifique as chaves `LESSTOKEN_API_KEY` e `LESSTOKEN_BASE_URL` no arquivo `.env`.
2.  **Context Pruning**: Antes de carregar arquivos de pesquisa massivos (como o `estudo_sdd.md` ou logs), solicite ou utilize o servidor MCP/API LessTokens para extrair apenas os "âncoras semânticos".
3.  **Smart Anchoring**: Garanta que as regras de **Persona** (Arquiteto/Construtor) e o **PLAN.md** NUNCA sejam comprimidos ou omitidos do contexto.
4.  **Injeção de Resumo**: Prefira carregar resumos comprimidos em vez de arquivos brutos, a menos que o `@Builder` necessite da implementação exata de uma linha de código.

## 🚫 Restrições
- Não use LessTokens para arquivos de configuração sensíveis (`.env`, `package.json`).
- Sempre informe o usuário quando o contexto estiver sendo comprimido para auditoria.

---
*Assinado: System Architect*
