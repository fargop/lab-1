import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
perimeter = a + b + c
p = perimeter / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Периметр: {perimeter:.2f}")
print(f"Площадь: {area:.2f}")
