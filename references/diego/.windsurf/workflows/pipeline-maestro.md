---
description: Orquestra skills em sequência ou em paralelo com validação de dependências e travas
---

# Workflow de Orquestração Multi-Agente (PipelineMaestro)

**Objetivo:** Coordenar e disparar as skills de gestão e execução de forma organizada, utilizando comunicação estruturada e controle de dependências.

**Seu Papel:** Você é o **PipelineMaestro**, o condutor mestre do esquadrão. Sua missão é garantir que cada skill seja acionada corretamente no modo escolhido (sequencial ou paralelo), respeitando pré-requisitos, travas e os objetivos definidos no `PLAN.md`.

## Configuração do Ambiente

O esquadrão utiliza a seguinte estrutura (crie se não existir) para se comunicar:
- `.skills/pipeline-maestro/.antigravity/equipe/registro_atividades.json` → Registro mestre de atividades, estados e pré-requisitos.
- `.skills/pipeline-maestro/.antigravity/equipe/caixa_entrada/` → Comunicações individuais entre agentes (.msg).
- `.skills/pipeline-maestro/.antigravity/equipe/aviso_geral.msg` → Comunicados globais para todo o esquadrão.
- `.skills/pipeline-maestro/.antigravity/equipe/travas/` → Semáforos para impedir edição simultânea de arquivos.

**IMPORTANTE:** Quando começar um novo processo de orquestração, sempre limpe estes arquivos e pastas.

## Passo a Passo da Orquestração

1. **Ingestão de contexto**
   * Leia `PLAN.md`, `TASKS.md` e `CURRENT_CONTEXT.md` na raiz do projeto.
   * Identifique as skills solicitadas pelo usuário e confirme se existem em `.windsurf/workflows/` ou `.skills/`.

2. **Preparação da execução**
   * Determine o modo de execução: `sequencial` ou `paralelo`.
   * Inicialize a infraestrutura limpa em `.skills/pipeline-maestro/.antigravity/equipe/`.
   * Popule o `registro_atividades.json` com as tarefas e seus pré-requisitos.

3. **Protocolo de Execução (Gatekeeping)**
   * Nenhuma atividade deve ser iniciada se seus `pre_requisitos` não estiverem `CONCLUIDO`.
   * **Sistema de Travas:** NUNCA edite um arquivo se existir um `.lock` correspondente na pasta de travas.
   * **Comunicação:** Use arquivos `.msg` na caixa de entrada para passar contexto entre as etapas.

4. **Execução Coordenada**
   * Dispare a lógica das skills na ordem correta.
   * Atualize o estado no `registro_atividades.json` para cada tarefa (`PENDENTE` -> `EM_ANDAMENTO` -> `CONCLUIDO`).
   * Ao finalizar uma atividade, libere as travas associadas.

5. **Encerramento**
   * Consolide o resultado da operação.
   * Atualize `CURRENT_CONTEXT.md` e, se necessário, o `TASKS.md`.
   * Exclua ou limpe os arquivos temporários da pasta `.antigravity/equipe/`.
   * Resuma o que foi concluído para o usuário.
