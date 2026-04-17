# 🌐 PeixotoClaw Multi-Tenant Maestro (MTM) Specification

## 1. O Problema: Contenção de Estado
Atualmente, o PeixotoClaw utiliza um ponto único de falha (`CURRENT_CONTEXT.md` na raiz) para rastrear o estado de todas as sessões. Quando múltiplas instâncias (janelas do VS Code) tentam atualizar este arquivo simultaneamente, ocorrem erros de permissão e perda de dados.

## 2. A Solução: Arquitetura Hub & Spokes (Eixo e Raios)
Descentralizar o estado, movendo a autoridade do contexto para dentro dos diretórios dos **Projetos Satélites**.

### 2.1 Estrutura de Contexto Descentralizada
- **Raiz (Hub)**: `PeixotoClaw/MASTER_LEDGER.log` (Append-only, não bloqueante).
- **Projetos (Spokes)**: `projects/<project_id>/.antigravity/CONTEXT.md`.

### 2.2 Regras de Precedência (Handover v2)
Ao iniciar uma sessão, o Agente deve:
1.  **Detectar o Satélite Ativo**: Verificar se o arquivo atual pertence a um subdiretório em `projects/`.
2.  **Carga de Contexto Local**: Se detectado, ler primeiro `projects/<project_id>/.antigravity/CONTEXT.md`.
3.  **Snapshot Local**: Durante a finalização, o Agente **NÃO** tenta atualizar o root se houver erro; ele persiste o snapshot localmente no projeto satélite.

## 3. Implementação Técnica

### 3.1 Identificador de Sessão (UUID)
Cada janela/conversa terá um `SESSION_ID` único. Logs de depuração serão salvos em `.agents/logs/sessions/<SESSION_ID>.log` para evitar conflitos de escrita no log principal.

### 3.2 Sincronização Assíncrona (O Maestro Background)
Um script servidor (opcional) ou uma rotina de `maestro_sync` consolidará os contextos locais no `MASTER_INDEX.md` da raiz apenas quando solicitado explicitamente, evitando locks durante o desenvolvimento ativo.

## 4. Impacto para o Usuário
O usuário poderá ter 10 janelas do VS Code abertas (Ex: `NR01`, `Clínica Mind`, `Doutorado`) e cada uma terá um PeixotoClaw focado exclusivamente naquele domínio, sem interferência mútua.

---
*Status: Proposto | Autor: @Architect*
