# Security Review Report: brainstorming

## 1. Executive Summary
**Grade: Secure**
The brainstorming skill is a behavioral and workflow guide designed to manage the discovery phase of projects. It does not utilize high-agency tools directly and relies on natural language interaction.

## 2. Identified Vulnerabilities
### Potential Logic Bypass (Severity: Low)
- **Description**: While the skill has a `<HARD-GATE>` to prevent implementation, a user could attempt to skip steps by directly asking for code.
- **Evidence**: Instructions in lines 12-14.
- **Impact**: Deviation from the project's planning-first philosophy.
- **Recommendation**: Reinforce the "Guardrail" role of the assistant when implementation skills are invoked prematurely.

## 3. Tool Usage Audit
The skill does not explicitly request tool permissions in its current `SKILL.md` frontmatter, making it inherently safe regarding filesystem or shell access.

## 4. Prompt Injection Resistance
Medium. The skill uses a structured checklist which guides the LLM to stay within the bounds of design, reducing the surface for injection-based implementation triggers.

## 5. Final Recommendations
- Ensure that the assistant context maintains the "Hard Gate" even if the user is persistent.
