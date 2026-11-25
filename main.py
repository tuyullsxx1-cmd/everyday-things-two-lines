# line 1: the analogy; line 2: its limits
LINE_ONE = "A toaster is like a tiny sun trapped in a metal box: it stares at your bread until it turns golden, and if you look away it burns it out of spite."
LINE_TWO = "The sun part works because both cook with heat and light, but it leaves out the timer — a real sun never pops up when it's done."


def emit_two_lines():
    text = "\n".join((LINE_ONE, LINE_TWO))
    handle = open("/output/entry.txt", "w", encoding="utf-8")
    handle.write(text)
    handle.close()


emit_two_lines()
