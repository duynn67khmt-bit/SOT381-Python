import math
a = float(int(input("nhập độ dài cạnh a: ")))   
b = float(int(input("nhập độ dài cạnh b: ")))
c = float(int(input("nhập độ dài cạnh c: ")))   
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác là:", S)