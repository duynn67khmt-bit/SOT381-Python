print("Nhập độ dài 3 cạnh")
a = int(input("cạnh 1:"))
b = int(input("cạnh 2:"))
c = int(input("cạnh 3:"))

if a + b <= c:
    print("-> Không phải tam giác (cạnh quá dài)")
elif c**2 == a**2 + b**2:
    print("-> Tam giác Vuông")
elif c**2 > a**2 + b**2:
    print("-> Tam giác Tù")
else:
    print("-> Tam giác Nhọn")