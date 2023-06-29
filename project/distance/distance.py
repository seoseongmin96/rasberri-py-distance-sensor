import serial
import threading
import time

line = '',

   

ser = serial.Serial(
        port= '/dev/ttyUSB0',
        baudrate= 57600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 
)



alivethread = True



def inch2cm(num):
    return int(num) * 2.54

def readthread(low, high):  
    for i in range(low, high):
        
        data = ser.read(size=1)
        if data == b'R':
            data = ser.read(size=3)
            print(f"측정거리 : {inch2cm(data)}cm")

        if data == b'P':
            data = ser.read(size=1)
            print("boolean 값 :" , data)


        
        
thread = threading.Thread(target=readthread, args=(1, 10000))
thread.start()

def main():
    while True:
        #print("Hello")
        time.sleep(1)
main()





    










