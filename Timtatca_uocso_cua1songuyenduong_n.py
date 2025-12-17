a = int(input("nhập vào số nguyên dương bất kỳ:"))
us = []
for i in range(1, a + 1):
    if a % i == 0:
        us.append(i)
print("các ước số của", a, "là:", us)
print("tổng các ước số của", a, "là:", sum(us))
print("số lượng ước số của", a, "là:", len(us))
print("ước số lớn nhất của", a, "là:", max(us))
print("ước số nhỏ nhất của", a, "là:", min(us))
print("ước số trung bình của", a, "là:", sum(us) / len(us))
