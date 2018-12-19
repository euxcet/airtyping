from leap import Leap

class Gesture():
    def __init__(self):
        self.GESTURE_TYPE = "ANY"

    def __str__(self):
        return "<Gesture>"

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return 0.25
        return 0.0

class DeleteLetterGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "DELETELETTER"
        self.timestamp = timestamp

    def __str__(self):
        return "<DeleteLetter Gesture> timestamp: %.5f" % self.timestamp

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return 0.25
        # if (gesture.GESTURE_TYPE == "CONFIRM"):
        #     return 2.0
        return 0.0

class DeleteWordGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "DELETEWORD"
        self.timestamp = timestamp

    def __str__(self):
        return "<DeleteWord Gesture> timestamp: %0.5f kind: %d" % self.timestamp

class KeyTapGesture(Gesture):
    def __init__(self, position, timestamp, kind):
        self.GESTURE_TYPE = "KEYTAP"
        self.position = position
        self.kind = kind
        self.timestamp = timestamp

    def __str__(self):
        return "<KeyTap Gesture> timestamp: %.5f position: (%.4f, %.4f) kind: %d" % (self.timestamp , self.position[0], self.position[2], self.kind)

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            if (gesture.kind == self.kind):
                return 0.5
            else:
                return 0.25
        return 0.0

class ConfirmGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "CONFIRM"
        self.timestamp = timestamp

    def __str__(self):
        return "<Confirm Gesture> timestamp: %.5f" % self.timestamp

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return 0.25
        # if (gesture.GESTURE_TYPE == "DELETELETTER"):
        #     return 2.0
        return 0.0

class SelectNextGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "SELECTNEXT"
        self.timestamp = timestamp

    def __str__(self):
        return "<SelectNext Gesture> timestamp: %.5f" % self.timestamp

class SelectPrevGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "SELECTPREV"
        self.timestamp = timestamp

    def __str__(self):
        return "<SelectPrev Gesture> timestamp: %.5f" % self.timestamp
