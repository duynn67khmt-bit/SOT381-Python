a = int(input("nhập vào số dương bất kì: "))

i = 2
print(f"Phân tích số {a} thành các thừa số nguyên tố: ", end="")
while a > 1:
    if a % i == 0:
        print(i, end=" ")
        a = a // i
    else:
        i += 1