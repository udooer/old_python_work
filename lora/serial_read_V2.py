#!/usr/bin/env python3
import time
import serial
import argparse
import datetime

parser = argparse.ArgumentParser(description="setting for serial communication!")
parser.add_argument("--port", required=True, type=str,
        help="this is the serial port chosen", 
        choices=["/dev/ttyS0", "/dev/ttyAMA0", "/dev/ttyUSB0"])
parser.add_argument("--baud", required=True, type=int,
        help="this is the baudrate for UART transmission",
        choices=[1200, 4800, 9600, 19200, 38400, 115200])

args = parser.parse_args()
port = args.port 
baud = args.baud

ser = serial.Serial(
        port = port,
        baudrate = baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:

        x=ser.readline().decode()
        split_x = x.split(',')
        data = split_x[0]
        time_sent = split_x[1][:-1]
        time_sent_hour = float(time_sent[0])
        time_sent_minute = float(time_sent[1])
        time_sent_second = float(time_sent[2]) 

        time_received = datetime.datetime.utctime().time()
        time_received_hour = flaot(time_received.hour)
        time_received_minute = float(time_received.minute)
        time_received_second = float(time_received.second) + float(time_received.microsecond)/1e-6

        print(x)
        print("sent data is {}".format(data))
        print("time_sent is {}".format(time_sent))
        print("time_sent_hour is {}".format(time_sent_hour))
        print("time_sent_minute is {}".format(time_sent_minute))
        print("time_sent_second is {}".format(time_sent_second))


        print("time_received is {}".format(time_received))
        print("time_received_hour is {}".format(time_received_hour))
        print("time_received_minute is {}".format(time_received_minute))
        print("time_received_second is {}".format(time_received_second))
