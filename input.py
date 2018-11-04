import sys
import time
from leap import Leap
from listener import Listener
from gesture import *
from gestureseq import *

def main():
    controller = Leap.Controller()

    GestureSeq().insertGesture(SwipeGesture(time.time()))
    GestureSeq().insertGesture(SwipeGesture(time.time()))
    print GestureSeq().getGesture()
    print GestureSeq().getGesture()


    #Enable swipe gesture
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.config.set("Gesture.Swipe.MinLength", 40.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 500)
    controller.config.save()

    listener = Listener()
    controller.add_listener(listener)

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
