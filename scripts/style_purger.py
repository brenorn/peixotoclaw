import os
import re

def purge_inline_styles(dashboard_path, css_path):
    print('--- INICIANDO PURGACAO DE ESTILOS ---')
    
    # Regex para capturar blocos style completos
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    css_link = f'    <link href="{css_path}" rel="stylesheet">'

    for file in os.listdir(dashboard_path):
        if file.endswith('.html'):
            file_path = os.path.join(dashboard_path, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '<style>' in content:
                    # Substitui o bloco de estilo pelo link
                    new_content = style_pattern.sub(css_link, content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'[PURIFICADO] {file}')
                else:
                    pass
            except Exception as e:
                print(f'[ERRO] Falha ao processar {file}: {e}')

if __name__ == "__main__":
    target_dir = r'D:/OneDrive/aiproj/mind/vpn_mind/src/modules/core/delivery/public/dashboard'
    # Como os arquivos estão dentro de /dashboard, o link para shared/css deve ser ../
    relative_css = '../shared/css/nexus_theme.css'
    purge_inline_styles(target_dir, relative_css)
