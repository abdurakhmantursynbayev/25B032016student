x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
l = x2 - x1
output = (l/ (y1 + y2)) * y1 + x1
print(f"{output:.10f} {0:.10f}")