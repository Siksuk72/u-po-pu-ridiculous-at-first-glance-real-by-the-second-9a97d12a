#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (<=200 characters) pitching a bizarre startup idea
that sounds absurd until you realise it would actually sell.
"""

ENTRY = "Your neighbours already see your Wi-Fi name, so we sell it to the café downstairs — you get paid every month for a password you never change."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing space"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    assert "\n" not in ENTRY, "entry must be a single line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
