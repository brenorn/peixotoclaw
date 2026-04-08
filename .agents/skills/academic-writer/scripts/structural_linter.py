import re
import sys
import argparse

class StructuralLinter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self._read_file()
        self.paragraphs = self._split_into_paragraphs()
        
    def _read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            sys.exit(1)

    def _split_into_paragraphs(self):
        # Split by double newlines or more
        raw_paras = re.split(r'\n\s*\n', self.content)
        # Filter out headers and short metadata lines
        return [p.strip() for p in raw_paras if p.strip() and not p.strip().startswith('#')]

    def check_paragraph_density(self, min_sentences=6):
        results = []
        for i, para in enumerate(self.paragraphs):
            # Simple sentence splitter (dot followed by space and capital letter/digit)
            sentences = re.split(r'\.[\s\n]+', para)
            sentences = [s for s in sentences if len(s.strip()) > 10]
            
            if len(sentences) < min_sentences:
                results.append({
                    "paragraph_index": i + 1,
                    "sentence_count": len(sentences),
                    "status": "FAIL",
                    "content_preview": para[:100] + "..."
                })
            else:
                results.append({
                    "paragraph_index": i + 1,
                    "sentence_count": len(sentences),
                    "status": "PASS"
                })
        return results

    def check_citations(self):
        # ABNT pattern: (NAME, Year, p. XX)
        citation_pattern = r'\([A-Z\s]+,\s*\d{4},\s*p\.\s*[\d-]+\)'
        results = []
        for i, para in enumerate(self.paragraphs):
            citations = re.findall(citation_pattern, para)
            if not citations:
                results.append({
                    "paragraph_index": i + 1,
                    "citations": 0,
                    "status": "FAIL",
                    "content_preview": para[:100] + "..."
                })
            else:
                results.append({
                    "paragraph_index": i + 1,
                    "citations": len(citations),
                    "status": "PASS"
                })
        return results

    def run_audit(self):
        print(f"--- Nexus V5 Structural Audit: {self.file_path} ---")
        density = self.check_paragraph_density()
        citations = self.check_citations()
        
        failed_density = [r for r in density if r['status'] == "FAIL"]
        failed_citations = [r for r in citations if r['status'] == "FAIL"]
        
        print(f"\n[Paragraph Density (Min 6 sentences)]")
        print(f"Total Paragraphs: {len(self.paragraphs)}")
        print(f"Passed: {len(self.paragraphs) - len(failed_density)}")
        print(f"Failed: {len(failed_density)}")
        
        if failed_density:
            print("\n  Details (Failed Density):")
            for r in failed_density:
                print(f"  - Para {r['paragraph_index']}: {r['sentence_count']} sentences. | Preview: {r['content_preview']}")

        print(f"\n[Citation Coverage (ABNT Pattern)]")
        print(f"Passed: {len(self.paragraphs) - len(failed_citations)}")
        print(f"Failed: {len(failed_citations)}")

        if failed_citations:
            print("\n  Details (Failed Citations):")
            for r in failed_citations:
                print(f"  - Para {r['paragraph_index']}: 0 citations found. | Preview: {r['content_preview']}")

        print("\n--- End of Audit ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nexus V5 Structural Linter')
    parser.add_argument('file', help='Markdown file to audit')
    args = parser.parse_args()
    
    linter = StructuralLinter(args.file)
    linter.run_audit()
