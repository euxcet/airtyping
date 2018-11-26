from leap import Leap

class Gesture():
    def __init__(self):
        self.GESTURE_TYPE = "ANY"
    def __str__(self):
        return "Gesture"

class SwipeGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "SWIPE"
        self.timestamp = timestamp
    def __str__(self):
        return "<Swipe Gesture> timestamp: " + '%.5f' % self.timestamp

class KeyTapGesture(Gesture):
    def __init__(self, position, timestamp):
        self.GESTURE_TYPE = "KEYTAP"
        self.position = position
        self.timestamp = timestamp
    def __str__(self):
        return "<KeyTap Gesture> timestamp: %.5f position: (%.4f, %.4f)" % (self.timestamp , self.position[0], self.position[2])
