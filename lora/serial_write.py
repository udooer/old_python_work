#!/usr/bin/env python3
import time
import serial
import datetime
ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

while 1:
    time_s = str(datetime.datetime.utcnow().time())
    counter_s = str(counter)
    send_data = "counter=" + counter_s + ", " + "time=" + time_s + '\n'
    ser.write(send_data.encode())
    time.sleep(1)
    counter += 1
