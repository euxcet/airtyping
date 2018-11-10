import Queue

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class GestureSeq():
    def __init__(self):
        self.seq = Queue.Queue()
        self.lastGesture = None

    def empty():
        return self.seq.empty()

    def full():
        return self.seq.full()

    def size():
        return self.seq.qsize()


    def insertGesture(self, gesture):

        if (self.lastGesture != None):
            last = self.lastGesture
            if (gesture.GESTURE_TYPE == last.GESTURE_TYPE):
                gap = gesture.timestamp - last.timestamp
                if (gap < 0):
                    print "Warning: new gesture's timestamp is too small."
                if (gesture.GESTURE_TYPE == "SWIPE" and gap < 0.5):
                    return
                if (gesture.GESTURE_TYPE == "KEYTAP" and gap < 0.25):
                    return

        print "Insert gesture: ", gesture

        self.seq.put(gesture)
        self.lastGesture = gesture

    def getGesture(self):
        if (self.seq.empty()):
            return None
        return self.seq.get()
