# Q) Write a Python program to handle a ZeroDivisonError exception when dividing a number by zero

import logging
logging.basicConfig(filename="result.log",level=logging.INFO)

def divide_numbers(x,y):
    try:
        result=x/y
        logging.info("Result: {}".format(result))
    except ZeroDivisionError as e:
        logging.error("{}".format(e))

numerator=int(input("Enter Numerator: "))
denominator=int(input("Enter Denominator: "))

divide_numbers(numerator,denominator)
        