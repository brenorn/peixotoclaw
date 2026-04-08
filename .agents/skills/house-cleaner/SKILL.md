---
name: house-cleaner
description: 'Especialista em organização e faxina de projetos. Use para reestruturar diretórios, mover arquivos para pastas lógicas (src, data, config, tests, reports), remover duplicidades e garantir a hermeticidade do projeto. Acione sempre que o usuário pedir para "arrumar a casa", "limpar o projeto" ou "organizar os arquivos".'
---

# Skill: House-Cleaner 🧹🏛️

Esta habilidade transforma um diretório bagunçado em uma estrutura de engenharia de elite, seguindo os padrões do PeixotoClaw.

## Protocolo de Execução

### 1. Auditoria de Ativos (Mapeamento)
Identifique a categoria de cada arquivo:
- **src/ (ou core/)**: Lógica principal (.py).
- **config/**: Segredos, tokens e chaves (.json, .pickle, .env).
- **data/**: Bancos de dados e esquemas (.db, .sql, .csv).
- **tests/**: Scripts de prova de conceito, experimentos e tracers.
- **reports/**: Saídas de dados, logs históricos, screenshots e documentos de análise.

### 2. Plano de Movimentação
Antes de mover, apresente uma tabela ao usuário comparando:
| Arquivo Original | Destino Sugerido | Categoria |
| :--- | :--- | :--- |
| `script.py` | `src/script.py` | Código |

### 3. Execução e Refatoração
- Crie as pastas necessárias.
- Mova os arquivos.
- **CRÍTICO**: Atualize os caminhos (paths) dentro dos arquivos Python para que eles continuem encontrando os arquivos de `config/` e `data/`. Use sempre `os.path.join(os.path.dirname(__file__), ...)` para manter a portabilidade.

### 4. Gestão de Resíduos (Protocolo de Duas Etapas)
- **NUNCA APAGUE**: Em vez de `os.remove`, use `shutil.move` para uma pasta oculta `.trash/`.
- **Auditoria de Lixo**: Crie um script `auditor.py` dentro da pasta `.trash/` que compare hashes de duplicidades e verifique referências no código para certificar que o arquivo pode ser futuramente descartado.

---
"O que parece ser lixo pode ser um backup de emergência."
