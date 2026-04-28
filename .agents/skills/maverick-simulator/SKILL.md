---
name: maverick-simulator
description: "Simulação industrial holística para prever falhas de segurança, gargalos de produtividade e riscos em fluxos de projeto."
---

# Skill: Maverick Simulator (Simulação Industrial Holística)

Esta skill permite ao agente realizar simulações virtuais de alta fidelidade sobre qualquer fase do projeto, feature ou fluxo de dados. Ela atua como um "Gêmeo Digital" da arquitetura, prevendo falhas de segurança e gargalos de produtividade antes da implementação real.

## 🎯 Gatilhos de Ativação
- "Simule a fase X"
- "Teste de fluxo de informação"
- "Simulação de nova empresa/tenant"
- "Análise de variáveis e conexões"
- "Relatório de produtividade de dev"

## 🛠️ Modos de Operação

### 1. Simulação de Segurança (Hardening Check)
- Simula ataques de Path Traversal, Injeção de Claims e Vazamento de Tenant.
- **Saída**: Score de Resiliência (0-100).

### 2. Simulação de Fluxo (Data Journey)
- Rastreia uma variável desde a entrada (API) até a persistência (DB/Silo).
- Identifica "pontos cegos" de importação ou lógica.

### 3. Simulação de Produtividade (DX - Developer Experience)
- Analisa a complexidade de implementação.
- Identifica se a arquitetura causa retrabalho ou se está seguindo o "Oceano Azul".

## 📋 Template de Relatório: SIMULATION_AUDIT_REPORT.md
Cada simulação deve gerar um documento seguindo este padrão:

# 🧪 Relatório de Simulação: [NOME_DO_CENÁRIO]
**Data:** [DATA] | **Fase Simulada:** [FASE]

### 1. Resumo Executivo
[Breve análise do sucesso/falha da simulação]

### 2. Matriz de Variáveis & Conexões
- **Variável X** -> [Origem] -> [Transformação] -> [Destino]
- **Status da Conexão:** [Estável/Ruidosa/Insegura]

### 3. Análise STO (Estratégico, Tático, Operacional)
- **Segurança:** [Nota 0-10]
- **Produtividade:** [Nota 0-10]
- **Fluxo de Info:** [Nota 0-10]

### 4. Veredito Maverick
[Recomendações de ajuste imediato]
