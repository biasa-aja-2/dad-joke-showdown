"""Dad Joke Showdown.

Writes one dad joke to /output/entry.txt. Pure stdlib,
deterministic: the same joke on every run.

The joke: "I told my computer I needed a break. Now it keeps
sending me KitKat ads."

A father at the table, fighting with technology: he says he
needs a break, and the computer takes him literally -- the
KitKat slogan is "Have a break, have a Kit Kat", so the machine
answers his sigh with chocolate ads. The pun turns on a single
word, "break", needs no explaining, and the punchline lands
last. Fresh -- no chicken crossing roads, no "Hi hungry, I'm
dad" -- while staying squarely in the dad joke tradition.
"""

import os

JOKE = "I told my computer I needed a break. Now it keeps sending me KitKat ads."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars"
    assert text.strip(), "joke must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone. Never chmod /output itself.
    os.chmod(path, 0o644)
    # Verify the written joke by reading it back: the entry on disk
    # must be exactly the joke this program produced.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "written joke differs from the joke"


if __name__ == "__main__":
    main()
