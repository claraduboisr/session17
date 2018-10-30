class Fraction (object):
    def __init__(self, den, num):
        self.x = num
        self.y = den
    def __str__(self):
        return str(self.x) + "/" + str(self.y)
    def __add__(self, other):
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Fraction(x, y)