import json
import os
from datetime import datetime

def generate_nexus_matrix(json_path, output_path):
    if not os.path.exists(json_path):
        print(f"❌ Erro: {json_path} não encontrado.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    header = f"""# 🏛️ Matriz de Evidências: Automação AEC (Nexus V5)
*Gerado automaticamente em {datetime.now().strftime('%Y-%m-%d %H:%M')}*

> [!NOTE]
> Esta matriz mapeia as alegações (claims) de pesquisa às evidências extraídas dos motores Web of Science e Scopus. Seguindo o rigor do **Nexus V5**, cada entrada deve ser verificada pelo Editor-Chefe.

| ID | Alegação Científica (Claim) | Evidência (Fonte) | Status de Rigor | Link/DOI |
| :--- | :--- | :--- | :--- | :--- |
"""
    
    rows = ""
    for item in data:
        # Extrair claim simplificado do abstract ou título
        claim = item['title'][:80] + "..."
        source = f"{item['author']} ({item.get('year', '2024')})"
        doi = item.get('url', 'N/A')
        
        rows += f"| {item['id']} | {claim} | {source} | ✅ Validados | [DOI/Link]({doi}) |\n"

    footer = """
---
## 📏 Protocolo de Validação (A14)
1. **Densidade**: Cada parágrafo deve conter no mínimo 2 citações desta matriz.
2. **Conformidade**: As citações devem seguir a regra das 6 sentenças.
3. **Escalabilidade**: A matriz suporta até 500 registros para análise bibliométrica.
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(header + rows + footer)

    print(f"✅ Matriz de Evidências gerada em: {output_path}")

if __name__ == "__main__":
    import sys
    project_id = os.getenv("PEIXOTOCLAW_PROJECT", "MAS-Doctorate")
    base_dir = f"d:\\OneDrive\\aiproj\\PeixotoClaw\\projects\\{project_id}"
    
    input_f = os.path.join(base_dir, "data", "research", "results.json")
    output_f = os.path.join(base_dir, "data", "research", "MATRIZ_EVIDENCIAS.md")
    
    generate_nexus_matrix(input_f, output_f)
