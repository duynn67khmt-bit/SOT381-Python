c = input("Nhập Bất Kỳ:")

if c.isupper():
    print(c,"là chữ hoa.")
elif c.islower():
    print(c,"là chữ thường.")
elif c.isdigit():
    print(c,"là số.")
else:
    print(c,"là kí tự đặc biệt")
