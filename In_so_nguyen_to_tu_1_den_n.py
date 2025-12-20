n = int(input("nhập vào phần tử n: "))
print("Các số nguyên tố từ 1 đến n là :")
i = 1

for i in range(2 , n + 1):
    d = 0
    for k in range(1, i + 1):
        if i % k == 0:
            d += 1
    if d == 2:
        print(i, end = ' ')
print()