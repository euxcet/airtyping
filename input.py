import sys
import time
from leap import Leap
from listener import Listener
from gesture import *
from gestureseq import *
from inputparser import *
from tkinter import *
from registration import *

def main():

    controller = Leap.Controller()

    # Enable swipe gesture
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.config.set("Gesture.Swipe.MinLength", 40.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 40)
    controller.config.save()

    listener = Listener()
    controller.add_listener(listener)

    keyboard = Registration().register()
    parser = Parser(keyboard)
    parser.run()
    #Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == '__main__':
    main()
