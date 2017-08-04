import math

def Square(value):
    return value * value

def Area(radius):
    return radius * radius * math.pi

def Circumference(radius):
    return 2 * radius * math.pi

def Distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print Square(4)
print Area(4)
print Circumference(4)
print Distance(0, 0, 3, 4)
print Distance(0, 0, 5, 12)
