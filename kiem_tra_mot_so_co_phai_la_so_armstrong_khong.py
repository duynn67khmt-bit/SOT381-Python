a = int(input("nhập vào số nguyên dương bất kỳ: "))
t = 0
t = str(a)
l = len(t)
s = 0
for i in range(l):
    s = s + int(t[i]) ** l
if s == a:
    print(a, "là số Armstrong")
else:
    print(a, "không phải là số Armstrong")
