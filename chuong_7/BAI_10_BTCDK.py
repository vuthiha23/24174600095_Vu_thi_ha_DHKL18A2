luong = float(input("nhap luong cua nhan vien (dong): "))
if luong == 15000000:
    thue_thu_nhap = 0.3
elif 7000000 <= luong < 15000000:
    thue_thu_nhap = 0.2
else:
    thue_thu_nhap = 0.1
tien_thue = luong * thue_thu_nhap
luong_rong = luong - tien_thue
print(f"thue thu nhap phai tra la {tien_thue} dong")
print(f"luong rong nhan duoc la {luong_rong} dong")        