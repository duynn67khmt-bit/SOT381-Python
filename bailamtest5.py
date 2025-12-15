n = int(input("nhập vào số n bất kì:"))
i = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    elif i % 2 == 0 and i % 3 == 1:
        print(i)
