n = int(input("nhập vào phần tử n: "))
i = 1
def sang_eratosthernes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p ** 2 <= n):
        if (primes[p] == True):
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers
print(sang_eratosthernes(n))
