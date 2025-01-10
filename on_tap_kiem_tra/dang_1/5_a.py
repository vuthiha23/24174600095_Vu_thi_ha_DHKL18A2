n = int(input("nhap so nguyen duong :"))
if n > 0:
    S = 0 # khỏiư tạo s = 0
    for i in range(n+1):# vòng lặp từ 0 đến n
        S=S+(i*(i+1))# cộng i *(i+1) vaof tổng s
    print(f"tong s = 1+2+3+...+{n} là : {S}")
else:
    print("vui long nhap so nguyen duong")  