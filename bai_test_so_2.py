#viết chương trình nhập vào số nguyên và chia hết cho 3 và 5
n = int(input("Nhập số nguyên: "))
if n % 3 == 0 and n % 5 == 0:
    print("Chia hết cho cả 3 và 5")
else:
    print("Không chia hết cho cả 3 và 5")

