a = int(input("nhap vao so nguyen duong a: "))
b = int(input("nhap vao so nguyen duong b: "))
so_nho_nhat = a
if b<=a:
    so_nho_nhat = b
k = so_nho_nhat     
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        break
    k = k -1
bcnn = abs(a*b)/k
if a == 0 or b == 0:
    print("khong co bcnn vi mot trong hai so bang 0" )
else:
    print(f"boi chung nho nhat cua {a} va {b} la:{bcnn}")