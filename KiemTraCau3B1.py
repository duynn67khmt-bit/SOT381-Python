print("nhập vào danh sách số nguyên, cách nhau bởi dấu cách:")
ds = list(map(int, input().split()))
print(ds)

for i in ds:
    if i % 2 and i % 3 == 0:
        print(f"{i} là số lẻ và chia hết cho 3")
    else:
        print(f"{i} không phải số lẻ hoặc không chia hết cho 3")
