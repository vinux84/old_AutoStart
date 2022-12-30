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

from machine import UART, Pin
import utime

gsm_uart = machine.UART(0)                                                                                                  # Choose UART # on pins on pico. chose 0 uart
start_pin = machine.Pin(15, machine.Pin.OUT)                                                                                # this can be any pin. put down pin 15 as a example. this pin will be hot for car to start
list_of_users = []
data = 'Start'
config_settings = 'Config'


def read_message():                                                                                                         # this function should work on its own,
    read_incoming_message = 'AT+CMGR=0\r'                                                                                   # without user input. part of message query? # assigning GSM command to a variable
    gsm_uart.write(read_incoming_message.encode())                                                                          # passing that variable(command) to UART pin and encoding from python string to send to GSM module. 
    utime.sleep(2)                                                                                                          # Waiting for response from GSM module
    read_response = gsm_uart.read()                                                                                         # Reading response from GSM                               
    received_message =  read_response.decode()                                                                              # storing in a variabel to be passed and decode to python string
    return received_message                                                                                                 # return stored variable - this message will be from user saying "Start" - this will connect to pin hardcode after functions

def send_message(phone_number, msg):                                                                                        # this function will send message to user for confirmation of start. needs to check with car first. 
    phone_num = f'AT+CMGS="+1{phone_number}"\r'                                                                             # gsm command with desired users phone number. stored in a variable 
    msg_data = f'{msg}\r'                                                                                                   # this is the message the GSM will send to user. for example "Car has started"
    gsm_uart.write(phone_num.encode())                                                                                      # users phone number sent to GSM to send message to user. this phone number will be harcoded later after stated functions
    utime.sleep(2)                                                                                                          # wait for response
    gsm_uart.write(msg_data.encode())                                                                                       # GSM module now ready for message - send message to user
    utime.sleep(2)
    check_response = gsm_uart.read()                                                                                        # Read the response from the GSM module to see if sent message is successful. 
    sent_status = check_response.decode()                                                                                   # decoding and storing response in variable to pass to error handler in case the sent message doens't go through
    return sent_status                                                                                                      # check to see confirmation of message successful. return in a variable for later use?

def delete_message():
    delete_all_messages = 'AT+CMGD=,4\r'                                                                                    # command to delete messages
    gsm_uart.write(delete_all.encode())                                                                                     # sending command to delete all messages
    utime.sleep(2)
    check_del_response = gsm_uart.read()                                                                                    # checking whether delete messages was successful
    delete_status = check_del_response.decode()                                                                             # decoding delete responde status
    return delete_status                                                                                                    # passing variable

def configuration(user_phone):
    number_input = 'Entered Configuration Mode: Please reply back with user phone number within 5 minutes'
    request_num = send_message(user_phone, number_input)
    # have some way to confirm message was sent? maybe just for R&D phase, no point in adding a confirm message to gsm module
    
    #while:
        
        
def get_phone_number(message_query):
    find_phone_number = message_query.find('","+1')
    begin_index = find_phone_number + 5
    end_index = begin_index + 10
    parsed_phone_number = (message_query[begin_index:end_index])
    return parsed_phone_number
    

                                                                                              # this needs to be while true to keep checking to see if new messages came in

message_query = read_message() # should this be in the while loop?
                                                                                                                            # example_string = '+CMGR: "REC READ","+15598168513"'
    
while True:
    
    message_query
    if data in message_query:
        if len(list_of_users) == 0:
            configuration()
        elif len(list_of_users) > 0:
            for find_number in list_of_users:
                if find_number in message_query:
                    phone_number = find_number
                    start_pin.value(1)                                                         
                # need some sort of confirmation from car proving the car started, then
                    start_pin.value(0)
                    confirm_sent = send_message(phone_number, 'Started')                                                       # once proven that it has started send message back to user confirming it has started
                    confrim_sent                                                                                               # need a error handler/raise exception to handle error in case sent message doesn't work. possibly sending message back to user saying it did not go through
    elif config_settings in message_query:
        user_phone = get_phone_number(message_query)
        user_response = configuration(user_phone)
    else:
        pass                                                                                                                   # end block of code if messsage is not "Start". There may not be a reason for thie else:pass, need to find out



# things left to figure out:

# 1. Can you choose to just read unread messages on gsm command? if you did so, you wouldn't have to delete all messages so often. IF not delete_message() needs to be inside read_message first thing
# 2. Is there a better way to constantly query the GSM messages then to just keep calling read_message over and over? would this take up a lot of memory
# 3. Handling and raising exceptions to confirm messages have come through.
# 4. How will the GSM know what message to send back to. 


