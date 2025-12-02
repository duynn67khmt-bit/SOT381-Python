x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

if x > 0 and y > 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ I ")
elif x < 0 and y > 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ II")
elif x < 0 and y < 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ III")
elif x > 0 and y < 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ IV")
