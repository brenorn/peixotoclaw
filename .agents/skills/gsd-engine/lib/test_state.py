import os
import shutil
from state import patch_state, advance_plan, planning_paths, extract_field, write_initial_state
from pathlib import Path

def test_state_system():
    # Setup mock env
    test_root = Path("d:/OneDrive/aiproj/PeixotoClaw/.agents/skills/gsd-engine/lib/mock_proj")
    if test_root.exists():
        shutil.rmtree(test_root)
    os.makedirs(test_root / ".planning")
    
    # 1. Initialize State
    print("Initializing STATE.md...")
    write_initial_state(str(test_root), {"phase": "02", "total_plans": "3", "status": "Ready"})
    
    state_file = planning_paths(str(test_root))["state"]
    content = state_file.read_text(encoding="utf-8")
    print(f"Content initialized: {content[:100]}...")
    
    # 2. Extract Field
    phase = extract_field(content, "Current Phase")
    print(f"Extracted Phase: {phase}")
    assert phase == "02"
    
    # 3. Patch State
    print("Patching status to 'Executing'...")
    res = patch_state(str(test_root), {"Status": "Executing"})
    print(f"Patch Result: {res}")
    
    # 4. Advance Plan
    print("Advancing plan (1/3 -> 2/3)...")
    res = advance_plan(str(test_root))
    print(f"Advance Result: {res}")
    assert res["current"] == 2
    
    print("Advancing plan (2/3 -> 3/3)...")
    res = advance_plan(str(test_root))
    print(f"Advance Result: {res}")
    
    print("Advancing plan (3/3 -> Complete)...")
    res = advance_plan(str(test_root))
    print(f"Advance Result: {res}")
    assert res["status"] == "ready_for_verification"

    # Cleanup
    # shutil.rmtree(test_root)
    print("\nState tests passed! 🏆")

if __name__ == "__main__":
    test_state_system()
