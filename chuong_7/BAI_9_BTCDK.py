km_di_chuyen = float(input("nhap so km di chuyen: "))
loai_xe = int(input("nhap loai xe (4 hoac 7): "))
thoi_gian_cho = int(input("nhap thoi gian cho (phut): "))
gia_mo_cua = 0
pham_vi_gia_cao = 0
gia_trong_pham_vi = 0
gia_sau_pham_vi = 0
if loai_xe == 4:
    gia_mo_cua = 11000
    pham_vi_gia_cao = 20
    gia_trong_pham_vi = 12100
    gia_sau_pham_vi = 10000
elif loai_xe == 7:
    gia_mo_cua = 13000
    pham_vi_gia_cao = 30
    gia_trong_pham_vi = 14100
    gia_sau_pham_vi = 12000
else:
    print("loai xe khong hop le ")    
if km_di_chuyen <= 0.8:
    tien_di_chuyen = gia_mo_cua
elif km_di_chuyen <= pham_vi_gia_cao:
    tien_di_chuyen = gia_mo_cua + (km_di_chuyen - 0.8) * gia_trong_pham_vi
else:
    tien_di_chuyen = gia_mo_cua + (pham_vi_gia_cao - 0.8) * gia_trong_pham_vi + (km_di_chuyen - pham_vi_gia_cao) * gia_sau_pham_vi
if thoi_gian_cho <=5:
    tien_cho = 0
else:
    tien_cho = (thoi_gian_cho - 5) * 800
tong_tien = tien_di_chuyen + tien_cho
print(f"tong tien phai tra la : {tong_tien} dong ")
        
