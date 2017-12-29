def  a(x):
	if x>=0:
		return x
	else :
		return -x
print(a(-9))
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a,b,c):
	x1 = (-b/2*a+math.sqrt(b*b-4*a*c)/2*a)
	x2 = (-b/2*a-math.sqrt(b*b-4*a*c)/2*a)
	return x1,x2
print(quadratic(1,-2,1))