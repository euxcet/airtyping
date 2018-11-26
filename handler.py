from leap import Leap
import time
from gesture import *
from gestureseq import *

'''
    frame: hands
    hands: is_empty, frontmost, leftmost, rightmost
'''

class Handler():
    def __init__(self):
        self.lastSwipeStart = dict()

    def detectSwipe(self, swipe):
        # only accept swiping righthand
        hand = swipe.pointable.hand
        finger = swipe.pointable.id
        start = swipe.start_position
        startDict = self.lastSwipeStart

        # refuse: swipe left hand
        if (hand != self.righthand):
            return

        # refuse: swipe right hand to the right
        if (swipe.position[0] - swipe.start_position[0] > -150):
            return

        if (not (finger in startDict) or startDict[finger] != start):
            startDict[finger] = start
            GestureSeq().insertGesture(SwipeGesture(time.time()))

    def detectKeyTap(self, keytap):
        hand = keytap.pointable.hand
        finger = keytap.pointable.id
        start = keytap.start_position
        startDict = self.lastSwipeStart

        if (keytap.position[1] - keytap.start_position[1] > -80 or
            abs(keytap.position[0] - keytap.start_position[0]) > 50 or
            abs(keytap.position[2] - keytap.start_position[2]) > 50):
            return

        if (not (finger in startDict) or startDict[finger] != start):
            #print keytap.position
            #print keytap.start_position
            #print
            startDict[finger] = start
            GestureSeq().insertGesture(KeyTapGesture(hand.palm_position, time.time()))

    def detectScreenTap(self, screentap):
        print "Screen Tap:"
        print "position:  ", screentap.position
        print "direction: ", screentap.direction
        print "pointable: ", screentap.pointable
        print "progress:  ", screentap.progress
        print ""


    def handle(self, controller):
        frame = controller.frame()
        hands = frame.hands
        self.lefthand = hands.leftmost
        self.righthand = hands.rightmost

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                self.detectSwipe(Leap.SwipeGesture(gesture))
                self.detectKeyTap(Leap.SwipeGesture(gesture))
            #if gesture.type is Leap.Gesture.TYPE_KEY_TAP:
                #self.detectKeyTap(Leap.KeyTapGesture(gesture))
            #if gesture.type is Leap.Gesture.TYPE_SCREEN_TAP:
                #self.detectScreenTap(Leap.ScreenTapGesture(gesture))
