x = int(input("nhập vào số x: "))
n = int(input("nhập vào số mũ n: "))

kq = 1
for n in range(1, n + 1):
    kq = kq * x
print("{} mũ {} là: {}".format(x, n, kq))

