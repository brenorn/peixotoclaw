import os
import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from core import planning_paths, load_config, normalize_md
import yaml

def extract_field(content: str, field_name: str) -> Optional[str]:
    """
    Extract a field value from STATE.md content.
    Supports **Field:** bold and plain Field: format.
    """
    escaped = re.escape(field_name)
    bold_pattern = fr"\*\*({escaped}):\*\*\s*(.+)"
    bold_match = re.search(bold_pattern, content, re.IGNORECASE)
    if bold_match:
        return bold_match.group(2).strip()
    
    plain_pattern = fr"^{escaped}:\s*(.+)"
    plain_match = re.search(plain_pattern, content, re.MULTILINE | re.IGNORECASE)
    if plain_match:
        return plain_match.group(1).strip()
    
    return None

def replace_field(content: str, field_name: str, new_value: str) -> Optional[str]:
    """Replace a field value in the content."""
    escaped = re.escape(field_name)
    bold_pattern = fr"(\*\*({escaped}):\*\*\s*)(.*)"
    if re.search(bold_pattern, content, re.IGNORECASE):
        return re.sub(bold_pattern, fr"\g<1>{new_value}", content, flags=re.IGNORECASE)
    
    plain_pattern = fr"(^({escaped}):\s*)(.*)"
    if re.search(plain_pattern, content, re.MULTILINE | re.IGNORECASE):
        return re.sub(plain_pattern, fr"\g<1>{new_value}", content, flags=re.MULTILINE | re.IGNORECASE)
    
    return None

def patch_state(cwd: str, patches: Dict[str, str]) -> Dict[str, Any]:
    """Patch multiple fields in STATE.md."""
    state_path = planning_paths(cwd)["state"]
    if not state_path.exists():
        return {"updated": [], "failed": list(patches.keys()), "error": "STATE.md not found"}
    
    try:
        content = state_path.read_text(encoding="utf-8")
        updated = []
        failed = []
        
        for field, value in patches.items():
            new_content = replace_field(content, field, value)
            if new_content:
                content = new_content
                updated.append(field)
            else:
                failed.append(field)
        
        if updated:
            state_path.write_text(sync_frontmatter(content, cwd), encoding="utf-8")
            
        return {"updated": updated, "failed": failed}
    except Exception as e:
        return {"updated": [], "failed": list(patches.keys()), "error": str(e)}

def advance_plan(cwd: str) -> Dict[str, Any]:
    """Progress the state to the next plan."""
    state_path = planning_paths(cwd)["state"]
    if not state_path.exists():
        return {"error": "STATE.md not found"}
    
    content = state_path.read_text(encoding="utf-8")
    today = datetime.now().isoformat().split('T')[0]
    
    plan_field = extract_field(content, "Plan")
    if not plan_field:
        return {"error": "Plan field not found"}
        
    try:
        # Expected format "2 of 6"
        match = re.search(r"(\d+)\s+of\s+(\d+)", plan_field)
        if not match:
            return {"error": f"Invalid plan format: {plan_field}"}
            
        current_plan = int(match.group(1))
        total_plans = int(match.group(2))
        
        if current_plan >= total_plans:
            # Phase Complete
            content = replace_field(content, "Status", "Phase complete — ready for verification")
            content = replace_field(content, "Last Activity", today)
            state_path.write_text(sync_frontmatter(content, cwd), encoding="utf-8")
            return {"advanced": False, "reason": "last_plan", "status": "ready_for_verification"}
        else:
            new_plan = current_plan + 1
            new_display = plan_field.replace(str(current_plan), str(new_plan), 1)
            content = replace_field(content, "Plan", new_display)
            content = replace_field(content, "Status", "Ready to execute")
            content = replace_field(content, "Last Activity", today)
            state_path.write_text(sync_frontmatter(content, cwd), encoding="utf-8")
            return {"advanced": True, "previous": current_plan, "current": new_plan}
            
    except Exception as e:
        return {"error": f"Advance Plan Error: {str(e)}"}

def sync_frontmatter(content: str, cwd: str) -> str:
    """Synchronize YAML frontmatter with body content."""
    # Strip existing frontmatter
    body = re.sub(r"^\s*---\n[\s\S]*?\n---\s*", "", content)
    
    # Extract fields from body
    fm = {
        "gsd_state_version": "1.0",
        "status": extract_field(body, "Status") or "unknown",
        "last_updated": datetime.now().isoformat(),
        "last_activity": extract_field(body, "Last Activity"),
        "current_phase": extract_field(body, "Current Phase"),
        "current_plan": extract_field(body, "Plan")
    }
    
    yaml_str = yaml.dump(fm, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---\n\n{normalize_md(body)}"

def write_initial_state(cwd: str, initial_data: Dict[str, Any]):
    """Initialize a new STATE.md."""
    state_path = planning_paths(cwd)["state"]
    template = f"""**Current Phase:** {initial_data.get('phase', '01')}
**Status:** {initial_data.get('status', 'Planning')}
**Plan:** 1 of {initial_data.get('total_plans', '1')}
**Progress:** [░░░░░░░░░░] 0%
**Last Activity:** {datetime.now().isoformat().split('T')[0]}

## Current Position
- No activities yet.

## Performance Metrics
| Phase/Plan | Duration | Task Count | File Count |
| :--- | :--- | :--- | :--- |
| None yet | - | - | - |

## Blockers
None
"""
    state_path.write_text(sync_frontmatter(template, cwd), encoding="utf-8")
