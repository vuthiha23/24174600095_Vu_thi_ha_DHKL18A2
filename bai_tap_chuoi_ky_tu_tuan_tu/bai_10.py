n = int(input("Nhap so luong sinh vien: "))
ds_sv = []
for i in range(n):
    print(f"Nhap thong tin cho sinh vien {i+1}:")
    ten = input("Ten sinh vien: ")
    diem = float(input("Điem tong ket cuoi nam: "))
    ttin_sv = {"Ten": ten, "Điem": diem}
    ds_sv.append(ttin_sv)

print("\nDanh sach sinh vien:")
for sv in ds_sv:
    print(f"Ten: {sv['Ten']}, Điem: {sv['Điem']}")
