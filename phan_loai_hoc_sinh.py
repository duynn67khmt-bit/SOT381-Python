diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]

for i in diem_so:
    if i >= 9:
        print(f"Điểm {i}: Học sinh loại Xuất sắc")
    elif i >= 8:
        print(f"Điểm {i}: Học sinh loại Giỏi")
    elif i >= 6.5:
        print(f"Điểm {i}: Học sinh loại Khá")
    elif i >= 5:
        print(f"Điểm {i}: Học sinh loại Trung bình")
    else:
        print(f"Điểm {i}: Học sinh loại Yếu")
