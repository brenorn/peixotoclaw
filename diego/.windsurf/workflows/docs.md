## name: docs

description: Atualiza a documentação técnica e README
model: Gemini 2.5 Pro

Adote a persona definida em `@scribe.md` (leia este arquivo de regra agora).

# Atualização de Documentação

1. **Leitura Total**
   * Leia todos os arquivos de código na pasta `src/`.
   * Leia o `TASKS.md` para ver o que foi feito recentemente.
   * Ative a persona  **@scribe.md** .
2. **Memorial Descritivo**
   * Atualize `docs/MEMORIAL.md`.
   * Para cada classe/model importante, adicione uma tabela de métodos e suas funções.
3. **README e Contexto**
   * Se houve mudança na instalação ou variáveis de ambiente, atualize o `README.md`.
   * Garanta que a documentação reflete o código real, não o planejado.
