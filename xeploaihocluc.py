def tinh_dtb_mon(ds_diem_tx, diem_gk, diem_ck):

    tong_tx = sum(ds_diem_tx)
    so_luong_tx = len(ds_diem_tx)
    dtb = (tong_tx + diem_gk * 2 + diem_ck * 3) / (so_luong_tx + 5)
    return round(dtb, 1)  # Làm tròn 1 chữ số thập phân

def xep_loai_hoc_sinh(bang_diem):
    mon_tinh_diem = bang_diem['mon_tinh_diem']
    mon_nhan_xet = bang_diem['mon_nhan_xet']

    # Các điều kiện cơ bản
    min_diem = min(mon_tinh_diem) if mon_tinh_diem else 0
    so_mon_tren_8 = len([d for d in mon_tinh_diem if d >= 8.0])
    so_mon_tren_6_5 = len([d for d in mon_tinh_diem if d >= 6.5])
    tat_ca_nhan_xet_dat = all(nx == 'Đ' for nx in mon_nhan_xet)
    so_mon_nhan_xet_cd = mon_nhan_xet.count('CĐ')
    so_mon_duoi_5 = len([d for d in mon_tinh_diem if d < 5.0])

    # 1. Xếp loại TỐT
    if tat_ca_nhan_xet_dat and min_diem >= 6.5 and so_mon_tren_8 >= 6:
        return "TỐT"

    # 2. Xếp loại KHÁ (nếu không đạt Tốt)
    elif tat_ca_nhan_xet_dat and min_diem >= 5.0 and so_mon_tren_6_5 >= 6:
        return "KHÁ"

    # 3. Xếp loại ĐẠT (nếu không đạt Khá)
    elif so_mon_nhan_xet_cd <= 1 and so_mon_duoi_5 <= 1:
        return "ĐẠT"

    # 4. Còn lại
    else:
        return "CHƯA ĐẠT"
# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    print("--- CHƯƠNG TRÌNH TÍNH ĐIỂM VÀ XẾP LOẠI (THÔNG TƯ 22) ---")

    # Danh sách môn học mẫu 
    ds_mon_tinh_diem = ["Toán", "Văn", "Ngoại Ngữ", "KHTN", "Lịch sử & ĐL", "Tin học", "Công nghệ", "GDCD"]
    ds_mon_nhan_xet = ["Thể dục", "Nghệ thuật", "HĐTN-HN", "Nội dung ĐP"]
    ket_qua_tinh_diem = []
    ket_qua_nhan_xet = []

    print("\n>>> NHẬP ĐIỂM CÁC MÔN TÍNH ĐIỂM:")
    for mon in ds_mon_tinh_diem:
        print(f"--- Môn {mon} ---")
        try:
            str_tx = input(f"Nhập các điểm thường xuyên (cách nhau bởi dấu cách): ")
            ds_tx = [float(x) for x in str_tx.split()]
            gk = float(input(f"Nhập điểm giữa kì môn {mon}: "))
            ck = float(input(f"Nhập điểm cuối kì môn {mon}: "))

            dtb = tinh_dtb_mon(ds_tx, gk, ck)
            print(f"-> ĐTB môn {mon}: {dtb}")
            ket_qua_tinh_diem.append(dtb)
        except ValueError:
            print("Lỗi nhập liệu! Vui lòng nhập số hợp lệ.")
            return

    print("\n>>> NHẬP KẾT QUẢ CÁC MÔN ĐÁNH GIÁ BẰNG NHẬN XÉT:")
    print("(Nhập 'D' cho Đạt, 'CD' cho Chưa đạt)")
    for mon in ds_mon_nhan_xet:
        while True:
            kq = input(f"Kết quả môn {mon} (D/CD): ").strip().upper()
            if kq in ['D', 'CD']:
                # Chuẩn hóa về dạng hiển thị tiếng Việt để xử lý logic
                if kq == 'D':
                    ket_qua_nhan_xet.append('Đ')
                else:
                    ket_qua_nhan_xet.append('CĐ')
                break
            else:
                print("Vui lòng chỉ nhập 'D' hoặc 'CD'.")

    # Tổng hợp dữ liệu
    du_lieu_hoc_sinh = {
        'mon_tinh_diem': ket_qua_tinh_diem,
        'mon_nhan_xet': ket_qua_nhan_xet
    }

    # Xếp loại
    xep_loai = xep_loai_hoc_sinh(du_lieu_hoc_sinh)

    print("\n" + "=" * 40)
    print(f"KẾT QUẢ CUỐI CÙNG: {xep_loai}")
    print("=" * 40)


if __name__ == "__main__":
    main()