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

    # swipe left hand to the left
    def detectDeleteWord(self, swipe):
        # only accept swiping lefthand
        hand = swipe.pointable.hand
        finger = swipe.pointable.id
        start = swipe.start_position
        startDict = self.lastSwipeStart

        # refuse: only one hand available
        if (self.lefthand == self.righthand):
            return

        # refuse: swipe right hand
        if (hand != self.lefthand):
            return

        # refuse: swipe left hand to the right
        if (swipe.position[0] - swipe.start_position[0] > -120):
            return

        if (not (finger in startDict) or startDict[finger] != start):
            startDict[finger] = start
            GestureSeq().insertGesture(DeleteWordGesture(time.time()))


    # swipe right hand to the left
    def detectDeleteLetter(self, swipe):
        # only accept swiping righthand
        hand = swipe.pointable.hand
        finger = swipe.pointable.id
        start = swipe.start_position
        startDict = self.lastSwipeStart

        # refuse: swipe left hand
        if (hand != self.righthand):
            return

        # refuse: swipe right hand to the right
        if (swipe.position[0] - swipe.start_position[0] > -120):
            return

        if (not (finger in startDict) or startDict[finger] != start):
            startDict[finger] = start
            GestureSeq().insertGesture(DeleteLetterGesture(time.time()))


    # swipe right hand to the right
    def detectConfirm(self, swipe):
        hand = swipe.pointable.hand
        finger = swipe.pointable.id
        start = swipe.start_position
        startDict = self.lastSwipeStart

        # refuse: swipe left hand
        if (hand != self.righthand):
            return

        # refuse: swipe right hand to the left
        if (swipe.position[0] - swipe.start_position[0] < 120):
            return

        if (not (finger in startDict) or startDict[finger] != start):
            startDict[finger] = start
            GestureSeq().insertGesture(ConfirmGesture(time.time()))

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
                self.detectDeleteLetter(Leap.SwipeGesture(gesture))
                self.detectDeleteWord(Leap.SwipeGesture(gesture))
                self.detectConfirm(Leap.SwipeGesture(gesture))
                self.detectKeyTap(Leap.SwipeGesture(gesture))
