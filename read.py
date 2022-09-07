#!/usr/bin/env python
#coding:utf-8
from xftts import xftts
import time

fp = open('book.txt','r')
tts = xftts('/dev/ttyUSB0')

for line in fp:
    txt = line.decode('utf-8')
    #print(type(txt))
    tts.say(txt)
    while tts.isBusy():
        time.sleep(0.1)
