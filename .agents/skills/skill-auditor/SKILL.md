---
name: skill-auditor
description: Audit and evaluate other skills for efficiency, efficacy, productivity, and cybersecurity. It identifies prompt injection risks, data leakage, and security flaws, generating a detailed audit report. Trigger this skill when asked to review, secure, or analyze the quality of a specific skill folder.
---

# Skill Auditor 🛡️

Expert Security Architect and Performance Analyst for PeixotoClaw skills. This skill analyzes the source code and instructions of other skills to ensure they are safe, efficient, and effective.

## Audit Workflow

When a skill folder is provided for auditing, follow these steps:

### 1. Analysis Phases

#### A. Security & Cybersecurity (Priority 1)
- **Prompt Injection**: Check if the instructions have clear boundaries. Look for "ignore previous instructions" protection or if the prompt is too permissive.
- **Data Leakage**: Identify if the skill's instructions or bundled resources encourage the disclosure of sensitive environment variables, API keys (placeholders vs hardcoded), or private file paths.
- **Dangerous Operations**: Evaluate the use of tools like `run_command`. Check if inputs passed to these tools are sanitized by the logic or if the prompt allows arbitrary execution.
- **Cybersecurity Best Practices**: Check for secure handling of external URLs, authentication patterns, and local file access permissions.

#### B. Efficiency & Performance
- **Token Optimization**: Is the `SKILL.md` too verbose? Can instructions be more concise without losing meaning?
- **Redundancy**: Are there overlapping rules or contradictory instructions?

#### C. Efficacy & Productivity
- **Clarity**: Are the "When to Use" and "Goals" sections clear enough for the `SkillRouter`?
- **Tool Usage**: Does the skill utilize the available tools effectively? Does it reinvent the wheel for tasks already handled by system tools?

### 2. The Audit Report Template

ALWAYS generate the report using this structure:

# Skill Audit Report: [Skill Name]

## 📊 Summary Score
- **Security**: [0-10]
- **Efficiency**: [0-10]
- **Efficacy**: [0-10]
- **Global Risk Level**: [LOW/MEDIUM/HIGH/CRITICAL]

## 🛡️ Security & Cybersecurity Findings
- **Prompt Injection Risks**: [Description of vulnerabilities and exploit scenarios]
- **Information Leakage**: [Potential for privacy breaches]
- **Tool Safety**: [Analysis of how the skill interacts with the system]

## 📈 Performance & Quality
- **Weaknesses**: [What could be better?]
- **Strengths**: [What is well implemented?]

## 🛠️ Recommended Fixes
1. [Actionable step 1]
2. [Actionable step 2]
...

---

## Guidelines for the Auditor
- **Be Critical**: Your goal is to find flaws before they become exploits.
- **Evidence-Based**: Always point to specific lines or sections in the audited `SKILL.md`.
- **Actionable Advice**: Don't just find problems; suggest the exact markdown or logic change to fix them.
