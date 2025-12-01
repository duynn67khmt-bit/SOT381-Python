a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
c = int(input("Nhập số c:"))

# Để tính xem thì ta dùng bất đẳng thức tam giác
if a + b > c and a + c > b and b + c > a:
    print("3 số đã nhập đủ điều kiện thành lập 1 tam giác")
else:
    print('3 số đã nhập không đủ điều kiện thành lập 1 tam giác abc')