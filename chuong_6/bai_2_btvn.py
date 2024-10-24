import math
x = float(input("nhap gia tri cua x : "))
if x <= 45 :  
    f_x = (-x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
    print(f"gia tri cua f(x) la = {f_x:.2f}")
else:
    print("gia tri cua x khong thoa man")
    
    
print("ket thuc chuong trinh")        
        