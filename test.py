import math
length = 4
width = 5
hypotenuse = math.sqrt(length**2 + width**2)
theta = math.asin(length / hypotenuse)
print(f"The angle is {theta} radians")