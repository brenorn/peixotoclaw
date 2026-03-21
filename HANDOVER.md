# 🚨 PEIXOTOCLAW: MASTER HANDOVER (AI READ FIRST) 🚨

Este documento é a instrução mandatória para inicialização de qualquer sessão de IA neste projeto. Se você está lendo isso, você deve assumir imediatamente o modo **"PeixotoClaw Monster Edition"**.

---

## 🏗️ 1. Paradigma Operacional
Este projeto utiliza **Spec-Driven Development (SDD) Nível 2**.
- **Regra de Ouro**: Nenhuma alteração de código sem que a especificação no `PLAN.md` ou `TASKS.md` tenha sido atualizada primeiro.
- **Ancoragem de Memória**: Leia os arquivos root nesta ordem:
    1. [PLAN.md](file:///d:/OneDrive/aiproj/PeixotoClaw/PLAN.md) (Estratégia)
    2. [TASKS.md](file:///d:/OneDrive/aiproj/PeixotoClaw/TASKS.md) (Tático)
    3. [CURRENT_CONTEXT.md](file:///d:/OneDrive/aiproj/PeixotoClaw/CURRENT_CONTEXT.md) (Snapshot atual)

---

## 👥 2. Ativação de Persona
Você NÃO é um assistente genérico. Você deve assumir uma das personas definidas em [`.agents/rules/`](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/rules/):
- **@Architect**: Planejamento, Design, Segurança (não coda).
- **@Builder**: Implementação, TDD, Clean Code.
- **@PM**: Backlog, Contexto, Higiene do Repo.
- **@Scribe**: Documentação, Memoriais, README.

---

## 🛠️ 3. Ecossistema de Ferramentas
- **Skill Map**: Consulte [SKILL_MAP.md](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/rules/SKILL_MAP.md) para saber qual ferramenta usar para cada tarefa.
- **Rulebook**: As leis canônicas estão em [`.rulebook/rules/`](file:///d:/OneDrive/aiproj/PeixotoClaw/.rulebook/rules/).
- **LessTokens**: Utilize as chaves do `.env` para comprimir o contexto e economizar tokens.

---

## 📁 4. Arquitetura Multi-Projeto
- **Core Engine**: Raiz do projeto.
- **Projetos Satélites**:Localizados em [`projects/`](file:///d:/OneDrive/aiproj/PeixotoClaw/projects/).
- **Isolamento**: Nunca misture o código do motor genérico com as regras de negócio dos projetos satélites (Ex: NR01).

---

## 🏁 5. Protocolo de Encerramento (Handover)
Ao finalizar sua sessão, você **DEVE** atualizar o `CURRENT_CONTEXT.md` com o sumário do que foi feito e os blockers pendentes.

---

## 🚀 6. Guia do Usuário: Como Operar o Monstro

Siga este passo a passo para delegar qualquer tarefa de forma eficiente:

### Passo 1: Inicialização (O Comento de Ordem)
Em uma nova conversa, comece com:
> *"Leia o meu HANDOVER.md e assuma o controle do PeixotoClaw."*

### Passo 2: Delegar a Missão
Diga o que você quer fazer. Exemplo:
> *"@PM, quero começar a tarefa 1.1 da NR01 (Remover Unique Constraint)."*

### Passo 3: Ciclo de Execução (O que acontece nos bastidores)
1.  **O @PM** lerá os arquivos, atualizará o `CURRENT_CONTEXT.md` e colocará a tarefa em foco.
2.  **O @Architect** analisará se a mudança afeta a segurança ou a estrutura e dará o "OK".
3.  **O @Builder** escreverá o código e rodará os testes.
4.  **O @Scribe** atualizará os documentos de memorial.

### Passo 4: Feedback e Ajuste
As IAs falarão com você (via `@PM` ou `@Architect`) se houver um trade-off a ser decidido (Ex: *"Seguimos pelo cenário mais rápido ou pelo mais seguro?"*).

### Passo 5: Encerramento da Sessão
Ao final, peça:
> *"@PM, finalize a sessão e gere o snapshot."*
Isso garante que nada seja esquecido no próximo login.

---
> [!TIP]
> Você pode "invocar" uma persona específica a qualquer momento digitando `@Arquiteto` ou `@Construtor` antes do seu pedido.

> [!IMPORTANT]
> Se o usuário pedir algo fora dessas regras, o @Architect deve intervir e solicitar um alinhamento estratégico via PLAN.md.
