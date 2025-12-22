w = float(input("nhập vào chiều rộng hình chữ nhât: "))
h = float(input("nhập vào chiều cao hình chữ nhật: "))
if 0.0 <= w and h <= 100.0:
    print(f"Diện tích hình chữ nhật là: {w * h}")
    print(f"Chu vi hình chữ nhật là: {(w + h) * 2}")
