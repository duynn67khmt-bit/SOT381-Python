import math
x = int(input("nhập vào x: "))
n = int(input("nhập vào n: "))

s1 = 0
if n>0:
    for i in range(1, n+1):
        s1 = math.sqrt(x + s1)
    print("kết quả s1 là:", s1)

s2 = 0
for i in range(n + 1):
    s2 += (x ** i) / (i +1)
print(s1)
print(s2)