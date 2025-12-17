ds = []
print("nhập 5 số từ bàn phím:")

for i in range(5):
    so = float(input("nhập số thứ {}: ".format(i + 1)))
    ds.append(so)

tong = sum(ds)
print("tổng của 5 số đã nhập vào là:", tong)
