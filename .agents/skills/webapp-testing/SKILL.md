---
name: webapp-testing
description: Toolkit para testes automatizados de aplicações web locais usando Playwright e captura de logs/screenshots.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

**Helper Scripts Available**:
- `scripts/with_server.py` - Manages server lifecycle (supports multiple servers)

**Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is abslutely necessary. These scripts can be very large and thus pollute your context window. They exist to be called directly as black-box scripts rather than ingested into your context window.

## Decision Tree: Choosing Your Approach

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Run: python scripts/with_server.py --help
        │        Then use the helper + write simplified Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Using with_server.py

To start a server, run `--help` first, then use the helper:

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

To create an automation script, include only Playwright logic (servers are managed automatically):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
    page = browser.new_page()
    page.goto('http://localhost:5173') # Server already running and ready
    page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
    # ... your automation logic
    browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- **Use bundled scripts as black boxes** - To accomplish a task, consider whether one of the scripts available in `scripts/` can help. These scripts handle common, complex workflows reliably without cluttering the context window. Use `--help` to see usage, then invoke directly. 
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`

## PeixotoClaw Visual Approval Protocol

Use this protocol whenever a task changes frontend behavior, approval flows, generated reports, dashboards, modals, forms, or any user-visible state.

### Required Evidence

For each relevant viewport, capture:

- **Screenshot**: final rendered state after the key user action.
- **Console logs**: browser errors, warnings, and failed requests.
- **DOM/action notes**: selectors used and the critical path executed.
- **Outcome assertion**: the visible condition that proves the workflow worked.

Default viewports:

- Desktop: `1440x900`
- Mobile: `390x844`

Add tablet only when layout risk is material.

### Standard Smoke Flow

1. Start the app with `scripts/with_server.py` when the server is not already running.
2. Navigate to the target URL and wait for `networkidle`.
3. Capture an initial screenshot for reconnaissance when selectors are unknown.
4. Execute the real user path with role/text selectors when possible.
5. Capture the final screenshot.
6. Fail the smoke if any of these occur:
   - uncaught browser console error
   - failed critical network request
   - blank screen or blank canvas
   - overlapping or clipped primary UI text
   - missing expected button, modal, status, toast, or generated artifact link
   - layout shift that changes the dimensions of fixed-format controls

### Approval And Report Flows

For approval/report screens, validate at minimum:

- Primary action button is visible, enabled only when expected, and does not overflow.
- Loading/background-job state is visible after submission.
- Polling or refresh behavior reaches a terminal status.
- Success state exposes the generated artifact or next action.
- Error state is readable and does not trap the user.
- Reopening the modal/page preserves the expected persisted status.

### Output Location

Prefer writing temporary screenshots and traces under a task-specific scratch folder, for example:

```bash
scratch/web-smoke/<feature-or-ticket>/
```

Mention the important screenshot paths in the final answer only when they are useful for review.

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation
