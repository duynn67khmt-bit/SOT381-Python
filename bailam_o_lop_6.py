n = int(input("nhập vào phần tử n: "))
i = 1
tu = (1 + 2 + 3 + n)
mau = (2 + 4 + 6 + 2*n)
tu = 0
mau = 0

for i in range(1, n+1):
    tu = tu + i
    mau = mau + 2*i
s = tu / mau
print("kết quả là:", s)