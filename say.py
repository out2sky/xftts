#!/usr/bin/env python3
# -*- coding:utf-8 -*-
 
from xftts import xftts
import sys


if len(sys.argv) < 2:
    print("need a word")
    #print(hex(ord(tts().sendCmd(0x88))))

else:
    tts = xftts('/dev/ttyUSB0')
    #msg = sys.argv[1].decode('utf-8')
    msg = sys.argv[1]
    tts.say(msg)
