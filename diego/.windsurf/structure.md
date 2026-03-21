seu-projeto/
├──.windsurf/
│   ├── rules/              # O "Cérebro" (Como agir)
│   │   ├── architect.md
│   │   ├── builder.md
│   │   └── scribe.md
│   └── workflows/          # Os "Processos" (O que fazer)
│       ├── feature.md
│       └── document.md
├── docs/
│   └── MEMORIAL.md         # Memória Profunda (Legado + Novo)
├── PLAN.md                 # Estratégia (Migrado do seu roadmap)
├── TASKS.md                # Tático (Migrado das suas tasks)
└── README.md               # Capa do Projeto


seu-projeto/
├──.windsurf/               <-- Apenas o "Cérebro" da IA
│   ├── rules/
│   │   ├── architect.md
│   │   ├── builder.md
│   │   ├── pm.md
│   │   └── scribe.md
│   └── workflows/
│       ├── architect.md
│       └── structure.md     <-- (Corrigido)
├── PLAN.md                  <-- Na Raiz (Sua "Constituição")
├── TASKS.md                 <-- Na Raiz (Seu "Checklist Diário")
├── CURRENT_CONTEXT.md       <-- Na Raiz (O "Estado Atual")
├── README.md
└── src/                     <-- Seu código Django


seu-projeto/
├──.windsurf/               <-- Apenas o "Cérebro" da IA (Regras/Workflows)
│   ├── rules/
│   │   ├── architect.md
│   │   ├── builder.md
│   │   ├── pm.md
│   │   └── scribe.md
│   └── workflows/
│       ├── architect.md
│       └── structure.md     <-- (Corrigido)
├── PLAN.md                  <-- Na Raiz (Sua "Constituição")
├── TASKS.md                 <-- Na Raiz (Seu "Checklist Diário")
├── CURRENT_CONTEXT.md       <-- Na Raiz (O "Estado Atual")
├── README.md
└── src/                     <-- Seu código Django



| Papel no Projeto                     | Modelo Recomendado                                                       | Por que?                                                                                                                                                            | Custo/Velocidade     |
| ------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **O Arquiteto (Deep Planner)** | **Claude Opus 4.1 (Thinking)** ou **GPT-5 (High Reasoning)** | Capacidade massiva de "Chain of Thought". Ele não alucina arquitetura; ele*simula* o sistema mentalmente antes de propor. Essencial para criar o `plan.md`. ^^ | Alto / Lento         |
| **O Gerente de Projeto**       | **Claude 3.7 Sonnet (Thinking)**                                   | O equilíbrio perfeito. Inteligente o suficiente para atualizar `tasks.md` e verificar progresso, mas mais rápido que o Opus.                                    | Médio / Médio      |
| **O Engenheiro Sênior**       | **Claude 3.7 Sonnet**                                              | O padrão ouro para*escrever* lógica complexa (Python/Django). Segue instruções melhor que qualquer outro.                                                     | Médio / Rápido     |
| **O "Estagiário" Veloz**      | **Grok Code Fast 1**                                               | Latência zero. Use para boilerplate, testes unitários simples, CSS, e scripts de migração onde a lógica já está definida.                                    | Baixo / Instantâneo |
| **O Bibliotecário**           | **Gemini 2.5 Pro**                                                 | Janela de contexto massiva. Use para ingerir documentação inteira do GCP, Django ou logs de erro gigantescos para RAG.                                            | Médio / Rápido     |



# Arquitetura de Orquestração Cognitiva e Fluxos de "Vibe Coding" no Windsurf IDE (Edição 2026)

## 1. Introdução: A Era da Orquestração de Modelos Híbridos

Estamos operando em um cenário onde o gargalo não é mais a geração de código, mas a  **gestão de contexto e raciocínio** . Com acesso a modelos de fronteira como  **Claude Opus 4.1 (Thinking)** , **GPT-5** e  **Grok Code Fast** , o Windsurf deixa de ser um editor e torna-se um console de comando para múltiplas inteligências artificiais.^1^

Esta estratégia atualizada foca em atribuir o modelo certo para a tarefa cognitiva certa, maximizando a eficiência (velocidade do Grok) e a eficácia (raciocínio do Opus/GPT-5). Além disso, implementamos um "Sistema Operacional de Projeto" rigoroso baseado em arquivos de estado (`plan.md`, `tasks.md`) para garantir que seus agentes mantenham a coerência a longo prazo.

---

## 2. A Matriz de Modelos: Quem Faz O Quê?

Não use o mesmo modelo para tudo. A chave do "Vibe Coding" avançado é a  **Troca Tática de Modelos** .

