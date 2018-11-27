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
        self.history = []

    def empty(self):
        return self.seq.empty()

    def full(self):
        return self.seq.full()

    def size(self):
        return self.seq.qsize()

    def validate(self, gesture):
        if (len(self.history) == 0):
            return True
        for g in self.history:
            gap = gesture.timestamp - g.timestamp
            if (g.conflict(gesture) and gap < 0.25):
                return False
        return True

    def insertGesture(self, gesture):
        if (self.validate(gesture)):
            self.seq.put(gesture)
            self.history.append(gesture)

    def getGesture(self):
        if (self.seq.empty()):
            return None
        return self.seq.get()
