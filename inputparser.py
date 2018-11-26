import time
from keyboard import *
from gesture import *
from gestureseq import *
from dictionary import *

class Parser():
    def __init__(self):
        self.keyboard = Keyboard()
        self.inputSeq = []
        self.dictionary = Dictionary('dict.txt')

    def deleteTail(self):
        if len(self.inputSeq) > 0:
            self.inputSeq.pop()
            print "Input Sequence Length: " + str(len(self.inputSeq))
        else:
            print "Input Sequence is empty."

    def findInDictionary(self):
        input = self.inputSeq
        kb = self.keyboard

        length = len(input)
        if length == 0:
            return "ERROR: There is no input."

        CONTENT = 0
        PROB = 1
        candidates = [[entry[CONTENT], 100.0 * entry[PROB]] for entry in self.dictionary.entries if len(entry[CONTENT]) >= length]

        for i in xrange(length):
            # absolute position
            maxProb = 0.0
            if i == 0:
                for cddt in candidates:
                    cddt[PROB] *= kb.getAbsProb(input[0], cddt[CONTENT][0])
                    maxProb = max(maxProb, cddt[PROB])
            else:
                for cddt in candidates:
                    cddt[PROB] *= kb.getRelProb(input[i], input[i - 1], cddt[CONTENT][i], cddt[CONTENT][i - 1])

            def prob_too_small(entry):
                return entry[PROB] < maxProb * 0.01
            filter(prob_too_small, candidates)

        candidates.sort(key = lambda e: e[PROB], reverse = True)
        return ' '.join([entry[CONTENT] for entry in candidates[:5]])

    def parse(self, gesture):
        print gesture.GESTURE_TYPE
        if gesture.GESTURE_TYPE == "SWIPE":
            self.deleteTail()
        elif gesture.GESTURE_TYPE == "KEYTAP":
            raw_position = gesture.position
            position = (raw_position[0], raw_position[2])

            self.inputSeq.append(position)
            kb = self.keyboard

            for ks in kb.scope.values():
                if ks.contains(kb.getRelCoordinate(position)):
                    print "You tap " + ks.charcter + "."
                    break;

            print self.findInDictionary()

    def run(self):
        while True:
            gesture = GestureSeq().getGesture()
            if gesture != None:
                self.parse(gesture)
