import sys
import time
from leap import Leap
from listener import Listener
from dataseq import *

def main():

    controller = Leap.Controller()

    listener = Listener()
    controller.add_listener(listener)

    print "Which finger do you want to record: ",
    finger = int(raw_input())
    print "Finger: ", finger

    f = open("test.out", "a")
    #Keep this process running until Enter is pressed
    tot = 0
    while (True):
        tot = tot + 1
        inp = sys.stdin.readline()
        if (len(inp) > 0 and inp[0] == 's'):
            break
        data = DataSeq().getData()
        print tot
        print data
        print >> f, len(data),
        for d in data:
            print >> f, d,
        print >> f, finger
        if (tot == 100):
            break
    f.close()

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == '__main__':
    main()
