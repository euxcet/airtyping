import math

class Keyboard():
    def __init__(self):
        '''
width: -150 ~ 220
    up: -150 ~ 220 / 10
    mid: -150 ~ 220 / 9
    down -150 ~ 220 / 7
height: -100 ~ 150
    up:   -100 ~ -15
    mid:   -15 ~ 70
    down:   70 ~ 150
        '''
        self.height_up = (-100.0, -15.0)
        self.height_mid = (-15.0, 70.0)
        self.height_down = (70.0, 150.0)
        self.upKeys = "qwertyuiop"
        self.midKeys = "asdfghjkl"
        self.downKeys = "zxcvbnm"
        self.scope = dict()
        for i in range(0, 10):
            width = (370.0 / 10 * i - 150, 370.0 / 10 * (i + 1) - 150)
            self.scope[self.upKeys[i]] = (width, self.height_up)
        for i in range(0, 9):
            width = (370.0 / 9 * i - 150, 370.0 / 9 * (i + 1) - 150)
            self.scope[self.midKeys[i]] = (width, self.height_mid)
        for i in range(0, 7):
            width = (370.0 / 7 * i - 150, 370.0 / 7 * (i + 1) - 150)
            self.scope[self.downKeys[i]] = (width, self.height_down)

    def calc(self, p0, p1):
        dis = ((p0[0] - p1[0]) * (p0[0] - p1[0]) + (p0[1] - p1[1]) * (p0[1] - p1[1])) / 10000
        return math.exp(-1./2 * dis)

    def getProbability(self, position):
        res = []
        for i in range(0, 26):
            c = chr(ord('a') + i)
            scope = self.scope[c]
            value = 0
            for x in xrange(0, 10):
                for y in xrange(0, 10):
                    px = (scope[0][0] * x + scope[0][1] * (9 - x)) / 9.
                    py = (scope[1][0] * y + scope[1][1] * (9 - y)) / 9.
                    value += self.calc(position, (px, py))
            res.append(value)
        return res
