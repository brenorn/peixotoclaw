import argparse
import sys
import json
import os
from pathlib import Path
from core import planning_paths, to_posix_path
from state import patch_state, advance_plan, write_initial_state, extract_field
from security import scan_for_injection
from diagnostics import get_system_health, format_pulse_report
from deep_sweep import deep_sweep, format_deep_sweep_report

def main():
    parser = argparse.ArgumentParser(description="PeixotoClaw Monster CLI Orchestrator")
    subparsers = parser.add_subparsers(dest="command", help="Comandos de orquestração")

    # Command: init
    init_parser = subparsers.add_parser("init", help="Inicializa a estrutura .planning")
    init_parser.add_argument("--phase", default="01", help="Fase inicial")
    init_parser.add_argument("--total", default="1", help="Total de planos na fase")

    # Command: state
    state_parser = subparsers.add_parser("state", help="Gerencia o estado do projeto")
    state_parser.add_argument("--get", help="Campo para extrair")
    
    # Command: patch
    patch_parser = subparsers.add_parser("patch", help="Atualiza campos no STATE.md")
    patch_parser.add_argument("--fields", required=True, help="JSON string com campos: {'Status': 'Ready'}")

    # Command: advance
    advance_parser = subparsers.add_parser("advance", help="Avança para o próximo plano")

    # Command: pulse
    pulse_parser = subparsers.add_parser("pulse", help="Exibe o Dashboard de Saúde (Peixoto Heartbeat)")

    # Command: study
    study_parser = subparsers.add_parser("study", help="Realiza a ingestão autônoma de um projeto (Deep Sweep)")
    study_parser.add_argument("path", help="Caminho do projeto para estudo")

    args = parser.parse_args()
    cwd = os.getcwd()

    if args.command == "init":
        plan_dir = planning_paths(cwd)["planning"]
        if not plan_dir.exists():
            plan_dir.mkdir(parents=True, exist_ok=True)
        write_initial_state(cwd, {"phase": args.phase, "total_plans": args.total})
        print(json.dumps({"ok": True, "msg": f"Estrutura .planning inicializada em {cwd}"}))

    elif args.command == "state":
        state_path = planning_paths(cwd)["state"]
        if not state_path.exists():
            print(json.dumps({"ok": False, "error": "STATE.md não encontrado"}))
            return
        
        content = state_path.read_text(encoding="utf-8")
        if args.get:
            value = extract_field(content, args.get)
            print(json.dumps({args.get: value}))
        else:
            print(content)

    elif args.command == "patch":
        try:
            fields = json.loads(args.fields)
            res = patch_state(cwd, fields)
            print(json.dumps(res))
        except Exception as e:
            print(json.dumps({"ok": False, "error": str(e)}))

    elif args.command == "advance":
        res = advance_plan(cwd)
        print(json.dumps(res))

    elif args.command == "pulse":
        health = get_system_health(cwd)
        msg = format_pulse_report(health)
        print(msg)

    elif args.command == "study":
        target = args.path
        res = deep_sweep(target)
        msg = format_deep_sweep_report(res)
        print(msg)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
