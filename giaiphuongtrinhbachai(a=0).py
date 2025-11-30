import cmath
import math

print("giải phương trình bậc hai tổng quát: ax^2 + bx + c = 0")

try:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
except ValueError:
    print("Vui lòng nhập các giá trị số hợp lệ.")
    exit()

# a = 0
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm (0x + 0 = 0).")
        else:
            print("Phương trình vô nghiệm (0x + c != 0).")
    else:
        x = -c / b
        print("Phương trình là phương trình bậc nhất. Có một nghiệm duy nhất: x =", x)
else:

    d = (b**2) - (4*a*c)

    rd = cmath.sqrt(d)
    # Tính hai nghiệm
    x1 = (-b - rd) / (2*a)
    x2 = (-b + rd) / (2*a)
    print(f"Phương trình có hai nghiệm (có thể là nghiệm phức):")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

