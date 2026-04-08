# Security Review Report: project-manager

## 1. Executive Summary
**Grade: Secure**
A management skill for document synchronization. Low security risk.

## 2. Identified Vulnerabilities
None identified.

## 3. Tool Usage Audit
- `write_to_file`: For updating `TASKS.md` and `CURRENT_CONTEXT.md`.

## 4. Prompt Injection Resistance
**High**. Directs the user back to the planned track.

## 5. Final Recommendations
- Ensure that "tasks as completed" checking includes a verification step as mentioned in the skill.
