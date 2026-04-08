---
name: reversa_frontend
description: Engenharia Reversa de Frontends (Mapeamento de Fluxo e Cálculos)
---

# Skill: Reversa Frontend 🦞

Esta skill é especializada em dissecar interfaces (HTML/JS/React) para entender como os dados são capturados, transformados e enviados para o backend.

## 🛠️ Metodologia de Operação

### Fase 1: Scan da Superfície (Python `extractor.py`)
- O script automatizado mapeia todos os elementos de interação (`input`, `button`, `select`).
- Identifica atributos `id`, `name` e `class`.
- Extrai links para arquivos JS externos e estilos CSS.

### Fase 2: Rastreamento de Eventos (Inspecção de Código)
- Busca por `addEventListener`, `onclick`, `handleSubmit`.
- Identifica as funções disparadoras de lógica.

### Fase 3: Motor de Cálculo (Decifrar Lógica)
- Isola os blocos de código que realizam cálculos (ex: somatórios, regras de No-Show, validações de data).
- Traduz a lógica JS para pseudocódigo ou Python para auditoria.

### Fase 4: Mapa de Soberania (Output Final)
Gerar um artefato `mapa_reversa_{NOME_PAGINA}.md` contendo:
- **Variáveis de Entrada**: Origem e formato.
- **Transformações**: Regras de negócio aplicadas.
- **Requisições de Rede**: Endpoints API (POST/GET).
- **Destino DB**: Tabelas alvo (Sincronizado com SchemaRegistry).

## 🚀 Como Usar
Para disparar a skill em uma página:
`@SandecoMaestro execute reversa_frontend em {PATH_PARA_PAGINA}`
