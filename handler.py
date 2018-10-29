from leap import Leap

'''
    frame: hands
    hands: is_empty, frontmost, leftmost, rightmost
'''

class Handler():
    def handle(self, controller):
        frame = controller.frame()
        hands = frame.hands
        lefthand = hands.leftmost
        righthand = hands.rightmost

        pointable = frame.pointables.frontmost
        direction = pointable.direction
        length = pointable.length
        width = pointable.width
        leapPoint = pointable.stabilized_tip_position
