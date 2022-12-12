# from gsm5320 import GsmCommand , this is from gsm5320.py class file. May not use yet
import time
import serial

serial_connect = serial.Serial(port="/dev/ttyUSB3", baudrate=115200, timeout=3)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Setting for BCM pin setting, rather then numbered pins
GPIO.setwarnings(False) # No warnings
GPIO.setup(18, GPIO.OUT) # initializing pin


def msg_query():
    delete_message() # Delete message function is the last function on this file. 
    read_msg = "AT+CMGR=0\r" # Creating GSM command for GSM module, this command is for reading 
    serial_connect.write(read_msg.encode()) # writing read_msg (the GSM command) to GSM module , then encoding for it to read from sting to unicode char
    time.sleep(2)
    read = serial_connect.read(serial_connect.inWaiting()) # This will read the response from the GSM module, should return any new messages
    time.sleep(2)
    read_m = read.decode() # decoding the message returned from GSM module. ex: this will check what messages have came in (from user)

    while True:

        if "ERROR" not in read_m:
            if '+CMGR: "REC READ","+15598168513"' or '+CMGR: "REC READ", "+15592808913"' in read_m:
                if "START" in read_m:
                    print("ACC ON")
                    GPIO.output(18, GPIO.HIGH)
                    




            if "Red" in de_read:
                print("Led on")
                GPIO.output(18, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(18, GPIO.LOW)
                delete_message()

            elif "+15592808913" in de_read:
                send_message("5592808913", "Whats up")
                print("Sent message")
                delete_message()

            else:
                print("Did not send the right message")
                delete_message()
        else:
            print("No incoming messages")

        time.sleep(1)


    if "OK" in read_m:
        print("It works")
    else:
        print("it didn't work")




def delete_message():
    del_all = "AT+CMGD=,4\r"
    serial_connect.write(del_all.encode())
    time.sleep(2)
    serial_connect.write()
    time.sleep(2)
    if "OK" in read_m:
        return read_
    else:
        print("Didn't work")


def read_serial():
    read = serial_connect.read(serial_connect.inWaiting())

    read_m = read.encode()

    return read_m
a