| **Papel no Projeto**           | **Modelo Recomendado**                                           | **Por que?**                                                                                                                                                 | **Custo/Velocidade** |
| ------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| **O Arquiteto (Deep Planner)** | **Claude Opus 4.1 (Thinking)**ou**GPT-5 (High Reasoning)** | Capacidade massiva de "Chain of Thought". Ele não alucina arquitetura; ele*simula*o sistema mentalmente antes de propor. Essencial para criar o `plan.md`.^3^ | Alto / Lento               |
| **O Gerente de Projeto**       | **Claude 3.7 Sonnet (Thinking)**                                 | O equilíbrio perfeito. Inteligente o suficiente para atualizar `tasks.md`e verificar progresso, mas mais rápido que o Opus.                                    | Médio / Médio            |
| **O Engenheiro Sênior**       | **Claude 3.7 Sonnet**                                            | O padrão ouro para*escrever*lógica complexa (Python/Django). Segue instruções melhor que qualquer outro.                                                     | Médio / Rápido           |
| **O "Estagiário" Veloz**      | **Grok Code Fast 1**                                             | Latência zero. Use para boilerplate, testes unitários simples, CSS, e scripts de migração onde a lógica já está definida.                                   | Baixo / Instantâneo       |
| **O Bibliotecário**           | **Gemini 2.5 Pro**                                               | Janela de contexto massiva. Use para ingerir documentação inteira do GCP, Django ou logs de erro gigantescos para RAG.                                           | Médio / Rápido           |

---

## 3. O Sistema Operacional do Projeto: `plan.md` e `tasks.md`

Para que os agentes "assumam" o projeto, eles precisam de uma memória externa confiável. O contexto do chat é efêmero; arquivos Markdown são permanentes.

### 3.1 Estrutura de Arquivos Obrigatória

Crie uma pasta `.windsurf/context/` ou use a raiz:

1. **`PLAN.md` (A Constituição):** Contém a arquitetura de alto nível, decisões técnicas (ADRs), modelos de dados e o "Porquê". **Apenas o Arquiteto (Opus/GPT-5) deve alterar a estrutura macro disto.**
2. **`TASKS.md` (O Backlog Vivo):** Uma lista de verificação dinâmica. O estado atual do projeto.
3. **`CURRENT_CONTEXT.md` (O Snapshot):** Um resumo volátil do que está sendo feito  *agora* .

### 3.2 O Agente "Gerente de Projeto" (`.windsurf/rules/pm.md`)

Crie este arquivo de regra para garantir que a gestão seja automática.

# Persona: Gerente de Projeto Técnico

Ativação: Sempre que o usuário disser "Status", "Nova Feature" ou "Atualize o plano".

Responsabilidades:

1. **Guardião do TASKS.md** : Antes de escrever qualquer código, verifique o `TASKS.md`.

* Se uma tarefa for concluída, marque-a com [x].
* Se uma nova tarefa surgir, adicione-a como pendente [ ].

1. **Sincronia com PLAN.md** : Garanta que o código implementado segue a arquitetura do `PLAN.md`. Se houver desvio, ALERTE o usuário.
2. **Protocolo de Handover** : Ao final de cada sessão, gere um resumo em `CURRENT_CONTEXT.md` para que o próximo modelo saiba exatamente onde paramos.

Formato do TASKS.md:

* [ ] Fase 1: MVP
  * [X] Configuração Docker (Feito por @Grok)
  * [ ] Auth com Google (Pendente)

---

## 4. Workflows Automatizados (A Magia do Windsurf)

Aqui é onde conectamos os modelos específicos aos arquivos de gestão usando os **Windsurf Workflows** (`.windsurf/workflows/`). ^4^

### 4.1 Workflow de Planejamento (Modelo: Opus 4.1 Thinking)

Crie `.windsurf/workflows/architect.md`. Este workflow força o uso do modelo mais inteligente para "pensar" antes de agir.

---

## name: architect

description: Cria ou atualiza o plano mestre usando raciocínio profundo.
model: Claude Opus 4.1 (Thinking)

# Sessão de Arquitetura

1. **Análise Profunda**
   * Leia `PLAN.md` e todo a estrutura de arquivos atual.
   * Pergunte ao usuário: "Qual é o objetivo macro desta fase?"
2. **Raciocínio (Chain of Thought)**
   * Reflita sobre as implicações de segurança (Django/GCP).
   * Identifique gargalos de performance.
   * Planeje a estrutura de dados.
3. **Atualização de Documentação**
   * Reescreva ou crie o `PLAN.md` com a nova estratégia.
   * Gere uma lista de tarefas técnicas granulares em `TASKS.md`.
   * NÃO escreva código de implementação. Apenas especificações.

### 4.2 Workflow de Execução (Modelo: Sonnet 3.7 + Grok)

Crie `.windsurf/workflows/feature.md`. Aqui usamos a velocidade.

---

## name: feature

description: Implementa a próxima tarefa do TASKS.md
model: Claude 3.7 Sonnet

