# Guia de Escrita e Interação (Padrões de Prompt)

Para utilizar esta skill de forma plena, recomenda-se seguir os padrões abaixo:

## Inicialização
- **Comando:** "PipelineMaestro, prepare o esquadrão completo de gestão de projeto."
- **Exemplo Real:** "PipelineMaestro, prepare o esquadrão integrando [@[c:\projetos-python\Arremate.AI\.skills\architecture-guardian] @[c:\projetos-python\Arremate.AI\.skills\autoresearch-diagrams] @[c:\projetos-python\Arremate.AI\.skills\avaliacoes] @[c:\projetos-python\Arremate.AI\.skills\brainstorming] @[c:\projetos-python\Arremate.AI\.skills\documentation-scribe] @[c:\projetos-python\Arremate.AI\.skills\feature-builder] @[c:\projetos-python\Arremate.AI\.skills\pipeline-benchmarker] @[c:\projetos-python\Arremate.AI\.skills\pipeline-tester] @[c:\projetos-python\Arremate.AI\.skills\project-manager] ]."
- **Efeito:** Cria a infraestrutura de pastas e arquivos no diretório `.agent/skills/pipeline-maestro/.antigravity/`.

## Gestão de Tarefas
- **Comando:** "PipelineMaestro, delegue ao **Gerente Tático** a atualização do `TASKS.md`."
- **Efeito:** Registra a atividade como prioridade no `registro_atividades.json`.

## Aprovação de Planos
- **Fluxo:** "Agente, envie o plano -> PipelineMaestro aprova."
- **Efeito:** Garante o gatekeeping sugerido no manual.

## Mensageria
- **Comando:** "Diga ao [PAPEL] que [MENSAGEM]." ou "Avise a todos que [COMUNICADO]."
- **Efeito:** Usa as pastas de comunicação para persistir os diálogos.

## Verificação de Travas
- **Fluxo:** "Checar travas antes de editar."
- **Efeito:** Evita conflitos em multi-agentes paralelos.
