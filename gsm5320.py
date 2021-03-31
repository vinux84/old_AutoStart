import time
import serial

serial_connect = serial.Serial(port="/dev/ttyUSB3", baudrate=115200, timeout=3)

class GsmCommand:

    def __init__(self):
        pass

    def send_message(self, phone_number, msg):
        phone_num = f'AT+CMGS="+1{phone_number}"\r'
        msg_data = f"{msg}"
        serial_connect.write(phone_num.encode())
        time.sleep(2)
        serial_connect.write(msg_data.encode())
        time.sleep(2)
        read = serial_connect.read(serial_connect.inWaiting())
        read_m = read.decode()
        return read_m

    def read_message(self):
        read_msg = "AT+CMGR=0\r"
        serial_connect.write(read_msg.encode())
        time.sleep(2)
        read = serial_connect.read(serial_connect.inWaiting())
        time.sleep(2)
        read_m = read.decode()
        return read_m

    def delete_messages(self):
        del_all = "AT+CMGD=,4\r"
        serial_connect.write(del_all.encode())
        time.sleep(2)
        read = serial_connect.read(serial_connect.inWaiting())
        read_m = read.decode()
        return read_m


class Ignition:

    pass


