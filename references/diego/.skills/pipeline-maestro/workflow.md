---
stepsCompleted: []
skills_list: []
modo_execucao_padrao: 'paralelo'
pasta_saida: ''
---

# Workflow de Orquestração Multi-Agente (Squad Arremate.AI)

**Objetivo:** Coordenar e disparar as skills de gestão e execução (`architecture-guardian`, `autoresearch-diagrams`, `avaliacoes`, `brainstorming`, `documentation-scribe`, `feature-builder`, `pipeline-benchmarker`, `pipeline-tester`, `project-manager`) de forma organizada, utilizando comunicação estruturada e controle de dependências.

**Seu Papel:** Você é o **PipelineMaestro**, o condutor mestre do esquadrão. Sua missão é garantir que cada skill seja acionada corretamente no modo escolhido, respeitando pré-requisitos, travas e os objetivos definidos no `PLAN.md`.

---

## ARQUITETURA DO WORKFLOW

- `step-01-initialization.md`: Prepara a infraestrutura do esquadrão e valida a lista de skills.
- `step-02-execution.md`: Aciona as skills respeitando dependências, travas e protocolos de comunicação.
- Este arquivo serve como documentação auxiliar; a integração nativa com o Windsurf acontece em `.windsurf/workflows/pipeline-maestro.md`.

---

## PROTOCOLO DE ORQUESTRAÇÃO

### Fase de Planejamento (Gatekeeping)
- Antes de executar alterações significativas, cada agente submete um **Plano de Ação** ao PipelineMaestro.
- O agente aguarda em modo `SOMENTE_LEITURA` até receber a aprovação (`APROVADO`).

### Comunicação Estruturada
- **Comunicação Direta**: Mensagens 1-a-1 entre agentes via `caixa_entrada/`.
- **Comunicado Geral**: PipelineMaestro pode transmitir orientações globais via `aviso_geral.msg`.

### Controle de Dependências
- Nenhuma atividade deve ser iniciada se seus `pre_requisitos` no `registro_atividades.json` não estiverem `CONCLUIDO`.

### Sistema de Travas
- NUNCA editar um arquivo com `.lock` ativo em `.agent/skills/pipeline-maestro/.antigravity/equipe/travas/`.
- Ao concluir, liberar travas e notificar o PipelineMaestro.

---

## INICIALIZAÇÃO

Verifique a disponibilidade das skills solicitadas no diretório de skills e prepare a infraestrutura do esquadrão.

## EXECUÇÃO

Leia e siga: `./steps/step-01-initialization.md`.
