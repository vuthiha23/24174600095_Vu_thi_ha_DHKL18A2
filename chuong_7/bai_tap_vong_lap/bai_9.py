import math
n = int(input("Nhap vao so nguyen duong n: "))
so_chinh_phuong = []
i = 1
while i * i < n:
    so_chinh_phuong.append(i * i)
    i += 1
if n <= 0:
    print("Vui long nhap mot so nguyen duong lon hon khong.")
else:
    ket_qua = so_chinh_phuong
print(f"Cac so chinh phuong nho hon {n} la: {ket_qua}")