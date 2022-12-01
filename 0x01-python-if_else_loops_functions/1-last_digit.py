#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = abs(number) % 10
if (rem < 0):
    rem = -rem
if (rem > 5):
    print(f"Last digit of {number} is {rem} and is greater than 5")
elif (rem == 0):
    print(f"Last digit of {number} is {rem} and is 0")
elif (rem < 6 and rem != 0):
    print(f"Last digit of {number} is {rem} and is less than 6 and not 0")
