def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
print("Tất cả các số nguyên tố từ 1 đến", n, "là:")
for i in range(2, n ):
    if is_prime(i):
        print(i, end=' ')