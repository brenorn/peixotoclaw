# Move-Git: Estratégia de Fatiamento (Monocode → Modular) 🔪📦

Para fatiar o código do Move-Git com **eficiência e eficácia**, utilizaremos a skill **`sandeco-maestro`** como orquestradora.

## 🎭 O Esquadrão Maestro
Não trabalharemos sozinhos. Invocaremos um time especializado:

1.  **📊 Explorador (@Scribe/Architect)**: Estuda o "Estado da Arte" e identifica os pontos de acoplamento (onde o código está "embolado").
2.  **📐 Projetista (@Architect)**: Desenha as novas fronteiras. Define o que vira um serviço e o que vira uma utilidade.
3.  **⚡ Executor (@Builder)**: Realiza o fatiamento técnico, move arquivos e ajusta os `imports`.
4.  **🕵️ Auditor (@QA)**: Garante que o `METADATA_MASTER.md` não foi violado e que as rotas continuam funcionando.

## 🔄 Fluxo de Trabalho (Passo a Passo)

### Passo 1: O Chamado
O usuário (você) dá a ordem:
> *"@PM, o projeto Move-Git está muito grande. Use o `Maestro Sandeco` para fatiar o módulo de Competência em sub-módulos `logic`, `prompts` e `api`."*

### Passo 2: O Planejamento Squad
O `SandecoMaestro` inicializa a pasta `.antigravity/equipe/` e distribui as tarefas:
- **Explorador**: lista todos os arquivos que citam "competencia".
- **Projetista**: cria o `projects/move-git/specs/modular_structure.md`.

### Passo 3: O Corte (Cenário Seguro)
O **Executor** move o código. Seguindo a **Regra 050**, ele não pode renomear nada sem que o **Auditor** valide.

### Passo 4: Validação Final
O time de QA roda os testes e o `Maestro` entrega o relatório final: *"Módulo fatiado: 100% de integridade mantida."*

---

## 🚀 Como isso resolve o seu problema?
1.  **Distribuição de Carga**: Diferentes "mentes" de IA cuidam de diferentes partes da refatoração.
2.  **Travas de Segurança**: O Maestro usa `travas/` para impedir que um agente mude um arquivo enquanto o outro está lendo.
3.  **Memória de Grupo**: O `registro_atividades.json` garante que ninguém alucine ou refaça o trabalho do outro.

---
> [!TIP]
> O `Maestro Sandeco` não roda no "start" do projeto porque ele é "Artilharia Pesada". Use-o apenas para grandes mudanças estruturais.
