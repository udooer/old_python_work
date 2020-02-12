#!/usr/bin/env python3
import time
import serial
import argparse
import datetime 
import pandas as pd 

#### Get command line argument ####
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

#### Set the serial configuration ####
ser = serial.Serial(
        port = port,
        baudrate = baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
#### Report list ####
reports = []

#### define function parse_data ####
def parse_data(x):
    x_split = x.split(',')

    data = x_split[0][8:]
    time_sent = x_split[1][6:-1] 

    time_sent_split = time_sent.split(':')
    time_sent_full = float(time_sent_split[0])*3600 + float(time_sent_split[1])*60 + float(time_sent_split[2])

    time_received = datetime.datetime.utcnow().time()
    time_received_full = (float(time_received.hour)*3600 + float(time_received.minute)*60 + 
                            float(time_received.second) + float(time_received.microsecond)*1e-6)

    time_delay = time_received_full - time_sent_full
    reports.append((x[:-1], data, time_sent, str(time_received), str(time_delay)))
    return 

def main():
    try:
        while 1:
        
            x=ser.readline().decode()
            print(x)
            parse_data(x)

    except KeyboardInterrupt:
        
        df = pd.DataFrame(reports, columns=["raw_data", "counter", "sent_time", "received_time", "time_delay"])
        df.to_csv("reports.csv")

if __name__ == "__main__":
    main()
