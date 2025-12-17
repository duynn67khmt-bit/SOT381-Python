print("v: hình vuông")
print("t: hình tam giác vuông cân")
print("hcn: hình chữ nhật")

a = str(input("Nhập vào hình muốn vẽ: "))

n = int(input("Nhập vào kích thước hình: "))
if a == "v":
    for i in range(n):
        print("* * " * n)
elif a == "t":
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
elif a == "hcn":
    for i in range(n):
        print("* " * n)
else:
    print("Hình không hợp lệ")