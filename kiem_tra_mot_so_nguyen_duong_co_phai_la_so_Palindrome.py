chuoi_xuoi = a = int(input("nhập vào số nguyên dương bất kì: "))
chuoi_nguoc = chuoi_xuoi[::-1]
if chuoi_xuoi == chuoi_nguoc:
    print(f"Số {a} là số Palindrome")
else:
    print(f"Số {a} không phải là số Palindrome")
