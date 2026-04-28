import os

def full_frontend_audit(base_path):
    print('--- INVENTARIO PANOPTICO DO FRONTEND ---')
    audit_report = []
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(('.html', '.js')):
                try:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, base_path)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = len(content.splitlines())
                        # Critérios de Auditoria
                        has_localhost = 'localhost' in content
                        has_legacy = ('src/api' in content) or ('server_v3' in content)
                        
                        audit_report.append({
                            'file': rel_path,
                            'lines': lines,
                            'localhost': has_localhost,
                            'legacy': has_legacy
                        })
                except:
                    pass
    
    # Ordenar por criticidade e tamanho
    audit_report.sort(key=lambda x: (x['localhost'] or x['legacy'], x['lines']), reverse=True)
    
    for item in audit_report:
        flags = []
        if item['localhost']: flags.append('LOCAL')
        if item['legacy']: flags.append('LEGACY')
        if item['lines'] > 500: flags.append('HUGE')
        
        status = f"[{'|'.join(flags)}]" if flags else '[OK]'
        print(f"{item['lines']:4d} l | {status:15} | {item['file']}")

if __name__ == '__main__':
    path = r'D:/OneDrive/aiproj/mind/vpn_mind/src/modules/core/delivery/public'
    full_frontend_audit(path)
