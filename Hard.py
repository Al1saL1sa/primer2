print("Выедите числа")
a = int(input("a1 = "))
a2 = int(input("a2 = "))
a3 = int(input("a3 = "))
b = int(input("b1 = "))
b2 = int(input("b2 = "))
t2 = (a + b) // 10
t3 = (a2 + b2 + t2) // 10
f1 = a3 + t3
f2 = (a2 + b2 + t2) % 10
f3 = (a + b) % 10
print(f1, f2, f3)