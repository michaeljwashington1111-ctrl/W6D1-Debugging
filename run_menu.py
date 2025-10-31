import subprocess, sys, json, os

TARGETS = [
    ("Run: calculator.py (may error)", ["python", "calculator.py"]),
    ("Tests: all (unittest discovery)", ["python", "-m", "unittest", "-v"]),
    ("Tests: calculator only", ["python", "-m", "unittest", "-v", "test_calculator.py"]),
    ("Tests: reverser only", ["python", "-m", "unittest", "-v", "test_reverser.py"]),
]

STATE = ".last_run_w6d1"

def load_last():
    try:
        with open(STATE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_last(idx):
    with open(STATE, "w") as f:
        json.dump({"last": idx}, f)

def main():
    env_sel = os.environ.get("RUN_TARGET")
    last = load_last().get("last")

    if env_sel is not None:
        try:
            idx = int(env_sel)
            title, cmd = TARGETS[idx]
            print(f"▶ Running via RUN_TARGET={idx}: {title}")
            save_last(idx)
            sys.exit(subprocess.call(cmd))
        except Exception as e:
            print("Invalid RUN_TARGET:", e)

    print("\n=== W6D1: Debugging & Testing — Runner ===")
    for i, (title, _) in enumerate(TARGETS):
        mark = " (last)" if last == i else ""
        print(f"[{i}] {title}{mark}")
    choice = input("Choose number (Enter = re-run last): ").strip()

    if choice == "":
        if last is None:
            print("No previous selection. Please choose a number.")
            return 0
        idx = last
    else:
        try:
            idx = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            return 1

    if not (0 <= idx < len(TARGETS)):
        print("Out of range.")
        return 1

    title, cmd = TARGETS[idx]
    print(f"▶ Running: {title} — {' '.join(cmd)}")
    save_last(idx)
    return subprocess.call(cmd)

if __name__ == "__main__":
    sys.exit(main())