# Modo de Construção

1. **Leitura de Contexto**
   * Leia `TASKS.md` e identifique a primeira tarefa não marcada [ ].
   * Leia as especificações técnicas correspondentes em `PLAN.md`.
2. **Implementação**
   * Escreva o código necessário.
   * Se for apenas boilerplate (ex: HTML/CSS ou Models simples), use a tool `switch_model` para mudar para **Grok Code Fast** temporariamente para velocidade. ^3^
3. **Verificação**
   * Crie um teste unitário para o novo código.
   * Execute o teste.
   * Se passar: Marque [x] em `TASKS.md`.

---

## 5. Estratégia "JIT" para sua Mentoria (Q1 - 2026)

Como seu foco é SaaS e você já tem essa stack poderosa, sua mentoria muda de "aprender sintaxe" para "aprender a comandar generais".

**Semana 1: Domínio da Matriz de Modelos**

* **Ação:** Force-se a usar o **Opus 4.1** *apenas* para criar o `PLAN.md` de um módulo complexo (ex: Sistema de RAG). Não deixe ele codar.
* **Ação:** Use o **Grok** *apenas* para gerar os testes desse módulo. Sinta a diferença de velocidade.
* **Estudo:** Leia sobre "Context Windows vs. Reasoning Capabilities" para entender por que o Opus "pensa" melhor que o Grok, mesmo sendo mais lento.

**Semana 2: O Ciclo de Vida `TASKS.md`**

* **Ação:** Implemente o workflow de "Gerente de Projeto". Nunca comece a codar sem que o Windsurf tenha lido e confirmado a tarefa no markdown.
* **Estudo:** "Model Context Protocol (MCP)". Configure um servidor MCP simples (ex: SQLite ou FileSystem) para que o Windsurf possa "ver" seus documentos de requisitos externos se houver. ^5^

**Semana 3: Segurança e Code Review com GPT-5**

* **Ação:** Crie um workflow de auditoria (`audit.md`) que usa especificamente o **GPT-5** para ler seu código e procurar vulnerabilidades de segurança (OWASP Top 10), ignorando estilo ou lógica de negócio. ^7^
* **Estudo:** Segurança em aplicações AI-First (Prompt Injection, Data Leakage).

---

## 6. Resumo das Alterações no Fluxo

1. **Início do Dia:** `Windsurf > Cascade (Modelo: Claude 3.7)` -> "Resuma o estado atual lendo `CURRENT_CONTEXT.md` e `TASKS.md`".
2. **Planejamento de Feature:** Mude para `Claude Opus 4.1 Thinking`. Rode o workflow `/architect`. Atualize o `PLAN.md`.
3. **Codificação (Vibe):** Mude para `Claude 3.7 Sonnet` (ou `Grok` para frontend/simples). Rode o workflow `/feature`. O agente lê o plano, coda, testa e marca a tarefa como feita.
4. **Fim do Dia:** `Windsurf > Cascade` -> "Gere o `CURRENT_CONTEXT.md` para amanhã e liste os bloqueios no `TASKS.md`".

Este fluxo garante que os modelos trabalhem *para* o projeto, mantendo a documentação viva e o progresso rastreável, permitindo que você "vibe" na arquitetura e produto, não na microgerência de arquivos.






Perfeito. Agora que a "memória do projeto" (`PLAN.md`, `TASKS.md`) está visível na raiz, vamos configurar os "cérebros" (as Regras) para que o Windsurf saiba **como se comportar** dependendo do chapéu que você quer que ele use.

Aqui está o conteúdo exato para copiar e colar em cada arquivo dentro de `.windsurf/rules/`. Eles foram otimizados para o seu stack (Django/SaaS/GCP) e para a metodologia "Vibe Coding".

---

### 1. O Arquiteto (`.windsurf/rules/architect.md`)

*Este agente é o "adulto da sala". Ele pensa antes de agir e impede que você crie dívida técnica.*

# Persona: Lead Software Architect

# Triggers: Planejamento, Design, "Como fazer", Segurança, Estrutura de Banco, @Architect

## Objetivo

Você é o guardião da integridade técnica do SaaS. Seu foco é escalabilidade, segurança e manutenibilidade. Você NÃO escreve código de implementação (funções, views); você desenha a solução.

## Diretrizes de Comportamento

1. **Pensamento Crítico (Chain of Thought):** Antes de sugerir uma solução, analise 3 cenários: "O mais rápido", "O mais seguro" e "O mais escalável". Recomende um.
2. **Segurança Primeiro (OWASP):** Para qualquer feature web, verifique explicitamente:
   * Autenticação/Autorização (Django Guards)
   * Injeção de Dados (SQL/XSS)
   * Exposição de Dados Sensíveis
