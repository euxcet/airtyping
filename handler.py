from leap import Leap
import gesture

'''
    frame: hands
    hands: is_empty, frontmost, leftmost, rightmost
'''

class Handler():
    def __init__(self):
        self.lastSwipeStart = dict()

    def detectSwipe(self, swipe):
        # righthand swipe
        if (swipe.pointable.hand == self.righthand and
            swipe.start_position != self.lastSwipeStart[swipe.pointable]):
            self.lastSwipeStart[swipe.pointable] = swipe.start_position
            if (swipe.position[0] < swipe.start_position[0]):
                GestureSeq().insertGesture(SwipeGesture(time.time()))

    def handle(self, controller):
        frame = controller.frame()
        hands = frame.hands
        self.lefthand = hands.leftmost
        self.righthand = hands.rightmost

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                self.detectSwipe(Leap.SwipeGesture(gesture))
