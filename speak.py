#!/usr/bin/env python3
# -*- coding:gbk -*-
 
import serial
import struct
    
class speak(object):
    def __init__(self):
        self.bate = 9600
        self.name = '/dev/ttyAMA0'
        self.timeout = 15
        self.Serial = serial.Serial(self.name,self.bate,self.timeout)
        self.Serial.open()
        
    def say(self,txt):
            hdr = struct.pack('!BHBB',0xfd,len(txt.encode('gbk'))+2,0x01,0x01)
            buff = hdr + txt.encode('gbk')
            self.Serial.write(buff)
            print(hex(ord(self.Serial.read())))
            return

        
        
    
