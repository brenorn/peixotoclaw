# METADATA_MASTER (SSOT - Single Source of Truth)

## Entidades Core
| Entidade | Tabela (DB) | Descrição |
| :--- | :--- | :--- |
| Usuário | `usuarios` | Tabela principal de dados de usuários. |
| Perfil | `perfis_usuarios` | Detalhes estendidos do perfil do usuário. |
| Pedido | `pedidos` | Registro de transações. |

## Atributos Canônicos (snake_case)
| Atributo | Descrição | Regra |
| :--- | :--- | :--- |
| `id_usuario` | Chave primária do usuário. | UUID |
| `vlr_total` | Valor total da venda/pedido. | Decimal(10,2) |
| `dt_criacao` | Data de criação do registro. | TIMESTAMP |

## Convenções de Código
- **Backend**: Python/FastAPI (snake_case).
- **Frontend**: React/TypeScript (camelCase para variáveis locais, PascalCase para Componentes).
- **Imports**: Sem `*`. Sempre explícitos.
