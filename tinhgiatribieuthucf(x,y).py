import math

# Danh sách
functions = {
    1: ("f(x,y) = x + y", lambda x, y: x + y),
    2: ("f(x,y) = x*y", lambda x, y: x * y),
    3: ("f(x,y) = x**2 + y**2", lambda x, y: x ** 2 + y ** 2),
    4: ("f(x,y) = (x + y) / (x - y)", lambda x, y: (x + y) / (x - y) if x != y else None),
    5: ("f(x,y) = sqrt(x + y)", lambda x, y: math.sqrt(x + y) if x + y >= 0 else None),
    6: ("f(x,y) = sin(x) * cos(y)", lambda x, y: math.sin(x) * math.cos(y)),
    7: ("f(x,y) = e^(x*y)", lambda x, y: math.exp(x * y)),
    8: ("f(x,y) = log(x*y)", lambda x, y: math.log(x * y) if x * y > 0 else None),
}

def main():
    print("=== DANH SÁCH CÁC BIỂU THỨC f(x,y) ===")
    for key, (desc, _) in functions.items():
        print(f"{key}. {desc}")

    choice = int(input("Chọn số tương ứng với biểu thức: "))

    if choice not in functions:
        print("Lựa chọn không hợp lệ.")
        return

    desc, func = functions[choice]
    print(f"Bạn đã chọn: {desc}")

    x = float(input("Nhập x: "))
    y = float(input("Nhập y: "))

    result = func(x, y)

    if result is None:
        print("Biểu thức không xác định với giá trị bạn nhập (lỗi miền xác định).")
    else:
        print(f"Giá trị f(x,y) = {result}")
if __name__ == "__main__":
    main()
