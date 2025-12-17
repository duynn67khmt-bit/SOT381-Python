dss = []
dem_duong = 0
dem_am = 0


print("hãy nhập 5 số âm dương bất kỳ:")

for i in range(5):
    so = float(input(f"nhập số thứ {i+1}: "))
    dss.append(so)

    if so > 0:
        print(f"số {so} là số dương")
    elif so < 0:
        print(f"số {so} là số âm")

    if so > 0:
        dem_duong += 1
    elif so < 0:
        dem_am += 1
    print("-" * 30)
    print(f"Tổng số dương: {dem_duong}")
    print(f"Tổng số âm: {dem_am}")