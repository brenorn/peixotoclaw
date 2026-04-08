---
name: pipeline-maestro
description: 'Executa uma lista de skills em sequência ou em paralelo conforme a necessidade informada pelo usuário.'
argument-hint: 'lista de skills separadas por vírgula, ex: help, brainstorming'
---

# Skill: pipeline-maestro (Orquestração Multi-Agente)

Esta habilidade permite ao Windsurf coordenar um esquadrão de agentes inteligentes atuando de forma simultânea no mesmo projeto, reproduzindo a lógica de "Times de Agentes" em ambientes colaborativos.

## Configuração do Ambiente

O esquadrão utiliza uma pasta oculta dentro do diretório desta skill para se comunicar:

.agent/skills/pipeline-maestro/.antigravity/equipe/registro_atividades.json → Registro mestre de atividades, estados e pré-requisitos.
.agent/skills/pipeline-maestro/.antigravity/equipe/caixa_entrada/ → Comunicações individuais entre agentes (.msg).
.agent/skills/pipeline-maestro/.antigravity/equipe/aviso_geral.msg → Comunicados globais para todo o esquadrão.
.agent/skills/pipeline-maestro/.antigravity/equipe/travas/ → Semáforos para impedir edição simultânea de arquivos.

# IMPORTANTE
1. Nunca crie uma nova pasta `.antigravity` na raiz do projeto.
Utilize a pasta `.antigravity` que fica dentro do diretório desta skill (`.agent/skills/pipeline-maestro/.antigravity/`).
2. Quando começar um novo processo de orquestração sempre limpe 
- registro_atividades.json
- aviso_geral.msg
- travas 
- caixa_entrada

## Papéis do Esquadrão (Squad Arremate.AI)

1. **Orquestrador Mestre (pipeline-maestro)**: O condutor. Inicializa a infraestrutura, coordena a comunicação e resolve conflitos de precedência.
2. **Gerente Tático (project-manager)**: O guardião do `TASKS.md` e `CURRENT_CONTEXT.md`. Foca em progresso, priorização e bloqueio de scope creep.
3. **Guardião da Arquitetura (architecture-guardian)**: Garante conformidade com o `PLAN.md` e regras de segurança (OWASP). Atua como auditor de design.
4. **Projetista de Pesquisa (autoresearch-diagrams)**: Realiza pesquisas técnicas aprofundadas e gera diagramas MermaidJS para visualização de sistemas.
5. **Estrategista Criativo (brainstorming)**: Líder de ideação. Resolve impasses técnicos através de propostas inovadoras e fluxos lógicos.
6. **Escriba de Documentação (documentation-scribe)**: Mantém logs de decisão (ADRs), manuais técnicos e documentação de código sempre atualizados.
7. **Construtor de Features (feature-builder)**: O executor técnico. Implementação de código JIT, refatoração e criação de novas funcionalidades.
8. **Testador de Regressão (pipeline-tester)**: Automatiza a execução de testes contra o "Golden Set" e valida a estabilidade do pipeline.
9. **Benchmarker de Performance (pipeline-benchmarker)**: Analisa métricas de acurácia (precisão/recall) e gera relatórios de melhoria do pipeline.
10. **Avaliador de Qualidade (avaliacoes)**: Audita os resultados finais sob a ótica da experiência do usuário e critérios de aceitação.
11. **Otimizador de Heurísticas (heuristic-optimizer)**: Especialista em sintonia fina das heurísticas do sistema. Analisa e calibra regras do Triador e Curador para combater falsos positivos (identificando muito) e falsos negativos (cegueira heurística).
12. **Especialista Frontend (django-tailwind-expert)**: Desenvolve e aprimora interfaces de usuário modernas e responsivas utilizando Django Template Language (DTL) e a biblioteca utility-first Tailwind CSS.
13. **Escriba de Commits (commit-scribe)**: O cronista do histórico. Analisa o progresso oficial em `PLAN.md`, `TASKS.md` e `specs/` cruzando com os deltas físicos do Git para gerar mensagens de commit precisas e conformes (Conventional Commits).
14. **Especialista Django DB (django-db-specialist)**: O arquiteto de dados. Foca em Schema design em Django + Postgres, garantindo Fat Models, Skinny Views e integração Cloud-Native (GCS Buckets).

## Protocolo de Orquestração Avançada

### 1. Modo de Planejamento (Gatekeeping)

Antes de efetuar alterações relevantes, cada agente deve submeter um **Plano de Ação** à caixa de entrada do PipelineMaestro.

- O agente permanece em modo `SOMENTE_LEITURA` ou `PLANEJAMENTO` até que o PipelineMaestro responda com um comunicado de `APROVADO`.

### 2. Comunicação e Difusão (Broadcast)

- **Comunicação Direta**: Coordenação 1-a-1 entre executores.
- **Comunicado Geral**: PipelineMaestro pode escrever em `aviso_geral.msg` para transmitir novas orientações a todo o esquadrão simultaneamente.

### 3. Sincronização de Atividades e Pré-requisitos

- As atividades em `registro_atividades.json` podem conter uma lista de `pre_requisitos`. Um agente não deve assumir uma atividade se seus pré-requisitos não estiverem com estado `CONCLUIDO`.

- Ao finalizar uma atividade, o agente deve liberar suas "travas" e notificar o PipelineMaestro.

### 4. Spec-Driven Gatekeeping (NO SPEC, NO CODE)
- **Bloqueio do Construtor**: O `feature-builder` está terminantemente proibido de iniciar qualquer implementação sem que o `architecture-blueprint-generator` tenha criado uma SPEC em `/specs/` e o `architecture-guardian` a tenha marcado como `SPEC_APPROVED` no `registro_atividades.json`.
- **Precedência de Atividade**: O Maestro deve priorizar a tarefa de "Arquitetura/Design" (blueprint) antes da "Implementação" (builder) para toda nova feature.

---

Siga as instruções em `./workflow.md` e os padrões de prompt em `./USO.md`.
