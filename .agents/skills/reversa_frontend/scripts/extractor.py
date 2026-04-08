import os
import re
import json
import argparse
from bs4 import BeautifulSoup

class FrontendExtractor:
    """Ferramenta de extração técnica para Engenharia Reversa de UI."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.results = {
            "file": os.path.basename(file_path),
            "inputs": [],
            "buttons": [],
            "api_endpoints": set(),
            "js_links": [],
            "calculations": []
        }

    def analyze(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

            # 1. Inputs e Variáveis
            for i in soup.find_all(['input', 'select', 'textarea']):
                self.results["inputs"].append({
                    "id": i.get('id'),
                    "name": i.get('name'),
                    "type": i.get('type'),
                    "class": i.get('class')
                })

            # 2. Botões e Ações
            for b in soup.find_all(['button', 'a']):
                if b.get('onclick') or b.get('id'):
                    self.results["buttons"].append({
                        "id": b.get('id'),
                        "text": b.text.strip(),
                        "onclick": b.get('onclick'),
                        "class": b.get('class')
                    })

            # 3. JS Links
            for s in soup.find_all('script', src=True):
                self.results["js_links"].append(s.get('src'))

            # 4. Busca por Endpoints de API e Cálculos em blocos SCRIPT
            for s in soup.find_all('script'):
                if not s.get('src'):
                    code = s.string if s.string else ""
                    # Busca URLs (padrão simples)
                    urls = re.findall(r'[\'"](/api/.*?)[\'"]|[\'"](.*?.php)[\'"]', code)
                    for url_tuple in urls:
                        for url in url_tuple:
                            if url: self.results["api_endpoints"].add(url)
                    
                    # Busca funções que pareçam cálculos
                    calcs = re.findall(r'function\s+(\w*(?:calc|caculate|total|sum|media|verify|validate)\w*)\s*\(', code, re.IGNORECASE)
                    self.results["calculations"].extend(calcs)

        self.results["api_endpoints"] = list(self.results["api_endpoints"])
        return self.results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Caminho do arquivo HTML/React")
    args = parser.parse_args()
    
    extractor = FrontendExtractor(args.file)
    data = extractor.analyze()
    print(json.dumps(data, indent=4, ensure_ascii=False))
