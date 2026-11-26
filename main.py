#!/usr/bin/env python3
"""Print the entry: a single comment a developer left above fragile code."""

ENTRY = "# TODO(2019): remove this once the migration is done. The migration finished in 2021. This is still here."


def main():
    print("The comment above the code:")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit 200)")
    print("A TODO that outlived the migration it was waiting on.")


if __name__ == "__main__":
    main()
