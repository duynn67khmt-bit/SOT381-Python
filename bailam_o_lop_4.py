a = int(input("Nhập một số nguyên dương: "))
b = int(input("Nhập một số nguyên dương: "))
c = int(input("Nhập một số nguyên dương: "))

def sln(a, b, c):
    ln = a
    if b > ln:
        ln = b
    if c > ln:
        ln = c
    return ln
def snn(a, b, c):
    sn = a
    if b < sn:
        sn = b
    if c < sn:
        sn = c
    return sn
print(f"Số lớn nhất trong ba số là: {sln(a, b, c)}")
print(f"Số nhỏ nhất trong ba số là: {snn(a, b, c )}")

