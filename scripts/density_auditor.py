import os

def audit_modules(path):
    print("--- AUDITORIA DE DENSIDADE ---")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        count = len(lines)
                        # Regra PeixotoClaw: > 350 é Alerta, > 500 é Proibido
                        if count > 500:
                            print(f"[PROIBIDO] {count} linhas - {file_path}")
                        elif count > 350:
                            print(f"[ALERTA] {count} linhas - {file_path}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    base_path = r'D:/OneDrive/aiproj/mind/vpn_mind/src/modules'
    audit_modules(base_path)
