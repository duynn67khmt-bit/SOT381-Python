year = int(input("nhập năm vào: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Năm", year, "có 366 ngày")
else:
    print("Năm", year, "có 365 ngày")
