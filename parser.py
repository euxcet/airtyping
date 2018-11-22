import time
from keyboard import *
from gesture import *
from gestureseq import *

class Parser():
    def __init__(self):
        self.keyboard = Keyboard()

    def parse(self, gesture):
        print gesture.GESTURE_TYPE
        if (gesture.GESTURE_TYPE != "KEYTAP"):
            return

        position = gesture.position
        prob = self.keyboard.getProbability((position[0], position[2]))

        max = 0
        pos = 0
        for i in range(0, 26):
            if (prob[i] > max):
                max = prob[i]
                pos = i
        print "output",  chr(ord('a') + pos)

    def run(self):
        while(True):
            gesture = GestureSeq().getGesture()
            if (gesture != None):
                self.parse(gesture)
