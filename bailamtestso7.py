n_str = input("Nhập vào số n: ")
n = int(n_str)
gt = 1
while True:
    if 0 < n < 10:
        for i in range(1, n + 1):
            gt = gt * i
        print(f"Giai thừa của {n} là: {gt}")
        break
    else:
        print("Nhập lại n (n phải > 0 và < 10)")
        n = int(input("Nhập lại n: "))