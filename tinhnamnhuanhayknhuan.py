year = int(input("nhập năm vào: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("năm nhuận")
else:
    print("không phải năm nhuận")
