# 📜 PeixotoClaw Universal Constitution (Monster Edition)

Este documento contém as regras fundamentais e invariáveis para todos os agentes do ecossistema PeixotoClaw. Referencie este documento para economizar tokens e garantir consistência.

## 🐍 Padrões de Codificação (Python First)
1. **Linguagem**: 100% Python 3.10+ para lógica, automação e scripts.
2. **Estilo**: Siga estritamente o **PEP 8**. Use nomes de variáveis descritivos em `snake_case`.
3. **Docstrings**: Todo módulo e função deve ter docstrings claras (Padrão Google ou NumPy).
4. **Tipagem**: Use `typing` (Type Hints) em todas as assinaturas de função.
5. **Hermeticidade**: Scripts devem ser auto-contidos ou usar a estrutura de Skills local.

## 🛡️ Segurança e Integridade
1. **Input Sanitization**: Todo input vindo do usuário ou de arquivos externos deve passar pelo `security.py`.
2. **Path Traversal**: Proibido acessar arquivos fora do workspace sem autorização explícita.
3. **Secrets**: NUNCA exponha chaves de API ou senhas. Use `.env` e o `universal_connector.py`.

## 🏗️ Fluxo de Trabalho e Arquitetura (GSD DNA)
1. **Siloed Sovereign (Soberania de Silo)**: Cada funcionalidade ou projeto deve existir em sua própria pasta independente. Proibido poluir o root do PeixotoClaw ou o `main` de um projeto com lógica densa.
2. **Regra dos 500**: Arquivos Python de lógica pura não devem exceder **500 linhas**. Ao atingir esse limite, a modularização em um novo micro-módulo é obrigatória.
3. **Goal-Backward**: Comece sempre pelo "O que deve ser VERDADE ao final?" antes de listar tarefas.
4. **Nyquist Isolation**: Um serviço só é considerado estável se puder ser testado de forma isolada (Mocking total de dependências externas).
5. **Atomic Commits**: Commits devem ser focados em uma única mudança e seguir o padrão: `tipo(escopo): descrição`.

## 🤖 Comunicação entre Agentes
1. **MCI (Modular Context Injection)**: Mantenha seus prompts de sistema enxutos. Se precisar de uma metodologia complexa, chame a Skill correspondente.
2. **HMR (Hybrid Model Router)**: Saiba que você pode ser executado em diferentes modelos (Claude, Gemini). Ajuste sua verbosidade e precisão conforme o modelo ativo.

---
"Rigor, Velocidade e Eficiência de Tokens."
