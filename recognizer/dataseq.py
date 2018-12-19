def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class DataSeq():
    def __init__(self):
        self.data = []

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
