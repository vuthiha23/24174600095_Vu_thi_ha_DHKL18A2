n = int(input("nhap so nguyen duong :"))
if n > 4:
    S = 0 # khỏiư tạo s = 0
    for i in range(4,n+1):# vòng lặp từ 4 đến n
        S=S+((i+1)/(i-1))# cộng i *(i+1) vaof tổng s
    print(f"tong s =  : {S}")
else:
    print("vui long nhap so nguyen duong") 