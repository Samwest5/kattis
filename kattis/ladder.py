from math import sin, radians, ceil

height, angle = [int(x) for x in input().split()]

print(int(ceil(height / sin(radians(angle)))))