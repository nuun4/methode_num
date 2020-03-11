from math import pi

r = 10.6
area_circle = pi*(r**2)

a = 1.3
b = 0
area_rectangle = a*b

while area_rectangle < area_circle:
    b += 1
    area_rectangle = a*b
    
b -= 1
print(b)