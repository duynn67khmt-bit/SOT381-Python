ds = []

for i in range(10):
    so = float(input("Nhập số thứ {}: ".format(i + 1)))
    ds.append(so)
print(ds)
print("số lớn nhất trong danh sách là:", max(ds))
print("số nhỏ nhất trong danh sách là:", min(ds))
