#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(number_str[-1])
if int(number_str) < 0:
    last_digit = last_digit * -1
if last_digit > 5:
    print("Last digit of %s is %s and is greater than 5" % (number_str, last_digit))
elif last_digit == 0:
    print("Last digit of %s is %s and is 0" % (number_str, last_digit))
else:
    print("Last digit of %s is %s and is less than 6 and not 0" % (number_str, last_digit))
