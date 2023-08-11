#!/usr/bin/python3

import hidden_4


def main():
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    main()
