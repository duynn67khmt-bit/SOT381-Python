a = input("Nhập vào mật khẩu: ")
while True:
    if a == "y" or a == "Y":
        print("Login success")
        break
    else:
        print("Login failed")
        a = input("nhập lại: ")

