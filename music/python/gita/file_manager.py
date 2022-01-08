import time
import sys
import os
from console_panel import window, setSaveServoButtonCb

def servoDataWriteDefault():
    writedict = {}
    for i in range(len(window.qleServoControl)):
        writedict[i] = 90
    print('default writedict is', writedict)
    with open(servoDataPath, 'w') as file:
        file.write(str(writedict))
    return writedict

def saveServoDatas():
    writedict = {}
    for i in range(len(window.qleServoControl)):
        writedict[i] = window.qleServoControl[i].text()
    print('writedict is', writedict)
    with open(servoDataPath, 'w') as file:
        file.write(str(writedict))

def readServoDatas():
    try:
        with open(servoDataPath, 'r') as file:
            writedict = eval(file.read())
        return writedict
    except:
        writedict = servoDataWriteDefault()
        return writedict

print(os.getcwd())
servoDataPath = os.getcwd() + '\\servoData.txt'
setSaveServoButtonCb(saveServoDatas)
