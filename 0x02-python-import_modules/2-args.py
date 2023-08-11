#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("{} arguments:".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
        print("{}: {}".format(num_args, argv[0]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i - 1]))


if __name__ == "__main__":
    main()
