import logging
logging.basicConfig(filename="factorial.log",level=logging.INFO)

class validate_number(Exception):
    def __init__(self,msg):
        self.msg=msg
    
def validate__number(num):
    if num <0:
        raise validate_number("no factorial for negative numbers")
    else:
        if num==0:
          logging.info("factorial is 1")
        else:
            fact=1;
            for i in range(1,num+1):
              fact=fact*i
            logging.info("factorial of "+str(num)+" is "+str(fact))

try:
    num=int(input("Enter any number: "))
    validate__number(num)
except validate_number as e:
    print(e)

logging.shutdown()