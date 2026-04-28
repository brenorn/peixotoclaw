---
name: gsd-engine
description: Motor de execução incremental e anti-congelamento. Use quando lidar com arquivos grandes (>300 linhas), projetos legados complexos ou fases de planejamento extensas. Garante que cada descoberta seja registrada imediatamente, evitando perda de contexto.
---

# GSD-Engine (Get Shit Done) 🦾🚀

Esta habilidade força o assistente a trabalhar em modo **"Bit-Stream"**, garantindo que o progresso seja registrado em tempo real e o contexto nunca sature.

## 🧱 Regra 1: Janela de Audição (Máx 300)
- **Bloqueio de Leitura**: NUNCA tente ler mais de 300 linhas de um arquivo de uma só vez.
- **Protocolo**: Leia 1-300 -> Faça um sumário no `discovery_stream.md` do módulo -> Leia 301-600.
- **Objetivo**: Manter a "RAM" da IA limpa.

## 🍞 Regra 2: Trilha de Migalhas (Logs Imediatos)
- **Registro em Tempo Real**: Toda vez que usar uma ferramenta de busca (`grep`, `ls`, `read`), escreva 1 frase sobre o que aprendeu no arquivo `_peixotoclaw/discovery_stream.md`.
- **Exemplo**: *"Grep encontrou que a variável X é exportada pelo arquivo Y"*.
- **Benefício**: Se a sessão expirar ou travar, o plano de ataque está salvo no disco.

## 🧩 Regra 3: Planejamento por Peças
- **Não planeje o Monolito**: Quebre o planejamento em arquivos específicos por domínio.
- **Exemplos**: `2026_04_21_DOMAIN_MODELS.md`, `2026_04_21_API_CONTRACTS.md`.
- **Fluxo**: Complete uma peça, registre como "Concluída" e limpe o contexto antes de ir para a próxima.

## ⚠️ Anti-Alucinação
- Se você perceber que está repetindo as mesmas perguntas ou se sentindo "perdido", PARE.
- Leia o `discovery_stream.md` local para se re-orientar.
- Não prossiga se houver dúvida; peça clarificação para o usuário com base nas migalhas já coletadas.

---
"O segredo do progresso é começar. O segredo de começar é quebrar suas tarefas complexas e esmagadoras em tarefas pequenas e gerenciáveis, e então começar pela primeira."
