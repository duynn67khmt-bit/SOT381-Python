def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

def tim_bcnn(a, b):
    return (a * b) // tim_ucln(a, b)
try:
    m = int(input("Nhập số m: "))
    n = int(input("Nhập số n: "))

    ucln = tim_ucln(m, n)
    bcnn = tim_bcnn(m, n)

    print(f"Ước chung lớn nhất của {m} và {n} là: {ucln}")
    print(f"Bội chung nhỏ nhất của {m} và {n} là: {bcnn}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")