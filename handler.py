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
        self.fistValidL = True
        self.fistValidR = True
        self.fingerY = [[[], [], [], [], []],  [[], [], [], [], []] ]

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


    def detectMakeAFist(self, hand, lr):
        s = 0
        for i in xrange(0, 5):
            s = s + hand.palm_position.distance_to(hand.fingers[i].tip_position)

        for i in xrange(0, 5):
            for j in xrange(i + 1, 5):
                s = s + hand.fingers[j].tip_position.distance_to(hand.fingers[i].tip_position)

        if (s < 800 and hand.sphere_radius < 70):
            if (lr == 0):
                if (self.fistValidL == True):
                    print "left hand make a fist"
                    GestureSeq().insertGesture(SelectNextGesture(time.time()))
                self.fistValidL = False
            else:
                if (self.fistValidR == True):
                    print "right hand make a fist"
                    GestureSeq().insertGesture(ConfirmGesture(time.time()))
                    #GestureSeq().insertGesture(SelectNextGesture(time.time()))
                self.fistValidR = False

        if (s > 900):
            if (lr == 0):
                self.fistValidL = True
            else:
                self.fistValidR = True

    def detectFingerTap(self, hand, lr):
        fingers = hand.fingers
        fingerY = self.fingerY
        for i in xrange(0, 5):
            Y = fingerY[lr][i]
            l = len(Y)
            finger = fingers[i]
            curY = finger.tip_position[1]

            if (l == 15):
                s = 0
                for j in xrange(0, l):
                    s = max(s, Y[j] - curY)

                if (s > 35):
                    if (i == 0 and lr == 0):
                        GestureSeq().insertGesture(ConfirmGesture(time.time()))
                    elif (i == 0 and lr == 1):
                        GestureSeq().insertGesture(SelectNextGesture(time.time()))
                    else:
                        GestureSeq().insertGesture(KeyTapGesture(finger.tip_position, time.time(), lr * 5 + i + 1))

            if (l < 15):
                Y.append(curY)
            else:
                for j in xrange(0, l - 1):
                    Y[j] = Y[j + 1]
                Y[l - 1] = curY

    def handle(self, controller):
        frame = controller.frame()
        hands = frame.hands
        self.lefthand = hands.leftmost
        self.righthand = hands.rightmost

        if (len(hands) == 2):
            #self.detectMakeAFist(self.lefthand, 0)
            #self.detectMakeAFist(self.righthand, 1)
            self.detectFingerTap(self.lefthand, 0)
            self.detectFingerTap(self.righthand, 1)

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                pass
                #self.detectDeleteLetter(Leap.SwipeGesture(gesture))
                #self.detectDeleteWord(Leap.SwipeGesture(gesture))
                #self.detectConfirm(Leap.SwipeGesture(gesture))
                #self.detectKeyTap(Leap.SwipeGesture(gesture))
