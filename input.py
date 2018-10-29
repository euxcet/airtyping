import sys
from leap import Leap
from listener import Listener

def main():
    controller = Leap.Controller()

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
