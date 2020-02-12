#!/usr/bin/env python3
import time
import serial
import argparse

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
        x=ser.readline()
        print(x)
