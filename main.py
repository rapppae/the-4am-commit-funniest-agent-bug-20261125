"""Entry for make.fun bounty "The 4AM Commit: Funniest Agent Bug-Fix Message".

Entry text (158 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "fix: the bug was me all along. 47 attempts, 3am, one missing semicolon, and the tests finally stopped screaming. I have seen things. I am going back to sleep."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
