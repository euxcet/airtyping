from leap import Leap

class Gesture():
    def __init__(self):
        self.GESTURE_TYPE = "ANY"

    def __str__(self):
        return "Gesture"

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return True
        return False

class DeleteLetterGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "DELETELETTER"
        self.timestamp = timestamp

    def __str__(self):
        return "<DeleteLetter Gesture> timestamp: %.5f" % self.timestamp

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return True
        if (gesture.GESTURE_TYPE == "CONFIRM"):
            return True
        return False

class DeleteWordGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "DELETEWORD"
        self.timestamp = timestamp

    def __str__(self):
        return "<DeleteWord Gesture> timestamp: %0.5f" % self.timestamp

class KeyTapGesture(Gesture):
    def __init__(self, position, timestamp):
        self.GESTURE_TYPE = "KEYTAP"
        self.position = position
        self.timestamp = timestamp

    def __str__(self):
        return "<KeyTap Gesture> timestamp: %.5f position: (%.4f, %.4f)" % (self.timestamp , self.position[0], self.position[2])

class ConfirmGesture(Gesture):
    def __init__(self, timestamp):
        self.GESTURE_TYPE = "CONFIRM"
        self.timestamp = timestamp

    def __str__(self):
        return "<Confirm Gesture> timestamp: %.5f" % self.timestamp

    def conflict(self, gesture):
        if (gesture.GESTURE_TYPE == self.GESTURE_TYPE):
            return True
        if (gesture.GESTURE_TYPE == "DELETELETTER"):
            return True
        return False
