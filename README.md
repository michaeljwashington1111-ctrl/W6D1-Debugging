# W6D1 — Debugging & Testing Workshop (GitHub Codespaces)

## Launch
1. Click **Code → Create codespace on main**.
2. Wait for the container to build.
3. In the terminal, run: `python run_menu.py` or use **Terminal → Run Task…**.

## Tasks
- Reproduce a traceback by running `python calculator.py`, then fix:
  - `divide(a, b)`: return `None` when `b == 0` (and print a helpful message)
  - `power(a, b)`: use `**` instead of `^`
  - `average(numbers)`: divide by `len(numbers)`; single-item list should work
- Run tests until green: `python -m unittest -v`
- TDD mini challenge: implement `reverse_string(s)` in `reverser.py` to satisfy `test_reverser.py`

## VS Code
- **Run & Debug**: Debug tests or current file.
- **Tasks**: Run calculator, run tests, or open the menu.

## Makefile (optional)
- `make run`, `make test`, `make test-calculator`, `make test-reverser`, `make menu`
