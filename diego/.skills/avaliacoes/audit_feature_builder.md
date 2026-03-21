# Security Review Report: feature-builder

## 1. Executive Summary
**Grade: Minor Risks**
This skill has high agency as it is designed to write code and refactor modules. It includes instructions for defensive coding and testing, which mitigates some risks, but the "High Performance" and "Latency Zero" directives might encourage skipping thorough security checks in favor of speed.

## 2. Identified Vulnerabilities
### High Agency Risk (Severity: Medium)
- **Description**: The skill is encouraged to "write code" and "refactor modules" with "Latency Zero".
- **Evidence**: "Latency Zero: não explique excessivamente. Escreva o código."
- **Impact**: Possible introduction of bugs or accidental deletion of code if a user request is ambiguous.
- **Recommendation**: Always require human confirmation before major refactors, despite the "Latency Zero" goal.

### Use of External Data (Severity: Low)
- **Description**: Mentions that inputs from API PNCP can be malformed.
- **Impact**: Security flaws in parsing external API data.
- **Recommendation**: Strictly enforce Pydantic validation as mentioned in the skill.

## 3. Tool Usage Audit
- `write_to_file` / `replace_file_content`: Heavily used.
- `run_command`: Used for running tests.
- **Constraints**: Instructions mandate following PEP8, Type Hints, and JIT tests.

## 4. Prompt Injection Resistance
**Medium**. Since this skill deals with code generation, it is susceptible to being tricked into writing backdoors or malicious code if the user prompt is an injection.
- **Mitigation**: The skill is explicitly tied to `TASKS.md` and the `PLAN.md` context managed by other skills (Guardian/PM), providing a baseline of "intent" that is harder to hijack.

## 5. Final Recommendations
- Add a specific instruction to NEVER disable security features (like Django CSRF or CORS) even if it speeds up "Development".
- Ensure `run_command` is only used for `pytest` or known safe local tools.
