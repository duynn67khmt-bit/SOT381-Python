import math

def kiem_tra_vi_tri(x, y, x0, y0, r):
    khoang_cach_binh_phuong = (x - x0) ** 2 + (y - y0) ** 2
    r_binh_phuong = r ** 2
    # So sánh
    if khoang_cach_binh_phuong < r_binh_phuong:
        return "Điểm nằm TRONG hình tròn."
    elif khoang_cach_binh_phuong == r_binh_phuong:
        return "Điểm nằm TRÊN vành tròn."
    else:
        return "Điểm nằm NGOÀI hình tròn."
if __name__ == "__main__":
    print("--- KIỂM TRA ĐIỂM THUỘC HÌNH TRÒN ---")

    try:
        # Nhập dữ liệu
        print("Nhập tọa độ tâm I(x0, y0):")
        x0 = float(input("x0 = "))
        y0 = float(input("y0 = "))

        r = float(input("Nhập bán kính R: "))
        if r < 0:
            print("Bán kính không thể âm!")
            exit()

        print("Nhập tọa độ điểm M(x, y) cần kiểm tra:")
        x = float(input("x = "))
        y = float(input("y = "))

        # Gọi hàm kiểm tra
        ket_qua = kiem_tra_vi_tri(x, y, x0, y0, r)

        # In kết quả
        print("-" * 30)
        print(f"Kết quả: {ket_qua}")
        print("-" * 30)

    except ValueError:
        print("Lỗi: Vui lòng nhập số thực hợp lệ.")