a = int(input("nhap vao so nguyen duong a: "))
b = int(input("nhap vao so nguyen duong b: "))
so_nho_nhat = a
if b<=a:
    so_nho_nhat = b
k = so_nho_nhat     
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat ")
        break
    k = k -1