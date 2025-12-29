toan =  int(input("Nhập điểm môn toán: "))
ly =  int(input("Nhập điểm môn lý: "))
hoa =  int(input("Nhập điểm môn hóa: "))

tongdiem3mon = toan + ly + hoa
if tongdiem3mon >= 15 and toan >= 5 and ly >= 5 and hoa >= 5:
    print("học đều các môn và đậu")
elif tongdiem3mon >= 15 and toan >= 4 and ly >= 4 and hoa >= 4:
    print("đậu")
else:
    print("học chưa đều các môn")