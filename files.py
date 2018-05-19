
file = open("c:\\Users\\fatda\Documents\\myfile.txt","rb") #rb for binary

#data = file.read(20) #20 bytes
#read returns a bytes object
#print (type(data))

with open("c:\\Users\\fatda\Documents\\myfile.txt","rb") as myfile:
    data = file.read()
    print (data)
    print (data.decode())

import logging

logging.basicConfig(level = logging.DEBUG, format = "%(levelname)s, %(asctime)s, %(message)s")
logging.warning("hmm - sure?")
logging.info("just FYI") # doesn't sow

#POpen command starts a separate CLI process - like ls or grep, or in this case notepad.exe
import os
from subprocess import Popen, PIPE
myproc = Popen(["notepad.exe", "c:\\LPMsetup.log"], stdout=PIPE)
print("stdout:"+myproc.stdout.readline().decode()) #blank in this case


