import math as m

a = float(input("nhập dộ dài cạnh a: "))
b = float(input("nhập độ dài cạnh b: "))
c = float(input("nhập độ dài cạnh c: "))
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Ba cạnh a, b, c không thể tạo thành một tam giác.")
    exit()
else:
    print(f"độ dài các cạnh tam giác là: a={a}, b={b}, c={c}")
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"Diện tích tam giác là: S={S}")
print(f'Chu vi tam giác là: P={2*p}')

