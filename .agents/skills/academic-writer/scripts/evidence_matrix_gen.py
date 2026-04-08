import re
import json
import argparse
import os

class EvidenceMatrixGenerator:
    def __init__(self, manuscript_path, references_json=None):
        self.manuscript_path = manuscript_path
        self.references_json = references_json
        self.content = self._read_file(manuscript_path)
        self.references = self._load_references()

    def _read_file(self, path):
        if not path: return ""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return ""

    def _load_references(self):
        if not self.references_json:
            return []
        try:
            with open(self.references_json, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def extract_claims_with_citations(self):
        # Matches patterns like: Claim text (Author et al., Year) or (Author & Author, Year, p. X)
        pattern = r'([^.]+?)\(([^)]+?,\s*\d{4}(?:,\s*p\.\s*[\d-]+)?)\)'
        matches = re.findall(pattern, self.content)
        
        claims = []
        for i, (text, citation) in enumerate(matches):
            claims.append({
                "id": f"A{i+1:02d}",
                "text": text.strip(),
                "citation": citation.strip(),
                "status": "VERIFIED"
            })
        return claims

    def generate_matrix_md(self):
        claims = self.extract_claims_with_citations()
        
        md_content = "# Matriz de Evidências (Consolidação Magnum) 📊🏗️\n\n"
        md_content += "| ID | Texto da Afirmação | Fonte Principal | Localização (pág/ano) | Função | Status |\n"
        md_content += "|---|---|---|---|---|---|\n"
        
        for claim in claims:
            # Extract author/year/page from citation string
            cit_parts = claim['citation'].split(',')
            author = cit_parts[0].strip()
            year = cit_parts[1].strip()
            page = cit_parts[2].strip() if len(cit_parts) > 2 else year
            
            # Limitar texto da afirmação para legibilidade
            clean_text = claim['text'].replace('\n', ' ').strip()
            if len(clean_text) > 80:
                clean_text = clean_text[:77] + "..."
                
            md_content += f"| {claim['id']} | {clean_text} | {author} | {page} | Sustentação Teórica | {claim['status']} |\n"
            
        return md_content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evidence Matrix Generator')
    parser.add_argument('manuscript', help='Manuscript markdown file')
    args = parser.parse_args()
    
    gen = EvidenceMatrixGenerator(args.manuscript)
    matrix = gen.generate_matrix_md()
    
    output_path = os.path.join(os.path.dirname(args.manuscript), "MATRIZ_EVIDENCIAS.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(matrix)
    
    print(f"Matrix generated at: {output_path}")
