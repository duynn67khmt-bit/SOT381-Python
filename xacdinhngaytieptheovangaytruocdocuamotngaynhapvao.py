def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)


def so_ngay_trong_thang(thang, nam):
    danh_sach_ngay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if la_nam_nhuan(nam):
        danh_sach_ngay[2] = 29

    if 1 <= thang <= 12:
        return danh_sach_ngay[thang]
    return 0


def kiem_tra_hop_le(ngay, thang, nam):
    max_ngay = so_ngay_trong_thang(thang, nam)
    if max_ngay == 0 or ngay < 1 or ngay > max_ngay:
        return False
    return True

def tim_ngay_mai(ngay, thang, nam):
    max_ngay = so_ngay_trong_thang(thang, nam)

    if ngay < max_ngay:
        ngay += 1
    else:
        ngay = 1
        if thang == 12:
            thang = 1
            nam += 1
        else:
            thang += 1
    return ngay, thang, nam


def tim_hom_qua(ngay, thang, nam):
    if ngay > 1:
        ngay -= 1
    else:
        # Nếu là ngày 1
        if thang == 1:
            thang = 12
            nam -= 1
            ngay = 31
        else:
            thang -= 1
            ngay = so_ngay_trong_thang(thang, nam)

    return ngay, thang, nam

def main():
    print("=== TRA CỨU DÒNG THỜI GIAN (HÔM QUA - HÔM NAY - NGÀY MAI) ===")

    while True:
        try:
            print("\n>> Nhập ngày cần tra cứu:")
            d = int(input("   Ngày : "))
            m = int(input("   Tháng: "))
            y = int(input("   Năm  : "))
            if not kiem_tra_hop_le(d, m, y):
                print(f"❌ LỖI: Ngày {d}/{m}/{y} không tồn tại!")
            else:
                d_qua, m_qua, y_qua = tim_hom_qua(d, m, y)
                d_mai, m_mai, y_mai = tim_ngay_mai(d, m, y)
                print("\n" + "=" * 35)
                print(f"{'HÔM QUA':<12} | {'HÔM NAY':<12} | {'NGÀY MAI':<12}")
                print("-" * 35)

                s_qua = f"{d_qua}/{m_qua}/{y_qua}"
                s_nay = f"{d}/{m}/{y}"
                s_mai = f"{d_mai}/{m_mai}/{y_mai}"

                print(f"{s_qua:<12} | {s_nay:<12} | {s_mai:<12}")
                print("=" * 35)

        except ValueError:
            print("❌ Vui lòng chỉ nhập số!")

        opt = input("\nBạn có muốn nhập tiếp không? (y/n): ")
        if opt.lower() == 'n':
            break


if __name__ == "__main__":
    main()