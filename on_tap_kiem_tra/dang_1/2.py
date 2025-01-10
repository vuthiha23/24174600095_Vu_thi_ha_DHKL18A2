n = int(input("nhap s nguyen duong:"))
if n > 0:
    s = 0
    for i in range(1,n+1):
        s += 2*i
    print(f"s = {s}")    
else:
    print("yeu cau nhap so nguyen duong")                