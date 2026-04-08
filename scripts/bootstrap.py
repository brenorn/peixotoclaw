import os
import shutil
from pathlib import Path

def bootstrap():
    print("================================================================")
    print("          PeixotoClaw: Industrial Bootstrap System             ")
    print("================================================================\n")

    base_dir = Path(__file__).parent.parent.absolute()
    
    # 1. Definir pastas obrigatórias que NÃO sobem para o Git
    required_dirs = [
        "projects",
        "data",
        "temp",
        "references",
        "logs"
    ]

    print(f"[*] Verificando estrutura em: {base_dir}")
    for folder in required_dirs:
        folder_path = base_dir / folder
        if not folder_path.exists():
            print(f"[+] Criando pasta: {folder}/")
            folder_path.mkdir(exist_ok=True)
        else:
            print(f"[OK] Pasta já existe: {folder}/")

    # 2. Setup do arquivo .env
    env_file = base_dir / ".env"
    env_example = base_dir / ".env.example"
    
    if not env_file.exists():
        if env_example.exists():
            print("[+] Inicializando .env a partir do .env.example...")
            shutil.copy(env_example, env_file)
        else:
            print("[!] Aviso: .env.example não encontrado. Criando .env vazio...")
            env_file.touch()
    else:
        print("[OK] Arquivo .env já existe.")

    # 3. Verificação de subpastas críticas
    (base_dir / "projects" / ".antigravity").mkdir(exist_ok=True)
    
    print("\n----------------------------------------------------------------")
    print("✅ Bootstrap concluído com sucesso!")
    print("----------------------------------------------------------------")
    print("[!] Próximos Passos:")
    print("1. Se for a primeira vez, execute: npm install")
    print("2. Configure suas credenciais no arquivo .env")
    print("3. Inicie o sistema pelo peixotoclaw.bat")
    print("================================================================\n")

if __name__ == "__main__":
    bootstrap()
