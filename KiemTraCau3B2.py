n=list(map(int,input("Nhập các phần từ:").split()))
tong=0
for i in range(len(n)):
    if n[i]%2==0 or n[i]%3==0:tong+=n[i]
print(tong)