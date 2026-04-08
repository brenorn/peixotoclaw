# Referência: Spec-Driven Development (SDD) com Codex

> **Fonte**: [Um caminho para usar Spec-Driven Development com Codex](https://mmarcosab.medium.com/um-caminho-para-usar-spec-driven-development-com-codex-ba5f37efa152)
> **Data de Ingestão**: 2026-03-21

---

## 🧠 Filosofia Central
O Spec-Driven Development (SDD) propõe inverter o fluxo tradicional: o foco é a **especificação**. O código é apenas uma consequência da qualidade da spec.

### 🚫 Contra o "Vibe Coding"
- Evita prompts soltos que geram inconsistência.
- Elimina a necessidade da IA "adivinhar" regras.
- Reduz o retrabalho e a dívida técnica acumulada.

---

## ✅ O Fluxo de Trabalho Oficial

### 1. Research (Pesquisa)
- **Ação**: Entender o problema e formar contexto.
- **No Arremate.AI**: Realizado pelas skills `architecture-blueprint-generator` e `autoresearch-diagrams`.

### 2. Spec (Especificação)
- **Ação**: Criar um arquivo Markdown explícito.
- **Conteúdo Obrigatório**:
  - Arquivos a criar/modificar.
  - Estrutura de diretórios.
  - Regras de negócio.
  - Detalhes técnicos e snippets.
- **No Arremate.AI**: Armazenado na pasta `/specs/` seguindo o `TEMPLATE.md`.

### 3. Code (Implementação)
- **Ação**: Usar a spec como prompt único para a IA.
- **No Arremate.AI**: Executado pela skill `feature-builder`.

---

## 🔄 Disciplina de Contexto
- **Limpeza**: É vital que a implementação não arraste o "ruído" da fase de pesquisa.
- **Isolamento**: Cada fase deve ser autocontida.

## 🧱 Estrutura Mental
1. **Pensar** (Research)
2. **Planejar** (Spec)
3. **Executar** (Code)

---

## 📌 Diferencial Arremate.AI
Adicionamos o papel do **Guardian** (Auditoria), que não está no artigo original. No nosso fluxo, a Spec não é apenas um guia, mas um **Contrato Inviolável** validado por um agente auditor antes e depois do código.

> **"IA sem especificação é tentativa e erro. IA com especificação é engenharia."**


Aqui está o conteúdo convertido para **Markdown (.md)** com base no artigo solicitado. Fiz um resumo estruturado fiel às ideias principais (sem copiar integralmente por questões de copyright), pronto para você salvar como arquivo:

---

```md
# Um caminho para usar Spec-Driven Development com Codex

Fonte: https://mmarcosab.medium.com/um-caminho-para-usar-spec-driven-development-com-codex-ba5f37efa152

---

## 🧠 Introdução

O Spec-Driven Development (SDD) propõe inverter o fluxo tradicional de desenvolvimento: em vez de começar pelo código, o foco passa a ser a **especificação**.

Com o uso de IA (como Codex), isso se torna ainda mais poderoso, pois:
- A IA responde melhor quando recebe instruções claras
- Reduz ambiguidade
- Gera código mais consistente

A ideia central: **especificações são o produto principal, código é consequência** :contentReference[oaicite:0]{index=0}

---

## 🚫 Problema do "vibe coding"

No modelo comum:
1. Você escreve um prompt
2. A IA gera código
3. Ajustes são feitos via novos prompts
4. Resultado inconsistente

Problemas:
- Falta de padrão
- Retrabalho constante
- Dificuldade de manutenção

Sem especificação, a IA "adivinha" o que fazer :contentReference[oaicite:1]{index=1}

---

## ✅ Proposta: fluxo Spec-Driven

O workflow sugerido segue etapas claras:

### 1. Research (Pesquisa)

- Entender o problema
- Buscar exemplos
- Explorar soluções

> Objetivo: formar contexto antes de pedir implementação

---

### 2. Spec (Especificação)

Criar um arquivo `Spec.md` contendo:

- Arquivos a criar/modificar
- Estrutura de diretórios
- Regras de negócio
- Detalhes técnicos
- Possíveis trechos de código

Formato recomendado:

```

/caminho/arquivo.py

* Criar função X
* Validar entrada Y
* Retornar Z

```

A spec deve ser **extremamente explícita**.

> Se não for claro, a IA improvisa (e geralmente erra)

---

### 3. Code (Implementação)

Agora sim:

- Enviar a spec como prompt
- Pedir implementação completa

Benefício:
- A IA usa todo o contexto focado
- Menos interferência de histórico
- Código mais alinhado

---

## 🔄 Técnica importante: limpar contexto

Entre cada etapa:

- Limpar conversa (`/clear`)
- Recomeçar com contexto específico

Fluxo ideal:

```

Pesquisa → limpa
Spec → limpa
Implementação → limpa

```

Isso melhora o uso da janela de contexto da IA.

---

## 🧱 Estrutura mental do processo

O ciclo completo fica:

1. Pensar (Research)
2. Planejar (Spec)
3. Executar (Code)

---

## ⚖️ Comparação com outras abordagens

| Abordagem        | Característica |
|------------------|--------------|
| Vibe Coding      | Rápido, caótico |
| TDD              | Focado em testes |
| SDD              | Focado em especificação |

SDD funciona melhor para:
- Projetos maiores
- Sistemas críticos
- Código que precisa escalar

---

## 🚀 Benefícios do SDD

- Menos retrabalho
- Código mais previsível
- Melhor comunicação com IA
- Padronização
- Facilidade de manutenção

Ferramentas como GitHub Spec Kit seguem essa linha :contentReference[oaicite:2]{index=2}

---

## ⚠️ Quando usar (ou não)

Use SDD quando:
- Projeto é complexo
- Vai para produção
- Tem múltiplos desenvolvedores

Não precisa usar quando:
- Protótipos rápidos
- Scripts simples

---

## 🧩 Conclusão

O SDD transforma o papel do desenvolvedor:

> De "quem escreve código" → para "quem escreve especificações"

Com IA, isso é ainda mais relevante.

A qualidade do resultado depende diretamente da qualidade da spec.

---

## 📌 Resumo em uma frase

**"IA sem especificação é tentativa e erro. IA com especificação é engenharia."**

```

---
