from sqlalchemy.sql.base import elements

a = input("Nhập vào mật khẩu: ")
while True:
    if a == "y" or a == "Y" or "con mẹ lý tày từ cha":
        print("Login success")
        break
    else:
        print("Login failed")
        a = input("nhập lại: ")

