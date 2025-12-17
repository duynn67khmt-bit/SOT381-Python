a = int(input("Nhập số a: "))
result = ""
while (a != 0):
    result += str(a % 10)
    a = a // 10
print("Số đảo ngược là:", result)

