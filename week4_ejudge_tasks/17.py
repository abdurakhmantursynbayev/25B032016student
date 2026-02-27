
from math import sqrt

r = int(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dx = x2 - x1
dy = y2 - y1
a = dx **2 + dy ** 2
b = 2 * x1 * dx + 2 * y1 * dy
c = x1**2 + y1 ** 2 - r ** 2
D = pow(b, 2) - 4 * a * c
if D <= 0:
    print(f"{0:.10f}")
else:
    t1 = (-b + sqrt(D)) / (2 * a)
    t2 = (-b - sqrt(D)) / (2 * a)
    left = max(0, min(t1, t2))
    right = min(1, max(t1, t2))
    ab = sqrt((dx) ** 2 + (dy) ** 2)    
    if left < right:
        length = (right - left) * ab
        print(f"{length:.10f}")
    else:
        print(f"{0:.10f}")
