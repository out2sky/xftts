#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import serial
import struct
import time

class xftts(object):
    def __init__(self,dev='/dev/ttyAMA0', baud = 115200 ):
        self.baud = baud
        self.name = dev
        self.timeout = 60
        self.open()
        #self.sleep()

    def __del__(self):
        if self.Serial.isOpen == True:
            self.Serial.close()
        

    def setBaud(self,baud):
        self.baud = baud
    def setDevName(self,DevName):
        self.name = DevName
    def setTimeout(timeout):
        self.timeout = timeout
    def open(self):
        self.Serial = serial.Serial(self.name,self.baud,timeout=self.timeout)

    def sendCmd(self,cmd):
        hdr = struct.pack('!BHB',0xfd,1,cmd)
        self.Serial.write(hdr)
        return self.Serial.read()
    def isBusy(self):
        self.sendCmd(0x21)
        tag = self.Serial.read()
        if tag == None:
            return False

        if ord(tag)==0x4f:
            return False
        else:
            return True

    def stop(self):
        self.sendCmd(0x02)
    def pause(self):
        self.sendCmd(0x03)
    def play(self):
        self.sendCmd(0x04)	
    def sleep(self):
        self.sendCmd(0x88)
    def wakeup(self):
        self.sendCmd(0xFF)
        
    def say(self,txt):
        #self.wakeup()
        hdr = struct.pack('!BHBB',0xfd,len(txt.encode('gbk'))+2,0x01,0x01)
        buff = hdr + txt.encode('gbk')
        self.Serial.write(buff)
        return ord(self.Serial.read())

if __name__ == "__main__":
    tts = xftts('/dev/ttyUSB0')
    tts.stop()
    tts.say(u"欢迎使用科大讯飞语音朗读系统(串口版)")
    tts.isBusy()
