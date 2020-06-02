import time
import serial

USB_PORT = "/dev/ttyUSB3"
serial_connect = serial.Serial(USB_PORT, baudrate=115200, timeout=10)

class GsmCommands:

    def __init__(self):  # set text mode?, baudrate, timeout, serial, USBPORT? ? # set_text_mode = "AT+CMGF=1\r"
        pass

    def send_message(self, phone_number, msg):
        phone_num = f'AT+CMGS="+1{phone_number}"\r'
        msg_data = f"{msg}"
        serial_connect.write(phone_num.encode())
        time.sleep(2)
        serial_connect.write(msg_data.encode())
        # need some sort of code to raise an error if it doens't say ok on gsm response

    def read_message(self):
        read_msg = "AT+CMGR=0\r"
        read = serial_connect.read(serial_connect.inWaiting())
        if read != "":
            serial_connect.write(read_msg.encode())
            time.sleep(2)
            read = serial_connect.read(serial_connect.inWaiting())
            time.sleep(2)
            read_m = read.decode()
            print(read_m)

    def delete_messages(self):
        del_all = "AT+CMGD=,4\r"
        serial_connect.write(del_all.encode())
        time.sleep(2)
        print("Deleting Messages")


