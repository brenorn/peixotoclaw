---
name: pipeline-tester
description: Executa testes de precisão e regressão no pipeline de agentes (Estrategista → Triador → Curador). Use quando o usuário reclamar de resultados faltantes, falsos positivos ou quando quiser validar se uma mudança nos prompts melhorou a acurácia do sistema. Esta skill compara os itens encontrados pelo pipeline com um "Golden Set" de IDs esperados.
---

# Pipeline Tester

Esta skill é responsável por garantir a eficácia do pipeline Arremate.AI através de testes de regressão quantitativos.

## Quando Usar
- Para validar se o Estrategista está gerando descritores que capturam editais conhecidos.
- Para verificar se o Curador está filtrando corretamente itens aprovados manualmente.
- Após alterações nos modelos Pydantic ou Prompts dos agentes.

## Workflow

### 1. Definir Caso de Teste (Golden Set)
Sempre comece identificando o que o usuário esperava ver.
Crie um arquivo em `core/tests/regression/cases/[nome_do_caso].json` com o seguinte formato:

```json
{
  "name": "Instalação TV Cabo RJ",
  "company_description": "Empresa especializada em instalação e manutenção de TV a cabo, antenas e serviços de telecomunicações no Rio de Janeiro.",
  "expected_ids": [
    "29128741000134-1-0000122026",
    "29138385000130-1-0000122026",
    "29138385000130-1-0000112026",
    "42498600000171-1-0010642026",
    "14999490000196-1-0000172026"
  ]
}
```

### 2. Executar o Pipeline de Teste
Utilize o script `scripts/run_regression.py` para rodar o pipeline no modo sandbox (sem persistência no banco real, apenas JSONs de teste).

O script deve:
1. Instanciar o `PipelineOrchestrator`.
2. Injetar a `company_description`.
3. Executar o fluxo completo.
4. Coletar os IDs de editais que chegaram ao estágio de **Curador Aprovado**.

### 3. Analisar Resultados e Gerar Relatório
Compare os `expected_ids` com os `found_ids`.

| Status | ID | Motivo da Falha (se houver) |
| :--- | :--- | :--- |
| ✅ HIT | 12345 | Encontrado e Aprovado |
| ❌ MISS | 67890 | Triador não buscou ou Curador reprovou |
| ⚠️ NEW | 11223 | Oportunidade nova encontrada (não estava no Golden Set) |

### 4. Diagnóstico de Falhas
- **Falha no Estrategista**: Os `expected_ids` não foram encontrados nem no diretório de downloads. Os descritores gerados foram muito específicos ou errados?
- **Falha no Triador**: O item foi baixado mas recebeu score baixo (<100) e não passou para o Curador.
- **Falha no Curador**: O item está no YAML com score 100, mas o Curador reprovou indevidamente.

## Protocolo de Orquestração (Gatekeeping)

Como membro do esquadrão Arremate.AI, você deve seguir o protocolo do `pipeline-maestro`:

1. **Plano de Ação**: Antes de iniciar uma bateria de testes de regressão que consuma muitos recursos ou alterar o "Golden Set", submeta um plano à caixa de entrada do `pipeline-maestro`.
2. **Aprovação**: Aguarde o `APROVADO` antes de disparar o `run_regression.py`.
3. **Travas (Locks)**: Cheque se há trava em `core/tests/regression/cases/` ou nos logs de busca antes de processar.
4. **Notificação**: Ao finalizar o benchmark, envie o relatório para a caixa de entrada do Maestro e atualize o status da atividade.

## Scripts Vinculados
- `scripts/run_regression.py`: Motor de execução de teste.

---
> [!IMPORTANT]
> A integridade técnica do pipeline depende de métricas objetivas. Use esta skill para evitar o "loop de tentativa e erro" manual.
