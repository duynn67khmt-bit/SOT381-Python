a = int(input("Nhập vào một sô nguyên dương: "))
dem = 0

while a > 10:
    dem += 1
    a = a// 10

print("Số lượng chữ số là:", dem + 1)
