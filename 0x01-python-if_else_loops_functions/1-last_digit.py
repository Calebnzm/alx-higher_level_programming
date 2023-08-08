#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
last_ = int(str(number)[-1])
last = last_

if last > 5 and number > 0:
    print(f"Last digit of {number} is {last_} and is greater than 5")
elif last > 5 and number < 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
elif last_ == 0:
    print(f"Last digit of {number} is {last_} and is 0")
elif last < 6 and last != 0 and number > 0:
    print(f"Last digit of {n} is {last} and is less than 6 and not 0")
elif last < 6 and last != 0 and number < 0:
    print(f"Last digit of {n} is -{last} and is less than 6 and not 0")
else:
    print("Invalid case")
