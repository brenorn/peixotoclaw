# peixotoclaw (Monster Edition) 🦖

> [!CAUTION]
> **ATENÇÃO IA**: Este projeto utiliza uma arquitetura de Multi-Agentes complexa.
> LEIA O ARQUIVO [**HANDOVER.md**](file:///d:/OneDrive/aiproj/PeixotoClaw/HANDOVER.md) ANTES DE QUALQUER AÇÃO.

---

## 🏗️ Visão Geral
PeixotoClaw é uma plataforma engine para desenvolvimento automatizado de agentes e automação de processos complexos. Controlado exclusivamente via **Telegram**. Ele combina a inteligência de LLMs de ponta (como Gemini 2.0) com a capacidade de interagir diretamente com o seu sistema de arquivos e executar habilidades especializadas.

---

## ⚡ O que você pode fazer com o PeixotoClaw?

Graças ao seu sistema de **Skills (Hot-Reload)** e **Agent Loop (ReAct)**, o PeixotoClaw é mais do que um chatbot; ele é um assistente operacional:

- **💻 Coder**: Peça para ele criar arquivos, refatorar código ou sugerir arquiteturas. Ele pode ler e escrever no seu sistema de arquivos local.
- **📄 Analista de Documentos**: Envie um **PDF** via Telegram e peça um resumo, uma análise de dados ou para extrair informações específicas.
- **🎨 Designer de Brand/Canvas**: Use skills especializadas para gerar diretrizes de marca ou conceitos de design.
- **🔨 MCP Builder**: Construa e gerencie Model Context Protocols diretamente.
- **📂 Gestor de Arquivos**: Peça para ele ler diretórios, organizar logs ou ler arquivos de configuração.
- **🧠 Memória Persistente**: Ele lembra do contexto das suas conversas passadas através de um banco de dados local SQLite.

---

## 🛠️ Configuração e Instalação

### 1. Pré-requisitos
- **Node.js**: v20+ (Recomendado).
- **Telegram Bot Token**: Crie um no [@BotFather](https://t.me/botfather).
- **Google AI Studio Key**: Obtenha sua chave do Gemini em [aistudio.google.com](https://aistudio.google.com/).

### 2. Instalação
```bash
git clone <seu-repositorio> peixotoclaw
cd peixotoclaw
npm install
```

### 3. Configuração (.env)
Crie um arquivo `.env` na raiz:
```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_ALLOWED_USER_IDS=seu_id_telegram
GEMINI_API_KEY=sua_chave_gemini
DEFAULT_PROVIDER=gemini
MAX_ITERATIONS=5
```

---

## 🚀 Como Executar

Para iniciar o bot em modo de desenvolvimento (com auto-reload):
```bash
npm run dev
```

O bot estará pronto assim que você vir `[Telegram] Bot started...` no terminal.

---

## 📂 Habilidades (Skills)

As habilidades são o "cérebro" variável do PeixotoClaw. Elas estão localizadas em `.agents/skills/`. Cada pasta contém um arquivo `SKILL.md` que o bot carrega dinamicamente.

**Habilidades Integradas:**
- `Coder`, `Skill-Creator`, `PDF-Analyzer`, `Webapp-Testing`, e mais 14!

**Para criar uma nova skill:**
Basta criar uma pasta em `.agents/skills/MinhaSkill` e adicionar um arquivo `SKILL.md` com o frontmatter YAML definindo nome e descrição. O bot a reconhecerá instantaneamente sem reiniciar.

---

## 🏗️ Arquitetura

- **Core ReAct**: O bot não apenas responde, ele "pensa" e "age" (Thought -> Action -> Observation).
- **SQLite Database**: Armazenamento local de mensagens e conversas.
- **Provider System**: Facilmente intercambiável entre Gemini, DeepSeek ou outros provedores locais.
- **Multimodal**: Suporte nativo para leitura de PDFs e infraestrutura para Voz e Imagem.

---

---

## 🎖️ Créditos e Agradecimentos

Este projeto é o resultado de uma evolução colaborativa e inspiração técnica. Agradecimentos especiais a:

- **Prof. Sandeco** ([@sandeco](https://github.com/sandeco)): Pela visão mestre, mentoria e por impulsionar os limites da automação com agentes.
- **Diego** ([@eudiegoaragao](https://github.com/eudiegoaragao)): Pela colaboração intensa na pesquisa e no desenvolvimento das bases deste ecossistema.
- **Marcos Silva** ([@mmarcosab](https://github.com/mmarcosab)): Pelas valiosas contribuições teóricas e insights técnicos compartilhados via Medium.

---

**Mantenedor:** Breno Peixoto
**Status:** Alpha v1.0 - PeixotoClaw Monster Ready 🚀🦾
