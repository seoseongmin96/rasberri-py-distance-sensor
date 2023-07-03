import serial
import threading
import time
from datetime import datetime

import pandas as pd 

ser = serial.Serial(
        port= '/dev/ttyUSB0',
        baudrate= 57600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 
)


def inch2cm(num):
    return round(int(num) * 2.54, 2)

def readthread(low, high):  
    df = pd.DataFrame(columns=["time", "distance", "Exists"])
    for i in range(low, high):
        data = ser.read(size=1)
        if data == b'R':
            data = ser.read(size=3)
            distance = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"{inch2cm(data.decode())}cm")
            row = {"distance": distance[1], "time" : distance[0]}

        elif data == b'P':
            data = ser.read(size=1)
            if data == b'1':
                row["Exists"] = "있음"
                print(f"{distance[0]}, {distance[1]}, 있음")
            elif data == b'0':
                row["Exists"] = "없음"
                print(f"{distance[0]}, {distance[1]}, 없음")

            df.loc[len(df)] = row

            df.to_csv('distance.csv', index=False, mode='w')
            
thread = threading.Thread(target=readthread, args=(1, 10000))
thread.start()



# def main():
#     while True:
#         #print("Hello")
#         time.sleep(1)
# main()





    










