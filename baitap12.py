import math
n = -1
while (n < 0):
    n = int(input("Nhập số n>0: "))


x = n
result = ""
while(n>0):
    result =str(n%2) + result
    n = n//2
print("Số nhị phân là:", result) 
    