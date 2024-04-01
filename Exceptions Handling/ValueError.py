import logging
logging.basicConfig(filename="IsValid.log",level=logging.INFO)

def get_integer(prompt):
    try:
        value=int(input(prompt))
        return value
    except ValueError as e:
        logging.error("{}".format(e))

n=get_integer("Input an integer: ")
logging.info("Input value: {}".format(n))