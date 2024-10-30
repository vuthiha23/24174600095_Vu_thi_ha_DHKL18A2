
print("Chào mừng đến với rạp chiếu phim ABC!")
print("Vui lòng chọn thể loại phim bạn muốn xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
lua_chon_cua_ban  = input("Nhập số tương ứng với thể loại phim bạn chọn (1-4): ")
if lua_chon_cua_ban == "1":
    print("Bạn đã chọn thể loại: Phim tình cảm.")
elif lua_chon_cua_ban == "2":
    print("Bạn đã chọn thể loại: Phim kinh dị.")
elif lua_chon_cua_ban == "3":
    print("Bạn đã chọn thể loại: Phim hoạt hình.")
elif lua_chon_cua_ban == "4":
    print("Bạn đã chọn thể loại: Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
