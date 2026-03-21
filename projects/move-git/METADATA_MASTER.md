# Move-Git: METADATA_MASTER.md (SSOT) 💎

Este arquivo é a verdade absoluta sobre a nomenclatura e estrutura do projeto.

---

## 🛣️ Rotas de API (Backend)
| Rota | Método | Função | Arquivo Origem |
| :--- | :--- | :--- | :--- |
| `/full-report` | GET | Gera o relatório completo | `routes/fullReportRoutes.js` |
| `/report-status` | GET | Verifica status da geração | `routes/reportStatusRoutes.js` |
| `/course-share` | POST | Compartilha recomendação | `routes/courseShareRoutes.js` |

## 🗄️ Tabelas de Banco de Dados (Schema)
| Tabela | Coluna Chave | Descrição |
| :--- | :--- | :--- |
| `submissoes` | `id` | Registro de respostas NR01/Competência |
| `usuarios` | `id_usuario` | Cadastro mestre de usuários |
| `competencias_resul`| `id_resultado`| Resultados processados do Capítulo 3 |

## 🐍 Variáveis & Constantes Core (Python)
- **`user_context`**: Dicionário mestre de contexto passado entre capítulos.
- **`ChapterResult`**: Classe de retorno obrigatória para todos os Chapters.
- **`MOVE_PROFILE`**: Estrutura contendo `(M, O, V, E)`.

---
> [!IMPORTANT]
> Se encontrar uma rota ou tabela não listada aqui, sua primeira tarefa é ADICIONÁ-LA a este arquivo.
