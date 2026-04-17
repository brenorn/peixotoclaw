# Arquitetura: PeixotoClaw Engine vs. Projetos Específicos

Para resolver a sua dúvida e evitar o "vazamento de contexto", devemos adotar o modelo de **Plataforma de Agentes**.

---

## 🏗️ 1. PeixotoClaw CORE (O Motor Genérico)
O foco desta pasta raiz é ser o framework. Nada de regras de negócio específicas (como "anônimo na NR01") deve viver aqui.

- **`.agents/rules/`**: Personas genéricas (Arquiteto, Construtor, PM). Eles sabem "como" trabalhar, mas não "o que" é o negócio.
- **`.agents/skills/`**: Ferramentas universais (Manipulação de Excel, PDF, Brainstorming, Auditoria).
- **`.rulebook/rules/`**: Leis universais de qualidade e SDD.
- **`PLAN.md`**: A visão estratégica da **Plataforma PeixotoClaw**.

## 📁 2. Pasta `projects/` (Contextos Específicos)
Cada projeto que o PeixotoClaw gerencia deve ter sua própria subpasta com suas próprias regras de negócio e lore.

Exemplo de Estrutura:
```text
PeixotoClaw/ (Root - Genérico)
├── projects/
│   ├── nr01-anonymity/     <-- Lore específica do projeto NR01
│   │   ├── rules/          <-- Regras de negócio da NR01
│   │   ├── TASKS.md        <-- Backlog da NR01
│   │   └── PLAN.md         <-- Roadmap da NR01
│   └── outro-projeto/
```

## 🧠 3. Como a IA deve agir?
Ao iniciar uma tarefa, o usuário (ou o PM) deve dizer:
*"@PM, vamos trabalhar no projeto `projects/nr01-anonymity`."*

O agente então:
1.  Carrega as **Persona Rules** (Genéricas).
2.  Carrega o **Contexto do Projeto** (Específico).
3.  Usa o **LessTokens** para ler as regras locais sem "sujar" o motor genérico.

---

### ✅ Conclusão
O `nr01-dev-loop` que vimos na sua pasta original provavelmente foi uma tentativa de automatizar esse projeto específico, mas no "PeixotoClaw Monstro", vamos separar a **Igreja do Estado**:
- **PeixotoClaw**: É o sistema operacional de agentes.
- **Projetos (NR01, etc.)**: São os aplicativos rodando nele.

Concorda com essa separação de pastas e responsabilidades?
