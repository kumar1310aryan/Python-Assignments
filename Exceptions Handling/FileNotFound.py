import logging
logging.basicConfig(filename="FileNotFound.log",level=logging.INFO)

def openFile(filename):
    try:
        file=open(filename,'r')
        contents=file.read()
        logging.info("file contents : {}".format(contents))
        file.close()
    except FileNotFoundError as e:
        logging.error("{}".format(e))

filename=input("Input a file name : ")
openFile(filename)
