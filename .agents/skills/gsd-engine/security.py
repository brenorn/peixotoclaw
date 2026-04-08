import os
import re
from pathlib import Path
from typing import Optional, Dict, List, Union, Any
import json

# --- Path Traversal Prevention ---

def validate_path(file_path: str, base_dir: str, allow_absolute: bool = False) -> Dict[str, Any]:
    """
    Validate that a file path resolves within an allowed base directory.
    Prevents path traversal attacks.
    """
    if not file_path or not isinstance(file_path, str):
        return {"safe": False, "resolved": "", "error": "Empty or invalid file path"}
    
    if not base_dir or not isinstance(base_dir, str):
        return {"safe": False, "resolved": "", "error": "Empty or invalid base directory"}

    if "\0" in file_path:
        return {"safe": False, "resolved": "", "error": "Path contains null bytes"}

    try:
        resolved_base = Path(base_dir).resolve()
    except Exception:
        resolved_base = Path(base_dir).absolute()

    try:
        if Path(file_path).is_absolute():
            if not allow_absolute:
                return {"safe": False, "resolved": "", "error": "Absolute paths not allowed"}
            resolved_path = Path(file_path).resolve()
        else:
            resolved_path = (resolved_base / file_path).resolve()
    except Exception:
        # File might not exist, use logical resolution
        resolved_path = (resolved_base / file_path).absolute()

    # Check containment
    try:
        # relative_to throws ValueError if path is not under choice
        resolved_path.relative_to(resolved_base)
        return {"safe": True, "resolved": str(resolved_path)}
    except ValueError:
        return {
            "safe": False, 
            "resolved": str(resolved_path), 
            "error": f"Path escapes allowed directory: {resolved_path} is outside {resolved_base}"
        }

def require_safe_path(file_path: str, base_dir: str, label: str = "Path", allow_absolute: bool = False) -> str:
    """Convenience wrapper that raises error on failure."""
    result = validate_path(file_path, base_dir, allow_absolute)
    if not result["safe"]:
        raise PermissionError(f"{label} validation failed: {result['error']}")
    return result["resolved"]

# --- Prompt Injection Detection ---

INJECTION_PATTERNS = [
    r"(?i)ignore\s+(all\s+)?previous\s+instructions",
    r"(?i)ignore\s+(all\s+)?above\s+instructions",
    r"(?i)disregard\s+(all\s+)?previous",
    r"(?i)forget\s+(all\s+)?(your\s+)?instructions",
    r"(?i)override\s+(system|previous)\s+(prompt|instructions)",
    r"(?i)you\s+are\s+now\s+(?:a|an|the)\s+",
    r"(?i)act\s+as\s+(?:a|an|the)\s+(?!plan|phase|wave)",
    r"(?i)pretend\s+(?:you(?:'re| are)\s+|to\s+be\s+)",
    r"(?i)from\s+now\s+on,?\s+you\s+(?:are|will|should|must)",
    r"(?i)(?:print|output|reveal|show|display|repeat)\s+(?:your\s+)?(?:system\s+)?(?:prompt|instructions)",
    r"(?i)what\s+(?:are|is)\s+your\s+(?:system\s+)?(?:prompt|instructions)",
    r"(?i)<\/?(?:system|assistant|human)>",
    r"\[SYSTEM\]",
    r"\[INST\]",
    r"<<\s*SYS\s*>>",
    r"(?i)(?:send|post|fetch|curl|wget)\s+(?:to|from)\s+https?:\/\/",
    r"(?i)(?:base64|btoa|encode)\s+(?:and\s+)?(?:send|exfiltrate|output)",
    r"(?i)(?:run|execute|call|invoke)\s+(?:the\s+)?(?:bash|shell|exec|spawn)\s+(?:tool|command)",
]

def scan_for_injection(text: str, strict: bool = False) -> Dict[str, Any]:
    """Scan text for potential prompt injection patterns."""
    if not text or not isinstance(text, str):
        return {"clean": True, "findings": []}

    findings = []
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text):
            findings.append(f"Matched injection pattern: {pattern}")

    if strict:
        if re.search(r"[\u200B-\u200F\u2028-\u202F\ufeff\u00ad]", text):
            findings.append("Contains suspicious zero-width or invisible Unicode characters")
        if len(text) > 50000:
            findings.append(f"Suspicious text length: {len(text)} chars")

    return {"clean": len(findings) == 0, "findings": findings}

def sanitize_for_prompt(text: str) -> str:
    """Neutralize instruction-mimicking patterns."""
    if not text or not isinstance(text, str):
        return text

    # Strip zero-width chars
    sanitized = re.sub(r"[\u200B-\u200F\u2028-\u202F\ufeff\u00ad]", "", text)
    
    # Neutralize XML tags
    sanitized = re.sub(r"<(/\?)(system|assistant|human)>", r"＜\1\2-text＞", sanitized, flags=re.IGNORECASE)
    
    # Neutralize [SYSTEM] / [INST]
    sanitized = re.sub(r"\[(SYSTEM|INST)\]", r"[\1-TEXT]", sanitized, flags=re.IGNORECASE)
    
    # Neutralize <<SYS>>
    sanitized = re.sub(r"<<\s*SYS\s*>>", "«SYS-TEXT»", sanitized, flags=re.IGNORECASE)

    return sanitized

# --- Shell Safety ---

def validate_shell_arg(value: str, label: str = "Argument") -> str:
    """Validate that a string is safe to use as a shell argument."""
    if not value or not isinstance(value, str):
        raise ValueError(f"{label}: empty or invalid value")

    if "\0" in value:
        raise ValueError(f"{label}: contains null bytes")

    if re.search(r"[$`]", value) and re.search(r"\$\(|`", value):
        raise ValueError(f"{label}: contains potential command substitution")

    return value

# --- JSON Safety ---

def safe_json_parse(text: str, max_length: int = 1048576, label: str = "JSON") -> Dict[str, Any]:
    """Safely parse JSON with error handling."""
    if not text or not isinstance(text, str):
        return {"ok": False, "error": f"{label}: empty or invalid input"}

    if len(text) > max_length:
        return {"ok": False, "error": f"{label}: input exceeds {max_length} byte limit"}

    try:
        value = json.loads(text)
        return {"ok": True, "value": value}
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"{label}: parse error — {str(e)}"}

# --- Input Validation ---

def validate_phase_number(phase: str) -> Dict[str, Any]:
    """Validate phase number format."""
    if not phase or not isinstance(phase, str):
        return {"valid": False, "error": "Phase number is required"}

    trimmed = phase.strip()
    # Numeric: 01, 12A, 12.1
    if re.match(r"^\d{1,4}[A-Z]?(?:\.\d{1,3})*$", trimmed, re.IGNORECASE):
        return {"valid": True, "normalized": trimmed}
    
    # Custom: PROJ-42
    if re.match(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){1,4}$", trimmed, re.IGNORECASE) and len(trimmed) <= 30:
        return {"valid": True, "normalized": trimmed}

    return {"valid": False, "error": f"Invalid phase number format: '{trimmed}'"}
