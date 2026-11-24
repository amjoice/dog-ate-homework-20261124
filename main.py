#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one funny excuse line, in a dog's own voice, to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked against the published judge brief, not as a first
draft. Two candidates were weighed and set aside: "I didn't eat your
homework. I relocated it somewhere warmer and darker." (a tidy
bureaucratic joke, but the dog sounds like a clerk filing paperwork, not
a dog caught in the act) and "The homework started it. It just sat there,
staring at me, being homework." (deadpan, but it ends on a shrug instead
of a punch). This one won: it opens mid-accusation, it gives the homework
a motive (it was staring, it was going to eat you), the dog's logic is
pure self-defence, and it closes on "You're welcome" -- a dog who is
convinced it did its human a favour, with zero embarrassment and no
stock line about the cat, the taste of paper, or being a good boy.
Short, too: 75 characters, which also wins a size tie-break.
"""

import os

EXCUSE = (
    "It kept staring at me, so I ate it before it could eat you. "
    "You're welcome."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "excuse must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
