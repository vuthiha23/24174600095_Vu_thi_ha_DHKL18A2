n = int(input("nhap so nguyen duong :"))
if n > 0:
    S = 0
    for i in range(1,n+1):
        S=S+i
    print(f"tong s = 1+2+3+...+{n} là : {S}")
else:
    print("vui long nhap so nguyen duong")    
