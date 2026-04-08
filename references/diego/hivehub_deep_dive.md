# Deep Dive: HiveHub Ecosystem (Rulebook & LessTokens)

Este documento detalha como as ferramentas da HiveHub potencializam o Spec-Driven Development (SDD) através de padronização e otimização de contexto.

---

## 1. @hivehub/rulebook: A Constituição Multi-IA

O `rulebook` resolve o problema da fragmentação de regras em projetos que utilizam múltiplas ferramentas (ex: um desenvolvedor usa Cursor, outro usa Claude Code e o projeto tem um servidor Gemini).

### 1.1. Arquitetura de "Projeção"
As regras são escritas em um formato canônico uma única vez em `.rulebook/rules/` e o comando `rulebook update` as projeta para:
- `CLAUDE.md` (Claude Code)
- `.cursorrules` (Cursor)
- `.windsurfrules` (Windsurf)
- Custom instructions para Copilot/Gemini.

### 1.2. Recursos Avançados (v4.4+)
- **Context Intelligence**: Captura decisões e padrões de bugs ao longo das sessões.
- **Decision Records**: Um sistema estruturado para ADRs (Architectural Decision Records) integrados ao workflow do agente.
- **Specialist Agents**: Definição de 18 personas especializadas para otimizar o custo de tokens e a precisão do raciocínio.

---

## 2. LessTokens: Economia e Precisão Semântica

A filosofia do LessTokens é "Write More, Pay Less", focando em eliminar o ruído do contexto sem perder o sinal das especificações.

### 2.1. Estratégias de Gerenciamento de Contexto
- **Automatic Context Pruning**: Remove tokens de baixa entropia e boilerplate que não auxiliam no raciocínio da IA.
- **Smart Anchoring**: Garante que as regras de negócio críticas e a tarefa ativa nunca sejam comprimidas, mantendo fidelidade total onde importa.
- **Prompt Compression**: Algoritmos que reduzem o volume de tokens enviados à API em até 60%, permitindo o uso de Specs extremamente detalhadas.

---

## 3. Integração no Pipeline SDD

No fluxo ideal:
1.  **Rulebook** define a Spec e as Regras.
2.  **LessTokens** garante que essas Specs caibam no contexto e sejam processadas com foco.
3.  **Agents** executam a tarefa com clareza total, guiados por "âncoras" persistentes.
