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

## Papéis do Esquadrão

1. **Condutor (SandecoMaestro)**: O líder do time. Decompõe o problema, distribui responsabilidades e valida planos de ação.
2. **Projetista**: Define a estrutura e padrões arquiteturais antes da codificação.
3. **Executor**: Realiza atividades técnicas específicas.
4. **Comunicador**: Criação de marca, identidade visual, e design.
5. **Auditor**: Procura falhas, bugs e vulnerabilidades.

## Protocolo de Orquestração Avançada

### 1. Modo de Planejamento (Gatekeeping)
Cada agente deve submeter um **Plano de Ação** à caixa de entrada do Condutor antes de alterações críticas. O Condutor responde com `APROVADO`.

### 2. Sincronização e Pré-requisitos
As atividades em `registro_atividades.json` possuem `pre_requisitos`. Um agente só assume uma tarefa se os pré-requisitos estiverem `CONCLUIDO`.

## Regras de Ouro
- SEMPRE cheque `./.antigravity/equipe/travas/` antes de editar arquivos.
- Ao concluir, libere as travas e atualize o `registro_atividades.json`.

---

Siga as instruções originais do Professor Sandeco para manter o sistema eficiente e eficaz.
