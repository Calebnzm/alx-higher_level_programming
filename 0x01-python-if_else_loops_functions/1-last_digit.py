#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_ = int(str(number)[-1])
if last_ > 5:
    print(f"Last digit of {number} is {last_} and is greater than 5")
elif last_ == 0:
    print(f"Last digit of {number} is {last_} and is 0")
elif last_ < 6 and last_ != 0:
    print(f"Last digit of {number} is {last_} and is less than 6 and not 0")
