a = int(input("Nhập một số nguyên dương: "))
v = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(v, end=" ")
        v += 1
    print()