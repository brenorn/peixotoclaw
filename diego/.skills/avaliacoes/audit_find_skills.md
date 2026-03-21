# Security Review Report: find-skills

## 1. Executive Summary
**Grade: Minor Risks**
This skill facilitates the discovery and installation of external agent skills via the `npx skills` CLI.

## 2. Identified Vulnerabilities
### Execution of Untrusted Third-Party Code (Severity: Medium)
- **Description**: The skill can install skills from GitHub or other sources using `npx skills add`.
- **Evidence**: Lines 28 and 101.
- **Impact**: Potential installation of malicious skills that could exfiltrate data or compromise the system.
- **Recommendation**: Mandatory human confirmation and strict verification of source reputation (stars, owner, install count) as specified in the skill's own Step 4.

## 3. Tool Usage Audit
- `run_command`: Used to run `npx skills` commands.
Safety is dependent on the `npx` sandbox and the user's manual verification of the package.

## 4. Prompt Injection Resistance
Medium. A user could trick the skill into searching and installing a malicious package if verification steps are ignored by the assistant.

## 5. Final Recommendations
- Never use the `-y` flag (auto-approve) for `npx skills add` unless the source is strictly from an official whitelist (e.g., `vercel-labs`, `anthropics`).
