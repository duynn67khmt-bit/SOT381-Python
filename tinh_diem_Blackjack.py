import secrets

def random_card():
    for i in range(13):
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return secrets.choice(cards)

def tinh_diem_bai(bai):
    gia_tri = 0
    so_ace = 0

    for the in bai:
        if the in ['J', 'Q', 'K']:
            gia_tri += 10
        elif the == 'A':
            so_ace += 1
            gia_tri += 11
        else:
            gia_tri += int(the)

    while gia_tri > 21 and so_ace:
        gia_tri -= 10
        so_ace -= 1

    return gia_tri


def random_hand():
    return [random_card(), random_card()]

def hien_thi_tay(bai, nguoi_choi=True):
    if nguoi_choi:
        return "Người chơi: " + ", ".join(bai) + f" (Điểm: {tinh_diem_bai(bai)})"
    else:
        return "Nhà cái: " + ", ".join(bai) + f" (Điểm: {tinh_diem_bai(bai)})"

def kiem_tra_thang_thua(nguoi_choi, nha_cai):
    diem_nguoi_choi = tinh_diem_bai(nguoi_choi)
    diem_nha_cai = tinh_diem_bai(nha_cai)

    if diem_nguoi_choi > 21:
        return "Người chơi thua! Quá 21 điểm."
    elif diem_nha_cai > 21:
        return "Nhà cái thua! Quá 21 điểm."
    elif diem_nguoi_choi > diem_nha_cai:
        return "Người chơi thắng!"
    elif diem_nguoi_choi < diem_nha_cai:
        return "Nhà cái thắng!"
    else:
        return "Hòa!"
# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    print("---BLACKJACK---")

    nguoi_choi = random_hand()
    nha_cai = random_hand()

    print(hien_thi_tay(nguoi_choi, True))
    print(hien_thi_tay([nha_cai[0]], False) + ", ???")

    while True:
        action = input("Bạn muốn (H)it thêm lá bài hay (S)tand? ").strip().upper()
        if action == 'H':
            nguoi_choi.append(random_card())
            print(hien_thi_tay(nguoi_choi, True))
            if tinh_diem_bai(nguoi_choi) > 21:
                print("Người chơi thua! Quá 21 điểm.")
                return
        elif action == 'S':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn H hoặc S.")

    while tinh_diem_bai(nha_cai) < 17:
        nha_cai.append(random_card())

    print(hien_thi_tay(nha_cai, False))

    ket_qua = kiem_tra_thang_thua(nguoi_choi, nha_cai)
    print(ket_qua)
if __name__ == "__main__":
    main()