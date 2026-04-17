import os
import yaml
import json
from pathlib import Path
import sys

# Garantir que o output suporte UTF-8 (emojis no Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def generate_manifest():
    skills_root = Path(r"d:\OneDrive\aiproj\PeixotoClaw\.agents\skills")
    manifest_path = Path(r"d:\OneDrive\aiproj\PeixotoClaw\skills_manifest.json")
    
    skills = []
    
    print(f"🔍 Escaneando habilidades em {skills_root}...")
    
    for skill_dir in skills_root.iterdir():
        if skill_dir.is_dir():
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                try:
                    content = skill_md.read_text(encoding="utf-8")
                    # Extrair YAML frontmatter
                    if content.startswith("---"):
                        parts = content.split("---")
                        if len(parts) >= 3:
                            data = yaml.safe_load(parts[1])
                            skills.append({
                                "id": skill_dir.name,
                                "name": data.get("name", skill_dir.name),
                                "description": data.get("description", "Sem descrição."),
                                "path": str(skill_md)
                            })
                except Exception as e:
                    print(f"⚠️ Erro ao ler {skill_md}: {e}")

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({"skills": skills, "total": len(skills)}, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Manifesto gerado com {len(skills)} habilidades em {manifest_path}")

if __name__ == "__main__":
    generate_manifest()
