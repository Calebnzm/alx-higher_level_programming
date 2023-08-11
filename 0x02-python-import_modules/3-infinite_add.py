#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]
    total = 0
    num_args = len(args)
    for i in range(0, num_args):
        total = total + int(args[i])
    print("{}".format(total))


if __name__ == "__main__":
    main()
