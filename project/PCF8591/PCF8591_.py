#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time


bus = smbus.SMBus(1)
while True:
    bus.write_byte(0x48, 0x44)  # adc 모듈에 값 어떤 채널을 쓸 것인지를 알려주기 위해 write해야 하는데 parameter를 입력
    value = bus.read_byte(0x48) # 어떤 채널을 쓸지 설정하고 그 채널에 연결되어 있는 전압 값을 read함 parameter를 입력
    value = round((3.3 / 255) * value, 2)
    dBA = round(value * 50, 1)
    
    print(f"{dBA} dBA") # read 된 값을 전압값으로 변환해서 print 되게
    time.sleep(0.1)