import math
n = int(input("Nhập phần tử : "))
s4 = 0

def s(n):
    if n == 1:
        return math.sqrt(3)
    else:
        return math.sqrt(3 + s(n - 1))

print(s(n))