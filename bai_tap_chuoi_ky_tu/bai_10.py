chuoi_nhap = input("Nhap vao chuoi ky tu: ")
so = ""  
chu = ""  
for ky_tu in chuoi_nhap:
    if ky_tu.isdigit():  
        so = so+ ky_tu
    else:  
        chu = chu +ky_tu
chuoi_moi = so + chu  
print(f"Chuoi moi sau khi don tat ca so sang ben trai la: {chuoi_moi}")