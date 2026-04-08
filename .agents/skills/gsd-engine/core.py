import os
import re
from pathlib import Path
from typing import Optional, Dict, Any, List
import json

def to_posix_path(p: str) -> str:
    return p.replace(os.sep, '/')

def load_config(cwd: str) -> Dict[str, Any]:
    config_path = Path(cwd) / ".planning" / "config.json"
    defaults = {
        "model_profile": "balanced",
        "commit_docs": True,
        "parallelization": True,
        "research": True,
        "plan_checker": True,
        "verifier": True,
        "nyquist_validation": True,
    }
    if not config_path.exists():
        return defaults
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return {**defaults, **json.load(f)}
    except Exception:
        return defaults

def normalize_md(content: str) -> str:
    if not content:
        return content
    # Basic normalization: ensure single newline at end, collapse triple newlines
    text = content.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text

def planning_dir(cwd: str) -> Path:
    return Path(cwd) / ".planning"

def planning_paths(cwd: str) -> Dict[str, Path]:
    base = planning_dir(cwd)
    return {
        "planning": base,
        "state": base / "STATE.md",
        "roadmap": base / "ROADMAP.md",
        "config": base / "config.json",
        "phases": base / "phases",
    }