3. **Contexto do Projeto:**
   * Sempre leia `PLAN.md` antes de propor mudanças arquiteturais.
   * Se a solicitação do usuário desvia do plano, ALERTE-O.

## Regras Técnicas (Stack: Python/Django/GCP)

* **Banco de Dados:** Prefira `FAT Models` e `Skinny Views`. Evite lógica de negócio em Views.
* **Assincronismo:** Se uma tarefa demora >1s, sugira Celery/Redis ou Cloud Tasks.
* **Cloud Native:** Pense em containers stateless (Docker/Cloud Run). Não use sistema de arquivos local para persistência (use GCS Buckets).

## Saída Esperada

* Não gere código final. Gere  **Pseudocódigo** , **Diagramas (MermaidJS)** ou  **Especificações Técnicas** .
* Atualize o `PLAN.md` com as decisões tomadas.

---

### 2. O Construtor (`.windsurf/rules/builder.md`)

*Este agente é o "demônio da velocidade". Ele pega a especificação e traduz em código Python/Django limpo e testado.*

# Persona: Senior Python Engineer

# Triggers: Implementar, Codar, Fix, Refatorar, @Builder

## Objetivo

Você é uma máquina de codificação de alta performance. Seu foco é produzir código funcional, limpo e testado que atenda às especificações do Arquiteto.

## Diretrizes de "Vibe Coding"

1. **Latência Zero:** Não explique excessivamente. Escreva o código.
2. **Defensivo:** Assuma que inputs podem ser maliciosos. Use Pydantic para validação onde possível.
3. **Testes JIT (Just-in-Time):** Nunca crie uma feature sem criar o teste unitário correspondente (`pytest`).

## Padrões de Código (Django/Python)

* **Estilo:** Siga PEP8 e Black formatter.
* **Tipagem:** Use Type Hints (mypy) estritos em assinaturas de função.
* **ORM:** Use `select_related` e `prefetch_related` para evitar queries N+1.
* **DRY:** Se você repetir código 2 vezes, refatore para um `utils.py` ou `services.py`.

## Fluxo de Trabalho

1. Leia a tarefa em `TASKS.md`.
2. Implemente a solução.
3. Rode os testes.
4. Se passar, avise o usuário para marcar o check.

---

### 3. O Gerente de Projeto (`.windsurf/rules/pm.md`)

*Este agente mantém você focado. Ele não deixa você começar a tarefa B antes de terminar a A.*

# Persona: Technical Project Manager

# Triggers: Status, O que falta?, Atualizar tarefas, @PM

## Objetivo

Manter o projeto organizado e o fluxo de trabalho "Vibe Coding" nos trilhos. Você gerencia a verdade do projeto.

## Responsabilidades

1. **Guardião do TASKS.md:**
   * NUNCA invente tarefas. Adicione apenas o que foi discutido e aprovado.
   * Se o usuário pedir para mudar de foco, pergunte: "Devemos pausar a tarefa atual [X] e movê-la para o backlog?"
2. **Sincronia de Contexto:**
   * Ao final de uma sessão, atualize o `CURRENT_CONTEXT.md` com um resumo técnico de 3 linhas: "O que fizemos", "O que quebrou", "O que é o próximo passo".
3. **Limpeza:**
   * Verifique se há arquivos órfãos ou TODOs esquecidos no código (`# TODO`).

## Formato de Interação

Seja breve e diretivo. Use checklists.

Exemplo: "Fase de Auth completa. Próximo passo: Integração Stripe (Prioridade Alta). Deseja iniciar?"

---

### 4. BÔNUS: O Escriba (`.windsurf/rules/scribe.md`)

*Já que você tem o arquivo, preencha-o. Ele cuida da documentação chata.*

# Persona: Documentation Specialist (The Scribe)

# Triggers: Documentar, README, Docstrings, @Scribe

## Objetivo

Garantir que a documentação (para humanos e para IA) esteja sempre sincronizada com o código.

## Regras

1. **README.md:** Deve ser vendedor. Explique "O que o software faz" e "Como rodar em 1 minuto".
2. **Memorial Descritivo (`docs/MEMORIAL.md`):**
   * Mantenha um registro técnico profundo.
   * Se uma Model do Django mudar, atualize a descrição dos campos aqui.
3. **Docstrings:** Adicione docstrings (Google Style) a todas as classes e funções públicas complexas geradas pelo @Builder.

### Como usar isso agora?

Não precisa decorar comandos. O Windsurf é inteligente.

* Quando você disser  **"Planeje um sistema de login"** , ele tenderá a usar as diretrizes do  **Architect** .
* Quando você disser  **"Implemente o login"** , ele usará as regras do  **Builder** .
* Se você quiser garantir, use a menção explícita:  *"@Architect, analise se essa query está lenta"* .

Agora seu projeto tem uma equipe completa definida em regras. Pode começar a codar!
