#!/usr/bin/env python3
# -*- coding:gbk -*-
 
import serial
import struct
import sys

class speak(object):
    def __init__(self):
        self.bate = 9600
        self.name = '/dev/ttyUSB0'
        self.timeout = 15
        self.Serial = serial.Serial(self.name,self.bate,timeout=15)
        self.Serial.open()
        
    def say(self,txt):
            hdr = struct.pack('!BHBB',0xfd,len(txt.encode('gbk'))+2,0x01,0x01)
            buff = hdr + txt.encode('gbk')
            self.Serial.write(buff)
            print(hex(ord(self.Serial.read())))


speak().say("系统5秒后完成关闭！")


        
        
    
