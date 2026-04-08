---
name: pipeline-benchmarker
description: Analisa criticamente os resultados do pipeline de busca de licitações (Estrategista → Triador → Curador). Use esta skill após uma execução do pipeline para gerar métricas de precisão, identificar falsos positivos/negativos e sugerir ajustes na estratégia de busca.
---

# Pipeline Benchmarker

Você é o validador de qualidade do pipeline de busca de licitações. Sua missão é garantir que o sistema esteja capturando oportunidades genuínas e minimizando ruído.

## Quando Usar
- Após a conclusão de uma busca no lab (ex: `lab_curador.py`).
- Quando o usuário quiser saber se os resultados foram bons.
- Para diagnosticar por que o sistema trouxe "lixo" ou por que perdeu um edital importante.

## Workflow

### 1. Preparação e Ingestão
Localize o diretório de resultados mais recente em `core/tests/jsons_API_PNCP/`.
Exemplo: `20260316_002_cftv_rj/`.

Leia os seguintes arquivos:
- `itens_relevantes_*.yaml`: Contém todos os itens encontrados e seus scores.
- `relatorio_oportunidades_*.txt`: Contem o que o Curador aprovou.
- `logs_pipeline_*.txt`: Contém a estratégia (descritores) usada.

### 2. Análise de Precisão
Analise os itens do YAML comparando com o perfil da empresa (peça a descrição da empresa se não estiver em contexto).

- **Verdadeiros Positivos (TP)**: Itens score 100 que são genuínos.
- **Falsos Positivos (FP)**: Itens score 100 que são irrelevantes (ruído).
- **Falsos Negativos (FN)**: Itens score 50 (ou menos) que deveriam ser 100 (oportunidades perdidas).
- **Verdadeiros Negativos (TN)**: Itens score 50 que são realmente irrelevantes.

### 3. Métricas
Calcule as métricas:
- **Precisão (Precision)**: TP / (TP + FP)
- **Taxa de Ruído**: FP / Total de itens analisados
- **Recall Estimado**: TP / (TP + FN)

### 4. Diagnóstico Estratégico
- **Descritores**: Os 5 termos principais foram eficazes ou trouxeram muito lixo?
- **Filtro Negativo**: Quais palavras faltam na `negative_keywords`?
- **Sinalização**: O Triador errou o score por falta de tokens ou contexto?

## Output Esperado

Crie um artefato `.md` no diretório da busca chamado `benchmark_analysis.md`.

### Estrutura do Relatório:

# Benchmark: [Nome da Busca]

## 1. Resumo Executivo
- **Score Geral**: [1-10]
- **Veredito**: [Excelente / Bom / Precisa de Ajustes / Crítico]

## 2. Métricas Quantitativas
| Métrica | Valor |
|---------|-------|
| Total Itens Encontrados | [N] |
| Itens Genuínos (TP) | [N] |
| Falsos Positivos (FP) | [N] |
| Precisão | [%] |

## 3. Top Achados (Oportunidades Reais)
- [Edital/Órgão]: [Descrição curta] (Score: [N])

## 4. Análise de Erros (Falsos Positivos)
- [Termo problemático]: "Explicar por que trouxe lixo e qual palavra-chave foi a culpada".

## 5. Recomendações Acionáveis
- **Ajuste de Keywords**: [Remover X, Adicionar Y]
- **Negative Keywords**: [Incluir termos Z]
- **Threshold**: [Aumentar/Diminuir rigor]

## Protocolo de Orquestração (Feedback Loop)

Você alimenta a inteligência do esquadrão:

1. **Plano de Ação**: Notifique o `pipeline-maestro` antes de iniciar a análise de um novo lote de busca.
2. **Registro de Alerta**: Se identificar `Falsos Negativos` críticos, envie uma mensagem direta ao `architecture-guardian` via `caixa_entrada` do maestro.
3. **Travas (Locks)**: Respeite as travas do `pipeline-tester` em `core/tests/regression/`.

---
> [!TIP]
> Use esta análise para ajustar o Agente Estrategista na próxima iteração.
