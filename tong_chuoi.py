#tính tổng chuỗi s = 1/a + 1/(a+1) + 1/(a+2) + ... + 1/a+n < 0,0001
a = int(input("Nhập a: "))
n = int(input("Nhập n: "))
s = 0
for i in range(n + 1):
    s = s + 1 / (a + i)
    if 1 / (a + i) < 0.0001:
        break
print(f"Tổng chuỗi là: {s}")
