from keyboard import *
from gesture import *
from gestureseq import *
from dictionary import *
from math import log
from clicker import *
import time
import os

class Registration():

    def getTap(self, finger):
        while True:
            gesture = GestureSeq().getGesture()
            if (gesture != None and gesture.GESTURE_TYPE == "KEYTAP" and gesture.kind == finger):
                return gesture.position


    def register(self):
        time.sleep(1)
        print "** START REGISTRATION **"
        print "Please tap f by your left hand's index finger."
        f = self.getTap(2)

        print "Please tap j by your right hand's index finger."
        j = self.getTap(7)

        left_most = f[0] - 75
        right_most = j[0] + 75
        top_most = (f[2] + j[2]) / 2 - 30
        bottom_most = (f[2] + j[2]) / 2 + 30
        return Keyboard(left_most, right_most, top_most, bottom_most)
