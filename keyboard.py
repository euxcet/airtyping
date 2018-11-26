import math
class Key():
    '''
      ---- up
      |  |
 left |  | right
      ---- bottom
    '''
    def __init__(self, left, top, width, height, char):
        self.left = left
        self.top = top
        self.right = left + width
        self.bottom = top + height

        self.center_x = left + width * 0.5
        self.center_y = top + height * 0.5
        self.center = (self.center_x, self.center_y)
        self.charcter = char

    def contains(self, pos):
        return self.left <= pos[0] < self.right and self.top <= pos[1] < self.bottom


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
        '''
        x: -150 ~ 220
        y: -100 ~ 150
        '''
        self.left_most = -150.0
        self.right_most = 220.0
        self.top_most = -100.0
        self.bottom_most = 150.0

        self.keyboard_width = self.right_most - self.left_most
        self.keyboard_height = self.bottom_most - self.top_most
        self.key_width = self.keyboard_width / 10
        self.key_height = self.keyboard_height / 3
        self.key_size = (self.key_width, self.key_height)

        '''
        self.height_up = (-100.0, -15.0)
        self.height_mid = (-15.0, 70.0)
        self.height_down = (70.0, 150.0)
        '''
        self.upKeys = "qwertyuiop"
        self.midKeys = "asdfghjkl"
        self.downKeys = "zxcvbnm"

        self.scope = dict()
        for i in xrange(0, 10):
            self.scope[self.upKeys[i]] = Key(i, 0.0, 1.0, 1.0, self.upKeys[i])
        offset = 1.0 / 3
        for i in xrange(0, 9):
            self.scope[self.midKeys[i]] = Key(i + offset, 1.0, 1.0, 1.0, self.midKeys[i])
        for i in xrange(0, 7):
            self.scope[self.downKeys[i]] = Key(i + offset * 2, 2.0 , 1.0, 1.0, self.downKeys[i])


        '''
        for i in range(0, 10):
            width = (370.0 / 10 * i - 150, 370.0 / 10 * (i + 1) - 150)
            self.scope[self.upKeys[i]] = (width, self.height_up)
        for i in range(0, 9):
            width = (370.0 / 9 * i - 150, 370.0 / 9 * (i + 1) - 150)
            self.scope[self.midKeys[i]] = (width, self.height_mid)
        for i in range(0, 7):
            width = (370.0 / 7 * i - 150, 370.0 / 7 * (i + 1) - 150)
            self.scope[self.downKeys[i]] = (width, self.height_down)
        '''


    def getRelCoordinate(self, pos):
        return ((pos[0] - self.left_most) / self.key_width, (pos[1] - self.top_most) / self.key_height)
    def getAbsCoordinate(self, pos):
        return (self.left_most + pos[0] * self.key_width, self.top_most + pos[1] * self.key_height)

    '''
        p0, p1: (x, y)
    '''
    def calc(self, p0, p1):
        dis = ((p0[0] - p1[0]) * (p0[0] - p1[0]) + (p0[1] - p1[1]) * (p0[1] - p1[1])) * 3.5
        return math.exp(-1./2 * dis)

    '''
        position: (x, y)
        char: chr
    '''

    def getAbsProb(self, position, char):
        return self.calc(self.getRelCoordinate(position), self.scope[char].center)

    def getRelProb(self, cur_pos, last_pos, cur_char, last_char):
        def sub(p1, p0):
            return (p1[0] - p0[0], p1[1] - p0[1])

        return self.calc(sub(self.getRelCoordinate(cur_pos), self.getRelCoordinate(last_pos)),\
                sub(self.scope[cur_char].center, self.scope[last_char].center))
