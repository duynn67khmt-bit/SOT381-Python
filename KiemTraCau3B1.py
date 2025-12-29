print("nhập vào danh sách số nguyên, cách nhau bởi dấu cách:")
ds = list(map(int, input().split()))

for i in ds:
    if i % 2 and i % 3 == 0:
        print(f"{i} là số chia hết 2 và chia hết cho 3")
    else:
        print("không chia hết cho cả 2 và 3")
