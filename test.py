from serial import Serial
import time

def arduinoSender(ans):
    arduinoData = Serial('com4', 9600)
    while True:
        msg = str(ans) + '\r'    
        arduinoData.write(msg.encode())

def closePort(arduinoData):
    #arduinoData = Serial('com4', 9600)
    arduinoData.close()