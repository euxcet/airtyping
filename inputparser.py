from keyboard import *
from gesture import *
from gestureseq import *
from dictionary import *
from math import log

class Parser():
    def __init__(self):
        self.keyboard = Keyboard()
        # self.inputSeq = [(-50, -50), (10, 10), (75, 0)]
        self.input = []
        self.inputSeq = []
        self.dictionary = Dictionary('dict.txt')

        # print self.findInDictionary()

    def deleteLetter(self):
        if len(self.inputSeq) > 0:
            self.inputSeq.pop()
        '''
            print "Input Sequence Length: " + str(len(seq))
        else:
            print "Input Sequence is empty."
        '''

    def deleteWord(self):
        if len(self.inputSeq) > 0:
            self.inputSeq = []
        elif len(self.input) > 0:
            self.input.pop()
        #print "Input Sequence Length: " + str(len(seq))


    def findInDictionary(self):
        input = self.inputSeq
        kb = self.keyboard

        '''
        for position in input:
            for ks in kb.scope.values():
                if ks.contains(kb.getRelCoordinate(position)):
                    print "You tap " + ks.charcter + "."
                    print "x : " + str(ks.left) + " " + str(ks.right) + " y : " + str(ks.top) + " " + str(ks.bottom)
                    break;
        '''

        length = len(input)
        if length == 0:
            return "ERROR: There is no input."

        CONTENT = 0
        PROB = 1
        candidates = [[entry[CONTENT], log(entry[PROB])] for entry in self.dictionary.entries if len(entry[CONTENT]) >= length]

        for i in xrange(length):
            # absolute position
            maxProb = -100000
            if i == 0:
                for cddt in candidates:
                    cddt[PROB] += kb.getAbsProb(input[0], cddt[CONTENT][0])
                    maxProb = max(maxProb, cddt[PROB])
            else:
                for cddt in candidates:
                    cddt[PROB] += kb.getRelProb(input[i], input[i - 1], cddt[CONTENT][i], cddt[CONTENT][i - 1])
                    maxProb = max(maxProb, cddt[PROB])

            def prob_too_small(entry):
                return entry[PROB] < maxProb - 100000
            #filter(prob_too_small, candidates)

        candidates.sort(key = lambda e: e[PROB], reverse = True)
        return candidates
        #return ' '.join([entry[CONTENT] for entry in candidates[:5]])

    def parse(self, gesture):
        #print gesture.GESTURE_TYPE
        if gesture.GESTURE_TYPE == "DELETELETTER":
            self.deleteLetter()

        elif gesture.GESTURE_TYPE == "DELETEWORD":
            self.deleteWord()

        elif gesture.GESTURE_TYPE == "CONFIRM":
            if len(self.inputSeq) > 0:
                self.input.append(self.findInDictionary()[0][0])
                self.inputSeq = []

        elif gesture.GESTURE_TYPE == "KEYTAP":
            raw_position = gesture.position
            position = (raw_position[0], raw_position[2])

            self.inputSeq.append(position)
            kb = self.keyboard


            '''
            for ks in kb.scope.values():
                if ks.contains(kb.getRelCoordinate(position)):
                    print "You tap " + ks.charcter + "."
                    break;
            '''

            self.findInDictionary()
            #print self.findInDictionary()
        self.printInput()

    def printInput(self):
        print "Inputed:  ",
        for word in self.input:
            print word,

        print

        print "Inputing: ",
        if (len(self.inputSeq) > 0):
            print self.findInDictionary()[0][0]
        else:
            print

        print

    def run(self):
        while True:
            gesture = GestureSeq().getGesture()
            if gesture != None:
                self.parse(gesture)
