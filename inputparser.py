from keyboard import *
from gesture import *
from gestureseq import *
from dictionary import *
from math import log
from clicker import *
import os, sys

class Parser():
    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.input = []
        self.inputSeq = []
        self.dictionary = Dictionary('dict_bylength.txt')

        self.clicker = Clicker()
        self.select = 0
        self.punctuation = [',', '.', "Enter", '?', '!', '\"', '-', '\'']

        # print self.findInDictionary()

    def deleteLetter(self):
        if len(self.inputSeq) > 0:
            self.inputSeq.pop()
        else:
            self.clicker.delete()
        '''
            print "Input Sequence Length: " + str(len(seq))
        else:
            print "Input Sequence is empty."
        '''

    def deleteWord(self):
        if len(self.inputSeq) > 0:
            self.inputSeq = []
        elif len(self.input) > 0:
            l = len(self.input[len(self.input) - 1])
            self.clicker.delete(l + 1)
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
        candidates = [[entry[CONTENT], log(entry[PROB])] for entry in self.dictionary.entries[length]]

        for i in xrange(length):
            # absolute position
            if i == 0:
                for cddt in candidates:
                    cddt[PROB] += kb.getAbsProb(input[0], cddt[CONTENT][0])
            else:
                for cddt in candidates:
                    cddt[PROB] += kb.getRelProb(input[i], input[i - 1], cddt[CONTENT][i], cddt[CONTENT][i - 1])


        # def prob_too_small(entry):
        #     return entry[PROB] < maxProb - 100000
        #filter(prob_too_small, candidates)

        def cmp(a, b):
            if a[PROB] > b[PROB]:
                return -1
            if a[PROB] < b[PROB]:
                return 1
            if len(a[CONTENT]) < len(b[CONTENT]):
                return -1
            if len(a[CONTENT]) > len(b[CONTENT]):
                return 1
            return -1

        candidates.sort(cmp)
        return candidates

    def parse(self, gesture):
        #print gesture.GESTURE_TYPE

        if gesture.GESTURE_TYPE == "DELETELETTER":
            self.select = 0
            self.deleteLetter()

        elif gesture.GESTURE_TYPE == "DELETEWORD":
            self.select = 0
            self.deleteWord()

        elif gesture.GESTURE_TYPE == "CONFIRM":
            if len(self.inputSeq) > 0:
                word = self.findInDictionary()[self.select][0]
                self.input.append(word)
                self.clicker.input(word + " ")
                self.inputSeq = []
                self.select = 0
            elif (self.select < len(self.punctuation)):
                punc = self.punctuation[self.select]
                if (punc == "Enter"):
                    self.clicker.newline()
                else:
                    self.clicker.delete()
                    self.clicker.input(punc)

                self.select = 0
            else:
                self.select = 0


        elif gesture.GESTURE_TYPE == "KEYTAP":
            if (self.select > 0):
                self.select = 0
            else:
                raw_position = gesture.position
                position = (raw_position[0], raw_position[2])

                self.inputSeq.append(position)
                kb = self.keyboard
                self.findInDictionary()

        elif gesture.GESTURE_TYPE == "SELECTNEXT":
            self.select += 1

        elif gesture.GESTURE_TYPE == "SELECTPREV":
            if (self.select > 0):
                self.select -= 1

        self.printInput()

    def printInput(self):
        if (sys.platform == "darwin"):
            os.system('clear')
        elif (sys.platform == "win32"):
            os.system('cls')
        print "Inputed:  ",
        for word in self.input:
            print word,

        print

        print "Inputing: ",
        if (len(self.inputSeq) > 0):
            words = self.findInDictionary()
            for i in xrange(0, min(20, len(words))):
                if (i == self.select):
                    print '\033[31m' + ("%d:" % i) + words[i][0] + "   " + '\033[0m',
                    #print '\033[31m' + ("%d:" % i) + words[i][0] + " " + ("%.4f: " % words[i][1]) + "   " + '\033[0m',
                else:
                    print ("%d:" % i) + words[i][0] + "   ",
                    #print ("%d:" % i) + words[i][0] + " " + ("%.4f: " % words[i][1]) + "   ",
        else:
            for i in xrange(0, len(self.punctuation)):
                if (i == self.select):
                    print '\033[31m' + ("%d:" % i) + self.punctuation[i] + "   " + '\033[0m',
                else:
                    print ("%d:" % i) + self.punctuation[i] + "   ",
            print

        print

    def run(self):
        while True:
            gesture = GestureSeq().getGesture()
            if gesture != None:
                self.parse(gesture)
