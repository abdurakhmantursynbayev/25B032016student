import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dx = x2 - x1
dy = y2 - y1
t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)
if t < 0:
    px, py = x1, y1
elif t > 1:
    px, py = x2, y2
else:
    px = x1 + t*dx
    py = y1 + t*dy
dist_to_segment = math.hypot(px, py)
if dist_to_segment >= r:
    ans = math.hypot(dx, dy)
else:
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)
    l1 = math.sqrt(d1*d1 - r*r)
    l2 = math.sqrt(d2*d2 - r*r)
    alpha1 = math.acos(r / d1)
    alpha2 = math.acos(r / d2)
    cos_delta = (x1*x2 + y1*y2) / (d1*d2)
    delta = math.acos(cos_delta)
    phi = delta - alpha1 - alpha2
    ans = l1 + l2 + r * phi
print(f"{ans:.10f}")