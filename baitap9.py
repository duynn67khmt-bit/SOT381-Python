import math
sotien = float(int(input("Nhập số tiền (VNĐ): ")))

d = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000 ]

print("Phân tách số tiền thành các mệnh giá:")
for menhgia in d:
    soluong = sotien // menhgia
    sotien = sotien % menhgia
    if soluong > 0:
        print(f"{int(soluong)} tờ mệnh giá {int(menhgia)} VNĐ")
print("Số tiền còn lại không thể phân tách:", int(sotien), "VNĐ")

