n = int(input("nhập vào số phần tử của dãy Fibonacci: "))
f1, f2 = 0, 1
c  = 0
print("dãy Fibonacci có", n, "phần tử là:")
while c < n:
    print(f1, end=' ')
    fn = f1 + f2
    f1 = f2
    f2 = fn
    c += 1
print()
