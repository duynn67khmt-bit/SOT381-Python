n = int(input("nhập vào số phần tử n để tính n! : "))
s = 0
giaithua = 1
for i in range(1, n + 1):
    giaithua = giaithua * i
    s = s + giaithua
print("tổng 1! + 2! + 3! + ... + n! là:", s)