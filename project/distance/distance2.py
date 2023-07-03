import serial
import threading
import time
from datetime import datetime
import csv
import pandas as pd 



   

ser = serial.Serial(
        port= '/dev/ttyUSB1',
        baudrate= 57600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 
)



alivethread = True




def inch2cm(num):
    return round(int(num) * 2.54, 2)

def readthread(low, high):  
    with open('distance.csv', 'w', encoding='utf-8' ) as f:
        for i in range(low, high):
            data = ser.read(size=1)
            if data == b'R':
                data = ser.read(size=3)
                saved_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"{inch2cm(data)}cm"

            elif data == b'P':
                data = ser.read(size=1)
                if data == b'1':
                    f.write(f"{saved_data[0]}, {saved_data[1]}, 있음 \n")
                    print(f"{saved_data[0]}, {saved_data[1]}, 있음")
                    
                elif data == b'0':
                    f.write(f"{saved_data[0]}, {saved_data[1]}, 없음 \n")
                    print(f"{saved_data[0]}, {saved_data[1]}, 없음")
                f.flush()
            
                


thread = threading.Thread(target=readthread, args=(1, 10000))
thread.start()



# def main():
#     while True:
#         #print("Hello")
#         time.sleep(1)
# main()





    










