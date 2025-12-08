sotien = int(input("Nhập số tiền gửi (VNĐ): "))
ls = float(input("Nhập lãi suất hàng năm (%): "))
kyhan = int(input("Nhập kỳ hạn gửi (tháng): "))

laisuat = (sotien * ls * kyhan) / (100 * 12)
tongtien = sotien + laisuat
print(f"Lãi suất bạn nhận được sau {kyhan} tháng là: {laisuat:.2f} VNĐ")
print(f"Tổng số tiền bạn có sau {kyhan} tháng là: {tongtien:.2f} VNĐ")
