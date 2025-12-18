a = int(input("Nhập số giờ :"))
b = int(input("Nhập số phút :"))
c = int(input("Nhập số giây :"))

tong_so_giay = lambda a, b, c: a*3600 + b*60 + c
print("Tổng số giây là:", tong_so_giay(a, b, c), "giây")