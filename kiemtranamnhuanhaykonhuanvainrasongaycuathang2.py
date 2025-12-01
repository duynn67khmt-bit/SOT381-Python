year = int(input("nhập năm vào: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("năm nhuận")
    print("Tháng 2 có 29 ngày")
else:
    print("không phải năm nhuận")
    print("Tháng 2 có 28 ngày")