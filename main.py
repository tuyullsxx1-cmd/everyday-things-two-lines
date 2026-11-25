import sys

# line 1: the analogy; line 2: its limits
LINE_ONE = "A toaster is like a tiny sun trapped in a metal box: it stares at your bread until it turns golden, and if you look away it burns it out of spite."
LINE_TWO = "The sun part works because both cook with heat and light, but it leaves out the timer \u2014 a real sun never pops up when it's done."

try:
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE_ONE + "\n" + LINE_TWO)
except OSError as problem:
    print("failed to write entry:", problem, file=sys.stderr)
    sys.exit(1)
