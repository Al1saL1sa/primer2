import math
print("Enter legs")
a = int(input("a: "))
b = int(input("b: "))
c = math.sqrt(a**2 + b**2) + a + b
print('%.3f' % c)
