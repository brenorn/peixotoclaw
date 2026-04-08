"""
Gerenciador de Esquadrão SandecoMaestro
========================================
Script para automação do gerenciamento de atividades
e comunicação entre agentes do esquadrão.
"""

import json
import os
import sys
import argparse
import io
from pathlib import Path
from datetime import datetime

# Forçar UTF-8 para evitar problemas com caracteres especiais no Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Local padrão caso nada seja especificado
DEFAULT_SQUAD_PATH = ".antigravity/equipe"


class GerenciadorEsquadrao:
    """Classe responsável por orquestrar toda a infraestrutura
    de comunicação e atividades do esquadrão multi-agente."""

    def __init__(self, squad_dir: str | Path | None = None):
        # Prioridade: 1. Argumento direto, 2. Env Var, 3. Default relativo ao CWD
        env_project = os.getenv("PEIXOTOCLAW_PROJECT_PATH")
        
        if squad_dir:
            base = Path(squad_dir)
        elif env_project:
            base = Path(env_project) / DEFAULT_SQUAD_PATH
        else:
            base = Path(DEFAULT_SQUAD_PATH)

        self._diretorio_base = base
        self._caminho_registro = self._diretorio_base / "registro_atividades.json"
        self._caminho_caixa_entrada = self._diretorio_base / "caixa_entrada"
        self._caminho_travas = self._diretorio_base / "travas"
        self._caminho_aviso_geral = self._diretorio_base / "aviso_geral.msg"

    def preparar_infraestrutura(self) -> None:
        """Monta todas as pastas e arquivos necessários para o esquadrão funcionar."""
        self._caminho_caixa_entrada.mkdir(parents=True, exist_ok=True)
        self._caminho_travas.mkdir(parents=True, exist_ok=True)

        if not self._caminho_registro.exists():
            conteudo_inicial = {"atividades": [], "integrantes": []}
            self._caminho_registro.write_text(
                json.dumps(conteudo_inicial, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )

        if not self._caminho_aviso_geral.exists():
            self._caminho_aviso_geral.write_text("", encoding="utf-8")

        print(f"[OK] Infraestrutura preparada em: {self._diretorio_base}")

    def criar_atividade(
        self,
        titulo: str,
        responsavel: str,
        pre_requisitos: list[int] | None = None,
    ) -> dict:
        """Registra uma nova atividade com suporte a pré-requisitos."""
        dados = self._carregar_registro()

        nova_atividade = {
            "id": len(dados["atividades"]) + 1,
            "titulo": titulo,
            "estado": "PENDENTE",
            "plano_validado": False,
            "responsavel": responsavel,
            "pre_requisitos": pre_requisitos or [],
            "tokens_locais": 0,
            "custo_estimado_nuvem": 0.0,
            "criado_em": datetime.now().isoformat(),
        }

        dados["atividades"].append(nova_atividade)
        self._salvar_registro(dados)

        print(
            f"[OK] Atividade #{nova_atividade['id']} "
            f"({titulo}) atribuída a {responsavel}."
        )
        return nova_atividade

    def comunicado_geral(self, remetente: str, conteudo: str) -> None:
        """Transmite uma mensagem para todos os integrantes do esquadrão."""
        comunicado = {
            "remetente": remetente,
            "categoria": "COMUNICADO_GERAL",
            "conteudo": conteudo,
            "enviado_em": datetime.now().isoformat(),
        }
        with open(self._caminho_aviso_geral, "a", encoding="utf-8") as arquivo:
            arquivo.write(json.dumps(comunicado, ensure_ascii=False) + "\n")

        print(f"[OK] Comunicado geral transmitido por {remetente}.")

    def mensagem_direta(self, remetente: str, destinatario: str, conteudo: str) -> None:
        """Envia uma mensagem à caixa de entrada de um agente específico."""
        mensagem = {
            "remetente": remetente,
            "conteudo": conteudo,
            "enviado_em": datetime.now().isoformat(),
        }
        caminho_destino = self._caminho_caixa_entrada / f"{destinatario}.msg"
        with open(caminho_destino, "a", encoding="utf-8") as arquivo:
            arquivo.write(json.dumps(mensagem, ensure_ascii=False) + "\n")

        print(f"[OK] Mensagem enviada de {remetente} para {destinatario}.")

    def consultar_atividades(self) -> list[dict]:
        """Retorna a lista completa de atividades registradas."""
        dados = self._carregar_registro()
        return dados["atividades"]

    def atualizar_estado(self, id_atividade: int, novo_estado: str) -> None:
        """Atualiza o estado de uma atividade pelo seu ID."""
        dados = self._carregar_registro()

        for atividade in dados["atividades"]:
            if atividade["id"] == id_atividade:
                atividade["estado"] = novo_estado
                self._salvar_registro(dados)
                print(
                    f"[OK] Atividade #{id_atividade} atualizada para estado '{novo_estado}'."
                )
                return

        print(f"[ERRO] Atividade #{id_atividade} não encontrada.")

    def registrar_economia(self, id_atividade: int, tokens: int, preco_por_milhao: float = 15.0) -> None:
        """Calcula e registra a economia gerada ao rodar a tarefa localmente."""
        dados = self._carregar_registro()
        for atividade in dados["atividades"]:
            if atividade["id"] == id_atividade:
                custo = (tokens / 1_000_000) * preco_por_milhao
                atividade["tokens_locais"] = tokens
                atividade["custo_estimado_nuvem"] = round(custo, 4)
                self._salvar_registro(dados)
                print(f"[ECONOMIA] Atividade #{id_atividade}: {tokens} tokens locais = ${custo:.4f} economizados.")
                return

    def _carregar_registro(self) -> dict:
        """Carrega o arquivo de registro de atividades."""
        if not self._caminho_registro.exists():
            return {"atividades": [], "integrantes": []}
        conteudo = self._caminho_registro.read_text(encoding="utf-8")
        return json.loads(conteudo)

    def _salvar_registro(self, dados: dict) -> None:
        """Persiste os dados no arquivo de registro."""
        self._caminho_registro.parent.mkdir(parents=True, exist_ok=True)
        self._caminho_registro.write_text(
            json.dumps(dados, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


def principal():
    """Ponto de entrada para execução via linha de comando."""
    parser = argparse.ArgumentParser(description="Gerenciador de Esquadrão SandecoMaestro")
    parser.add_argument("comando", choices=["iniciar", "criar_atividade", "comunicado_geral", "mensagem_direta", "listar", "atualizar_estado", "registrar_economia"])
    parser.add_argument("--project", help="Caminho base do projeto")
    parser.add_argument("--squad-dir", help="Caminho direto para a pasta da equipe")
    
    # Argumentos posicionais extras dependendo do comando
    parser.add_argument("args", nargs="*", help="Argumentos extras para o comando")

    args = parser.parse_args()

    # Determinar diretório da equipe
    squad_path = args.squad_dir
    if args.project:
        squad_path = Path(args.project) / DEFAULT_SQUAD_PATH

    gerenciador = GerenciadorEsquadrao(squad_dir=squad_path)

    if args.comando == "iniciar":
        gerenciador.preparar_infraestrutura()

    elif args.comando == "criar_atividade":
        if len(args.args) < 2:
            print("Erro: Faltam título e responsável.")
            sys.exit(1)
        titulo = args.args[0]
        responsavel = args.args[1]
        pre_requisitos = []
        if len(args.args) > 2:
            pre_requisitos = [int(p) for p in args.args[2].split(",")]
        gerenciador.criar_atividade(titulo, responsavel, pre_requisitos)

    elif args.comando == "comunicado_geral":
        if len(args.args) < 2:
            print("Erro: Faltam remetente e conteúdo.")
            sys.exit(1)
        gerenciador.comunicado_geral(args.args[0], args.args[1])

    elif args.comando == "mensagem_direta":
        if len(args.args) < 3:
            print("Erro: Faltam remetente, destinatário e conteúdo.")
            sys.exit(1)
        gerenciador.mensagem_direta(args.args[0], args.args[1], args.args[2])

    elif args.comando == "listar":
        atividades = gerenciador.consultar_atividades()
        if not atividades:
            print("Nenhuma atividade registrada.")
        for ativ in atividades:
            print(f"  #{ativ['id']} [{ativ['estado']}] {ativ['titulo']} → {ativ['responsavel']}")

    elif args.comando == "atualizar_estado":
        if len(args.args) < 2:
            print("Erro: Faltam ID e novo estado.")
            sys.exit(1)
        gerenciador.atualizar_estado(int(args.args[0]), args.args[1])

    elif args.comando == "registrar_economia":
        if len(args.args) < 2:
            print("Erro: Faltam ID da atividade e número de tokens.")
            sys.exit(1)
        id_ativ = int(args.args[0])
        tokens = int(args.args[1])
        preco = 15.0
        if len(args.args) > 2:
            preco = float(args.args[2])
        gerenciador.registrar_economia(id_ativ, tokens, preco)


if __name__ == "__main__":
    principal()
