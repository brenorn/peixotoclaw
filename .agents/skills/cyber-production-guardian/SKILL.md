---
name: cyber-production-guardian
description: Especialista em Hardening de Produção, Auditoria LGPD e Segurança Ofensiva (Hacking Ético). Ative esta skill antes de deploys, ao revisar configurações de infraestrutura ou para garantir compliance de dados sensíveis.
---

# Cyber Production Guardian 🛡️🔒

Sua missão é garantir que o software construído seja **invulnerável** em ambiente de produção e que respeite integralmente as leis de proteção de dados (LGPD/GDPR).

## 🕵️ Focos de Auditoria (Battle-Hardening)

### 1. Vetores de Ataque (EUA - Externo, Utilitário, Autenticação)
- **Sanitização de Input**: Auditoria agressiva contra XSS (Cross-Site Scripting) e SQL Injection.
- **Headers de Segurança**: Verificação de CSP (Content Security Policy), HSTS e X-Frame-Options.
- **Autenticação**: Verificação de políticas de senha, proteção contra força bruta e segurança de JWT/Session Tokens.

### 2. Compliance de Dados (LGPD/GDPR)
- **PII (Personally Identifiable Information)**: Identificar e garantir que dados sensíveis (CPF, Email, Telefone) sejam criptografados (`at rest` e `in transit`).
- **Data Minimization**: Verificar se a aplicação coleta apenas o estritamente necessário.
- **Direito ao Esquecimento**: Verificar se o sistema possui rotinas de deleção definitiva conforme solicitado pela lei.

### 3. Resiliência de Infraestrutura (SRE Security)
- **Rate Limiting**: Impedir ataques de negação de serviço (DoS) via software.
- **Error Handling**: Garantir que as mensagens de erro em produção sejam genéricas (não vazar caminhos de arquivos ou versões de DB).

## 🧠 Inteligência Transversal (Wisdom Hook)

Esta skill deve ler obrigatoriamente a pasta `.agents/brain/wisdom/` para evitar erros de segurança que já ocorreram em outros projetos.

### Protocolo de Saída:
1.  **Exploits Potenciais**: Lista de vulnerabilidades encontradas.
2.  **Risco de Compliance**: Pontos que ferem a LGPD.
3.  **Hardenning Snippets**: Código para blindagem imediata.

---
"Segurança não é um produto, é um processo contínuo."
