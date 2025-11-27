from typing import Tuple

def triangle_area(a: Tuple[float, float],
                  b: Tuple[float, float],
                  c: Tuple[float, float]) -> float:
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    det = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
    return abs(det) / 2.0

def is_collinear(a, b, c, eps=1e-12):
    return triangle_area(a,b,c) <= eps

if __name__ == "__main__":
    print("Nhập 3 điểm A, B, C (mỗi dòng: x y):")
    ax, ay = map(float, input("A: ").split())
    bx, by = map(float, input("B: ").split())
    cx, cy = map(float, input("C: ").split())

    A = (ax, ay); B = (bx, by); C = (cx, cy)
    area = triangle_area(A, B, C)
    if is_collinear(A,B,C):
        print("Ba điểm thẳng hàng — diện tích = 0")
    else:
        print(f"Diện tích tam giác = {area}")
