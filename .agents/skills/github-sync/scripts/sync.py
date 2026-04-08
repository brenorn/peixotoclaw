import subprocess
import datetime
import os
import sys

# Configuration: Forbidden paths that MUST NOT be staged
FORBIDDEN_PATHS = ["projects/", "references/get-shit-done/", "vendor/EvoSkill/"]
# Core paths that SHOULD be staged
CORE_PATHS = [
    ".agents/", ".rulebook/", ".claude/", ".cursor/", ".github/", ".antigravity/",
    "scripts/", "src/", "templates/", "dashboard/",
    "README.md", ".gitignore", "package.json", "tsconfig.json", ".env.example", "peixotoclaw.bat", "gemini-extension.json"
]

def run_command(cmd, shell=True):
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H%M")

def main():
    print("--- PeixotoClaw Industrial Sync (Safety-First) ---")
    
    # 1. Create safety branch
    timestamp = get_current_timestamp()
    branch_name = f"sync/{timestamp}"
    print(f"Creating branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}")
    
    # 2. Clear index (Nuclear Reset)
    print("Purging git index (Nuclear Reset)...")
    run_command("git rm -r --cached .")
    
    # 3. Add core components
    print("Staging core components...")
    for path in CORE_PATHS:
        if os.path.exists(path):
            run_command(f"git add -f {path}")
    
    # 4. Privacy Audit
    print("Performing Privacy Audit...")
    staged_files = run_command("git diff --cached --name-only").stdout.splitlines()
    leaks = []
    for file in staged_files:
        for forbidden in FORBIDDEN_PATHS:
            if file.startswith(forbidden):
                leaks.append(file)
    
    if leaks:
        print("!!! SECURITY BREACH DETECTED !!!")
        print("The following forbidden files were detected in the staging area:")
        for leak in leaks:
            print(f" - {leak}")
        print("Aborting sync for your safety.")
        # Attempt to roll back branch
        run_command("git checkout -")
        run_command(f"git branch -D {branch_name}")
        sys.exit(1)
    
    print("Privacy Audit: PASSED ✅")
    
    # 5. Commit and Push
    commit_msg = f"feat(workspace): industrial sync branch {timestamp} - clean privacy & complete assets"
    print(f"Committing: {commit_msg}")
    run_command(f'git commit -m "{commit_msg}"')
    
    print(f"Pushing to origin {branch_name}...")
    push_result = run_command(f"git push origin {branch_name}")
    
    if push_result.returncode == 0:
        print("\n--- SYNC COMPLETED SUCCESSFULLY ---")
        print(f"Your workspace is now safe on branch: {branch_name}")
        print(f"Merge Link: https://github.com/brenorn/peixotoclaw/compare/{branch_name}")
        print("Note: Merge to 'main' ONLY after manual review on GitHub.")
    else:
        print("\n!!! PUSH FAILED !!!")
        print("Please check your internet connection and Git permissions.")

if __name__ == "__main__":
    main()
