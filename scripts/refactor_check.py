import os
import subprocess
import sys

def check_broken_references(old_string, project_root):
    """Procura por referências a nomes antigos ou caminhos antigos no projeto."""
    print(f"🔍 [REFACTOR-CHECK] Verificando referências perdidas para: '{old_string}'...")
    
    # Ignorar pastas de sistema e venv
    exclude_dirs = [".git", ".agents", "venv", "__pycache__", "node_modules", "dist", "build"]
    
    findings = []
    try:
        # Usando ripgrep (rg) se disponível, senão fallback para grep nativo
        # No Windows, usamos o git-grep ou findstr, mas aqui usaremos uma busca python para estabilidade
        for root, dirs, files in os.walk(project_root):
            # Filtrar pastas ignoradas
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.tsx', '.html', '.css', '.md')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            for i, line in enumerate(f, 1):
                                if old_string in line:
                                    findings.append(f"{file_path}:{i} -> {line.strip()}")
                    except:
                        continue
    except Exception as e:
        print(f"❌ Erro durante a busca: {e}")

    if findings:
        print(f"\n⚠️  [ATENÇÃO] Foram encontradas {len(findings)} referências que podem estar quebradas:")
        for f in findings[:20]: # Mostrar apenas as primeiras 20 para não poluir
            print(f"  {f}")
        if len(findings) > 20:
            print(f"  ... e mais {len(findings) - 20} ocorrências.")
        return False
    else:
        print(f"✅ Nenhuma referência ao termo '{old_string}' encontrada. Limpeza completa!")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python refactor_check.py [termo_antigo] [caminho_projeto]")
        sys.exit(1)
    
    old_term = sys.argv[1]
    path = sys.argv[2]
    check_broken_references(old_term, path)
