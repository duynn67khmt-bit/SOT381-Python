import math

a = int(input("nhap so a:"))
b = int(input("nhap so b:"))
c = int(input("nhap so c:"))

if a == 0:
    print("Khong Phai Phuong Trinh Bac Hai")
else:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Phuong Trinh Co 2 Nghiem Phan Biet")
        print("x1=",x1)
        print("x2=",x2)
    elif d==0:
        x = -b/(2*a)
        print("Phuong Trinh Co 1 Nghiem Kep x =",x)
    else:
        print("Phuong Trinh Khong Co Nghiem Thuc (delta < 0)")