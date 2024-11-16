chuoi_ky_tu = input("nhap chuoi ky tu : ")
chu_hoa = 0
chu_thuong = 0
for ky_tu in chuoi_ky_tu:
    if ky_tu.isupper():
        chu_hoa = chu_hoa + 1
    elif ky_tu.islower():
        chu_thuong = chu_thuong + 1
print(f"so ky t viet hoa la {chu_hoa}")
print(f"so ky tu viet thuong la {chu_thuong}")            