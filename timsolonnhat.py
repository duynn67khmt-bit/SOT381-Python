try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    c = float(input("Nhập số thứ ba: "))

    # Giả sử a là số lớn nhất ban đầu
    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    print(f"Số lớn nhất là: {largest}")

except ValueError:
    print("Vui lòng nhập số hợp lệ!")