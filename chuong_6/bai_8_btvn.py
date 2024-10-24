import math
x = float(input("nhap gia tri cua x : "))
if x > 0 :
    f_x = math.log(x, 4) + math.log(2, x)
    print(f"gia tri cua f(x) la = {f_x:.2f}")
else:
    print("gia tri cua x khong thoa man")
    
print("ket thuc chuong trinh")        