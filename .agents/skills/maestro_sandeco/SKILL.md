---
name: sandeco-maestro
description: 'Executa uma lista de skills em sequência ou em paralelo conforme a necessidade informada pelo usuário.'
argument-hint: 'lista de skills separadas por vírgula, ex: help, brainstorming'
---

# Skill: SandecoMaestro (Orquestração Multi-Agente Global)

Esta habilidade permite ao Antigravity coordenar um esquadrão de agentes inteligentes atuando de forma simultânea no mesmo projeto, reproduzindo a lógica de "Times de Agentes" em ambientes colaborativos.

## Configuração do Ambiente (RAIZ DO PROJETO)

Diferente de skills locais, o Maestro opera na **RAIZ do projeto** para garantir que todos os agentes (arquitetos, executores, auditores) compartilhem o mesmo contexto:

- `./.antigravity/equipe/registro_atividades.json` → Registro mestre de atividades, estados e pré-requisitos.
- `./.antigravity/equipe/caixa_entrada/` → Comunicações individuais entre agentes (.msg).
- `./.antigravity/equipe/aviso_geral.msg` → Comunicados globais para todo o esquadrão.
- `./.antigravity/equipe/travas/` → Semáforos para impedir edição simultânea de arquivos.

## Papéis do Esquadrão (SQUAD PEIXOTOCLAW)

1.  **Orquestrador Mestre (SandecoMaestro)**: O condutor. Inicializa a infraestrutura, coordena a comunicação e resolve conflitos.
2.  **Gerente Tático (project-manager)**: Guardião do `TASKS.md` e `CURRENT_CONTEXT.md`. Foca em progresso e priorização.
3.  **Guardião da Arquitetura (architecture-guardian)**: Garante conformidade com o `PLAN.md` e regras de segurança.
4.  **Projetista de Pesquisa (autoresearch-diagrams)**: Pesquisas técnicas aprofundadas e diagramas MermaidJS.
5.  **Estrategista Criativo (brainstorming)**: Líder de ideação e resolução de impasses técnicos.
6.  **Escriba de Documentação (documentation-scribe)**: Mantém logs de decisão (ADRs), memoriais descritivos e READMEs.
7.  **Construtor de Features (feature-builder)**: Implementação técnica, refatoração e novas funcionalidades.
8.  **Testador de Regressão (pipeline-tester)**: Validação de estabilidade e execução contra o Golden Set.
9.  **Benchmarker de Performance (pipeline-benchmarker)**: Analisa métricas de precisão e gera relatórios de melhoria.
10. **Avaliador de Qualidade (avaliacoes)**: Auditor de UX/UI e critérios de aceitação final.
11. **Otimizador de Heurísticas (heuristic-optimizer)**: Sintonia fina das regras de triagem e curadoria de IA.
12. **Especialista Frontend (django-tailwind-expert)**: Desenvolvimento de interfaces modernas com DTL e Tailwind CSS.
13. **Escriba de Commits (commit-scribe)**: Gera mensagens de commit precisas (Conventional Commits).
14. **Especialista Django DB (django-db-specialist)**: Arquiteto de dados (Schema design, Postgres, Cloud-Native).

## Protocolo de Orquestração Avançada

### 1. Modo de Planejamento (Gatekeeping)
Cada agente deve submeter um **Plano de Ação** à caixa de entrada do Condutor antes de alterações críticas. O Condutor responde com `APROVADO`.

### 2. Sincronização e Pré-requisitos
As atividades em `registro_atividades.json` possuem `pre_requisitos`. Um agente só assume uma tarefa se os pré-requisitos estiverem `CONCLUIDO`.

### 3. Spec-Driven Gatekeeping (NO SPEC, NO CODE)
O `feature-builder` não deve iniciar implementação sem uma SPEC aprovada em `/specs/` pelo `architecture-guardian`.

## Regras de Ouro
- SEMPRE cheque `./.antigravity/equipe/travas/` antes de editar arquivos.
- Ao concluir, libere as travas e atualize o `registro_atividades.json`.

---

Siga as instruções originais do Professor Sandeco para manter o sistema eficiente e eficaz.
