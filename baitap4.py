import math 
g = 9.81  # gia tốc
h = float(int(input("Nhập chiều cao h (m): ")))
v = math.sqrt(2 * g * h)
print("Vận tốc của vật khi chạm đất là:", v, "m/s")