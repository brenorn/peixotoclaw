# Plano "PeixotoClaw Monstro": Transformação em SaaS Factory Multi-Agente

Este plano detalha a migração e evolução da infraestrutura de agentes do PeixotoClaw, integrando os conceitos de Spec-Driven Development (SDD) e as ferramentas do ecossistema HiveHub.

## 🎯 Objetivos
- Transformar o projeto em uma "Orquestra de Agentes".
- Garantir 100% de eficiência no uso de tokens com LessTokens.
- Estabelecer uma "Fonte da Verdade" (PLAN.md) inabalável.

## 🛠️ Mudanças Propostas

### Fase 1: Fundação e Memória Externa
#### [NEW] [PLAN.md](file:///d:/OneDrive/aiproj/PeixotoClaw/PLAN.md)
- Onde residirá a "Constituição" do projeto. Decisões arquiteturais, visão de longo prazo e regras inegociáveis.
#### [NEW] [TASKS.md](file:///d:/OneDrive/aiproj/PeixotoClaw/TASKS.md)
- O backlog tático vivo, sincronizado por agentes.
#### [NEW] [CURRENT_CONTEXT.md](file:///d:/OneDrive/aiproj/PeixotoClaw/CURRENT_CONTEXT.md)
- Snapshot de handover para evitar perda de contexto entre sessões de IA.

---

### Fase 2: Personas e Regras (Migração Diego)
#### [NEW] [architect.md](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/rules/architect.md)
- Adaptado do Diego. Foco em design de Skills e AgentLoop.
#### [NEW] [builder.md](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/rules/builder.md)
- Foco em TypeScript/Python e integração de APIs.
#### [NEW] [pm.md](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/rules/pm.md)
- Gerente de projeto local para manter `TASKS.md` sempre em dia.

---

### Fase 3: Integração HiveHub (Aceleradores)
#### [NEW] [.rulebook/rules/](file:///d:/OneDrive/aiproj/PeixotoClaw/.rulebook/rules/)
- Inicialização do `@hivehub/rulebook` para padronizar regras entre Claude, Cursor e Windsurf.
#### [CONFIG] [.env](file:///d:/OneDrive/aiproj/PeixotoClaw/.env)
- Integração ativa das chaves `LESSTOKEN` nos prompts mestres para compressão automática.

---

### Fase 4: Skills de Elite
#### [COPY] [architecture-guardian](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/skills/architecture-guardian)
- Auditoria de segurança e design.
#### [COPY] [pipeline-maestro](file:///d:/OneDrive/aiproj/PeixotoClaw/.agents/skills/pipeline-maestro)
- Orquestrador central de processos.

## ✅ Plano de Verificação

### Automatizado
- Executar scripts de auditoria de skills para validar as novas regras.
- Validar conectividade com a API LessTokens.

### Manual
- Realizar uma sessão de "/architect" para validar a atualização do `PLAN.md`.
- Observar se o `builder` gera `tests` automáticos via workflows.
