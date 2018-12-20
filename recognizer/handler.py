from leap import Leap
import time
import math
from dataseq import *

class Handler():
    def __init__(self):
        pass


    def handle(self, controller):
        frame = controller.frame()
        hands = frame.hands

        data = []

        if (len(hands) == 1):
            hand = hands[0]

            palm = hand.palm_position

            data = data + [palm[0], palm[1], palm[2]]
            fingers = hand.fingers
            for finger in fingers:
                tip = finger.stabilized_tip_position
                data = data + [tip[0], tip[1], tip[2]]

                for boneid in xrange(0, 4):
                    bone = finger.bone(boneid)
                    data = data + [bone.center[0], bone.center[1], bone.center[2]]

            DataSeq().setData(data)
