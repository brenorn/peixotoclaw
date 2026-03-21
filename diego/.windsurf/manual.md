Este manual é o seu "Livro de Regras" para operar a máquina que construímos. Você não está mais apenas codando; você está gerenciando uma equipe de IA.

Imprima ou mantenha este guia aberto. Ele explica como reger a orquestra que você configurou em `.windsurf`.

---

# 📘 Manual de Operações: Windsurf SaaS Factory

## 1. O Conceito: A "Sala de Reunião"

Você configurou o Windsurf para agir como uma equipe completa de engenharia. Em vez de pedir "crie um código", você delega tarefas para especialistas.

* **Sua Função:** CTO & Product Owner (Você define  *O Quê* ).
* **A Função Deles:** Execução e Gerenciamento (Eles definem  *O Como* ).

---

## 2. As Personas (Quem é Quem)

Localização: .windsurf/rules/

Como usar: O Windsurf tenta adivinhar, mas você deve ser explícito usando @ para melhores resultados.

| **Agente**         | **Arquivo** | **Quando Chamar?**                                                         | **Modelo Recomendado**                 | **Exemplo de Prompt**                                                |
| ------------------------ | ----------------- | -------------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------- |
| **O Arquiteto**    | `architect.md`  | Início de feature, dúvidas de banco de dados, segurança, decisões difíceis. | **Claude Opus 4.1**(Thinking)          | "@Architect, como devemos estruturar o banco para suportar multi-tenancy?" |
| **O Construtor**   | `builder.md`    | Quando o plano já existe e você quer código. É o "operário".                | **Claude 3.7 Sonnet**                  | "@Builder, implemente a View de login conforme o TASKS.md."                |
| **O Gerente (PM)** | `pm.md`         | Quando você está perdido, quer saber o status ou finalizar uma sessão.        | **Claude 3.7 Sonnet**                  | "@PM, o que falta para terminarmos a Fase 1? Atualize o tasks.md."         |
| **O Escriba**      | `scribe.md`     | No final de uma feature, para atualizar docs.                                    | **Gemini 2.5 Pro**(Lê muito contexto) | "@Scribe, gere a documentação técnica da nova API de pagamentos."       |

---

## 3. Os Comandos de Automação (Workflows)

Localização: .windsurf/workflows/

Como usar: Digite / no chat e selecione o comando.

### 🧠 `/architect` (A Sessão de Planejamento)

O que faz: Lê todo o projeto + PLAN.md e gera um plano de batalha para o próximo passo.

Quando rodar:

1. Antes de começar qualquer funcionalidade nova.
2. Quando você sentir que o código está virando "espaguete".
   Resultado: Ele vai atualizar o PLAN.md e encher o TASKS.md de checkboxes.


---

## 4. O Fluxo de Trabalho Diário (The Loop)

Aqui está o roteiro passo-a-passo para sua sessão de  **Vibe Coding** :

### Passo 1: Check-in (Modo PM)

* **Ação:** Abra o Windsurf.
* **Prompt:** "@PM, leia o `CURRENT_CONTEXT.md` e o `TASKS.md`. Onde paramos e qual a prioridade de hoje?"
* **Resultado:** O PM vai te dizer: "Paramos nos testes da Auth. Próximo passo é criar o `test_login.py`."

### Passo 2: Planejamento (Se for algo novo)

* **Ação:** Se a tarefa for complexa (ex: "Criar sistema de RAG").
* **Comando:** Digite `/architect`.
* **Interação:** Converse com o Opus 4.1 até ele atualizar o `PLAN.md` com a estratégia.

### Passo 3: Mão na Massa (Vibe Coding)

* **Ação:** Mude o modelo para **Claude 3.7 Sonnet** (ou **Grok** se quiser velocidade extrema).
* **Prompt:** "@Builder, pegue a primeira tarefa não marcada do `TASKS.md` e implemente. Crie o teste primeiro (TDD)."
* **Dica:** Deixe o Windsurf rodar os comandos de terminal (Turbo Mode). Apenas observe.

### Passo 4: Auditoria e Commit

* **Ação:** O código está pronto e testes passando?
* **Prompt:** "@PM, a tarefa X está pronta. Marque no `TASKS.md`, atualize o `CURRENT_CONTEXT.md` e gere uma mensagem de commit."

---

## 5. Resumo de Manutenção (Dicas de Ouro)

1. **Nunca edite o `TASKS.md` manualmente** se puder evitar. Peça para o @PM fazer isso. Isso mantém o "modelo mental" da IA sincronizado com o arquivo real.
2. **Se a IA alucinar:** Pare. Digite `/architect` e peça para ele "Re-ler o plano e corrigir o rumo". Alucinação geralmente é falta de contexto atualizado.
3. **Documentação é Código:** Trate o `PLAN.md` com o mesmo respeito que trata o `settings.py`. Se o plano estiver errado, o código sairá errado.

Agora você tem uma "empresa" dentro do seu IDE. Use seus funcionários virtuais!
