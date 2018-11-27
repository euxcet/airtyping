import sys
import time
from leap import Leap
from listener import Listener
from gesture import *
from gestureseq import *
from inputparser import *
from tkinter import *

def main():

    controller = Leap.Controller()

    # Enable swipe gesture
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.config.set("Gesture.Swipe.MinLength", 40.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 40)
    controller.config.save()

    # Enable key tap gesture
    '''
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
    controller.config.set("Gesture.KeyTap.MinDownVelocity", 10)
    controller.config.set("Gesture.KeyTap.HistorySeconds", .1)
    controller.config.set("Gesture.KeyTap.MinDistance", 1.0)
    controller.config.save()
    '''

    # Enable screen tap gesture
    '''
    controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
    controller.config.set("Gesture.ScreenTap.MinForwardVelocity", 1.0)
    controller.config.set("Gesture.ScreenTap.HistorySeconds", .5)
    controller.config.set("Gesture.ScreenTap.MinDistance", 0.1)
    controller.config.save()
    '''

    listener = Listener()
    controller.add_listener(listener)


    parser = Parser()
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
