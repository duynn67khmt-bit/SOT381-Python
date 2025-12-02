a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
c = int(input("Nhập số nguyên c:"))

ds = sorted([a, b, c])
n1, n2, ln = ds[0], ds[1], ds[2]

import math

if ln**2 == n1**2 + n2**2:
    print(f"-> ĐÚNG. ({a}, {b}, {c}) là một bộ ba Pytago.")
    if math.gcd(a, math.gcd(b, c)) == 1:
        print("   (Đây còn là bộ ba Pytago nguyên thủy)")
else:
    print(f"-> SAI. ({a}, {b}, {c}) không tạo thành bộ ba Pytago.")