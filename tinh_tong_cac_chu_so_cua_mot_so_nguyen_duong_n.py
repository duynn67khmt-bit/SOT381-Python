n = int(input("nhập một số nguyên dương: "))
chuoi = str(n)
t = 0
i = 0

for i in chuoi:
    t = t + int(i)
print(f"Tổng các chữ số của số {n} là: {t}")