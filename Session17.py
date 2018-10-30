class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def distance (self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 ) **0.5

    def __str__(self): # override of print
        return "<" + str(self.x) + "," + str(self.y) + ">"


    def __len__(self):
        return 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __lt__(self, other): # less than
        d1 = (self.x ** 2 + self.y ** 2)**0.5
        d2 = (other.x ** 2 + other.y ** 2)**0.5
        return d1<d2


# Instantiate a point object to see that it works

p1 = Point(3, 5)
p2 = Point(5, 6)


