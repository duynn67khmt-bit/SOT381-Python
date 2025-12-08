so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]

for i in so_luong:
    if i < 10:
        index = so_luong.index(i)
        print(f"Sản phẩm {ten_san_pham[index]} cần được nhập thêm hàng. Hiện có {i} sản phẩm trong kho.")
