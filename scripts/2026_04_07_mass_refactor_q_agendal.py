import os

# CONFIGURAÇÃO DE ALVOS (Nexus v3.0)
PROJECT_PATH = r'd:\OneDrive\aiproj\mind\vpn_mind\src'
TARGET = 'q_agendal'
REPLACEMENT = 'id_agendap'

def mass_refactor():
    print(f"🔍 Iniciando Faxina em: {PROJECT_PATH}")
    count = 0
    # Percorre todos os arquivos .py e .md na pasta src
    for root, dirs, files in os.walk(PROJECT_PATH):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if TARGET in content:
                        new_content = content.replace(TARGET, REPLACEMENT)
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✅ Refatorado: {path}")
                        count += 1
                except Exception as e:
                    # Fallback para outros encodings se utf-8 falhar
                    try:
                        with open(path, 'r', encoding='latin-1') as f:
                            content = f.read()
                        if TARGET in content:
                            new_content = content.replace(TARGET, REPLACEMENT)
                            with open(path, 'w', encoding='latin-1') as f:
                                f.write(new_content)
                            print(f"✅ Refatorado (Latin1): {path}")
                            count += 1
                    except:
                        print(f"❌ Erro crítico em {path}: {e}")
    
    print(f"\n🏁 Operação Faxina Concluída!")
    print(f"📦 Total de Arquivos Blindados: {count}")

if __name__ == "__main__":
    mass_refactor()
