# PeixotoClaw: Lições Aprendidas (Knowledge Base) 🧠

Este documento é o cérebro evolutivo do projeto. Ele DEVE ser consultado por todos os agentes antes de qualquer execução técnica.

## 🏗️ Arquitetura e Portabilidade
- **Caminhos Absolutos (CRITICAL)**: NUNCA usar caminhos fixos como `d:\OneDrive...` ou `c:\projetos...`.
  - **Motivo**: Quebra o projeto ao mover de máquina ou subir para o Git.
  - **Solução**: Usar sempre `path_utils.py` para resolver caminhos relativos à raiz do projeto.

## 🗄️ Banco de Dados (PostgreSQL)
- **Unique Constraints (Work-in-Progress)**: Evitar travas de `user_id` em submissões que precisam ser anônimas ou coletivas.
  - **Motivo**: Impede o fluxo de "Anonimato Total".

## 🤖 Orquestração (Maestro)
- **Ledger Sync**: O `registro_atividades.json` é a fonte da verdade para o estado da equipe.
  - **Solução**: Sempre atualizar o status da tarefa no ledger antes de finalizar o turno.

---
*Gerado via PeixotoClaw Engine - Memória Ativa v1.0*
