import re
import os

class NexusLinter:
    def __init__(self, draft_path):
        self.draft_path = draft_path

    def audit(self):
        if not os.path.exists(self.draft_path):
            print(f"❌ Arquivo {self.draft_path} não encontrado.")
            return

        with open(self.draft_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Separar por parágrafos (assumindo \n\n)
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.startswith('#')]
        
        print(f"🔍 Auditando {len(paragraphs)} parágrafos no draft...\n")
        
        report = []
        all_passed = True
        
        for i, p in enumerate(paragraphs):
            # 1. Contar sentenças (separadores básicos: . ! ?)
            sentences = re.split(r'(?<=[.!?])\s+', p)
            num_sentences = len(sentences)
            
            # 2. Contar citações (formato: (Autor, Ano) ou Autor (Ano))
            citations = re.findall(r'\(.*?\d{4}\)', p)
            num_citations = len(citations)
            
            status = "✅ PASS"
            issues = []
            
            if num_sentences != 6:
                status = "❌ FAIL"
                issues.append(f"Sentenças: {num_sentences} (Esperado: 6)")
                all_passed = False
            
            if num_citations < 2:
                status = "❌ FAIL"
                issues.append(f"Citações: {num_citations} (Esperado: 2+)")
                all_passed = False
                
            report.append(f"Parágrafo {i+1}: {status} | {' | '.join(issues) if issues else 'Nenhuma violação'}")

        print("\n".join(report))
        print("\n" + "="*30)
        if all_passed:
            print("💎 CERTIFICADO NEXUS V5: APROVADO")
        else:
            print("⚠️ REVISÃO NECESSÁRIA: VIOLAÇÃO DE RIGOR")
        print("="*30)

if __name__ == "__main__":
    project_id = os.getenv("PEIXOTOCLAW_PROJECT", "MAS-Doctorate")
    draft_f = f"d:\\OneDrive\\aiproj\\PeixotoClaw\\projects\\{project_id}\\drafts\\CHAPTER_01_STATE_OF_ART.md"
    linter = NexusLinter(draft_f)
    linter.audit()
