a = float(int(input("nhập vào số a: ")))
b = float(int(input("nhập vào số b: ")))
c = float(int(input("nhập vào số c: ")))

m = a
if b > m:
    m = b
if c > m:
    m = c
print(f"số lớn nhất trong 3 số {a}, {b}, {c} là: {m}")

n = a
if b < n:
    n = b
if c < n:
    n = c
print(f"số nhỏ nhất trong 3 số {a}, {b}, {c} là: {n}")