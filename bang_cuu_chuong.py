n = int(input("Bạn muốn in bảng cửu chương mấy? "))
print(f"--- Bảng cửu chương {n} ---")

for i in range(1, 11):
    ket_qua = n * i
    # In ra màn hình theo định dạng: n x i = kết quả
    print(f"{n} x {i} = {ket_qua}")