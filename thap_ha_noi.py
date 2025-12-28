so_cot = int(input("Nhập vào số cột:"))
so_dia = int(input("Nhập vào số dĩa:"))

def thap_ha_noi(so_dia, cot_bat_dau, cot_dich, cot_tam):
    if so_dia == 1:
        print(f"Chuyển đĩa từ cột {cot_bat_dau} sang cột {cot_dich}")
    else:
        thap_ha_noi(so_dia - 1, cot_bat_dau, cot_tam, cot_dich)
        print(f"Chuyển đĩa từ cột {cot_bat_dau} sang cột {cot_dich}")
        thap_ha_noi(so_dia - 1, cot_tam, cot_dich, cot_bat_dau)
thap_ha_noi(so_dia, 1, 3, 2)
print("Hoàn thành!")