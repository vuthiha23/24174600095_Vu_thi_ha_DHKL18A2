import math
tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))
ucln = math.gcd(tu, mau)
tu = tu // ucln
mau = mau // ucln  
if mau < 0:
    tu = -tu
    mau = -mau
print(f"Phan so sau khi toi gian: {tu}/{mau}")
if mau == 0:
    print("mau so khong the bang khong.")