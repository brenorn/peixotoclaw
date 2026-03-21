import json
import os
from datetime import datetime

class AcademicSessionMemory:
    """
    Versão simplificada da Memory do Sandeco para persistência local sem Redis.
    Focada em manter o contexto da tese/artigo durante a sessão.
    """
    def __init__(self, session_file="academic_session.json"):
        self.session_file = session_file
        self.history = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def add_memory(self, role, content):
        timestamp = datetime.now().isoformat()
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": timestamp
        })
        self._save_memory()

    def _save_memory(self):
        with open(self.session_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)

    def get_context_summary(self):
        """Retorna as últimas 5 interações como contexto."""
        return self.history[-10:]

if __name__ == "__main__":
    mem = AcademicSessionMemory()
    mem.add_memory("user", "Iniciando seção de resultados para Automation in Construction.")
    print(f"✅ Sessão atual com {len(mem.history)} mensagens.")
