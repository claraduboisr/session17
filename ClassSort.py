from Session17 import Point
import random
# Import class

l = []

p = Point(1, 10)
l.append(p)
p = Point(1, 3)
l.append(p)
p = Point(5, 6)
l.append(p)

# List inside of a list

for i in l:
    print(i, end=", ")
# <1,10>, <1,3>, <5,6>,

print("")
# Next line
print("Let's sort it:")

l.sort()
for i in l:
    print(i, end=", ")
# <1,3>, <5,6>, <1,10>,

print("")
# Next line
print("Let's be random!")
for i in range(0, 10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    p = Point(x, y)
    l.append(p)

for i in l:
    print(i, end=", ")
# <1,3>, <5,6>, <1,10>, <9,6>, <10,10>, <1,7>, <3,6>, <6,6>, <9,8>, <3,3>, <3,10>, <1,10>, <8,10>,

print("")