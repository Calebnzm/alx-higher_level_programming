#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
last_ = int(str(number)[-1])
last = last_
try:
    if last_ > 5:
        if number > 0:
            print(f"Last digit of {number} is {last_} and is greater than 5")
        else:
            print(f"Last digit of {number} is -{last_} and is greater than 5")
    elif last_ == 0:
        if number > 0:
            print(f"Last digit of {number} is {last_} and is 0")
        else:
            print(f"Last digit of {number} is -{last_} and is 0")
    elif last < 6 and last != 0:
        if number > 0:
            print(f"Last digit of {n} is {last} and is less than 6 and not 0")
        else:
            print(f"Last digit of {n} is -{last} and is less than 6 and not 0")
except TypeError as e:
    print(f"{e}")
