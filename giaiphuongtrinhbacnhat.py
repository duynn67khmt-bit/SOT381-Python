a = int(input("nhap so a:"))
b = int(input("nhap so b:"))

if a != 0:
    x = -b / a
    print("Nghiem duy nhat:", x)
else:
    if b == 0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")