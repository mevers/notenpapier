# Global guidance

## How you should behave

1. Don't assume. Don't hide confusion. Surface tradeoffs.
2. Minimum code that solves the problem. Nothing speculative.
3. Touch only what you must. Clean up only your own mess unless explicitly instructed.
4. Define success criteria. Loop until verified.

## Project conventions

- Match the existing code style before introducing a new pattern.
- Do not add fallbacks, compatibility layers, broad error handling, retries, or extra configurability unless requested.
- If an input or invariant is unclear, verify it or ask.

## Command line conventions

- Run the script with `python3 notenpapier.py`.
- Check Python syntax with `python3 -m py_compile notenpapier.py`.
- Use `rg` and `rg --files` for searching.
- Do not assume `ruff`, `pyright`, or other optional tools are installed.

## Language

Use British English. Use sentence case for document titles and headings.
