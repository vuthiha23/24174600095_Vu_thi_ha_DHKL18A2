import math
n = int(input("Nhập vào một số nguyên dương: "))
can_bac_hai_cua_n = math.isqrt(n) 
if can_bac_hai_cua_n * can_bac_hai_cua_n == n:
    print(f"{n} la so chinh phuong.")
else:
    print(f"{n} khong phai la so chinh phuong.")