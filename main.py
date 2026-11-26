#!/usr/bin/env python3
"""Print the entry: a single comment a developer left above fragile code."""

ENTRY = "# TODO(2019): remove this once the migration is done. The migration finished in 2021. This is still here."


def main():
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
