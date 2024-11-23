chuoi_ky_tu = input("nhap vao ky tu:")
if chuoi_ky_tu.startswith('-') and chuoi_ky_tu[1:].isdigit(): #starswith lệnh kiểm tra số gì "-"(la số âm)   isdigit kiểm tra xem là số hay k
    print(" chuoi la so am")
else:
    print(" chuoi khong phai so am")
    