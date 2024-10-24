import math
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
if h>0 and r>0:
    pi = 3.14
    Sxq = 2 * pi * r * h
    Stp = Sxq + 2 * pi * r**2
    V = pi * r**2 * h
    print(f"dien tich toan phan cua khoi tru :{Stp:.2f}")
    print(f"dien tich xung quanh cua khoi tru: {Sxq:.2f}")
    print(f"the tich cua khoi tru : {V:.2f}")
else:
    print("gia tri nhap khong thoa man")
    
    
print("ket thuc chuong trinh")        
