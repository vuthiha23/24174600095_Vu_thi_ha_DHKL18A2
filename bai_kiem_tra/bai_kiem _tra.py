danh_sach_cau_thu = []

while True:
    print("\nChương trình quản lý đội bóng")
    print("1. Xem danh sách cầu thủ")
    print("2. Nhập thông tin cầu thủ")
    print("3. Tính thưởng cho cầu thủ")
    print("4. Tìm kiếm và xóa cầu thủ")
    print("5. Tìm kiếm và sửa thông tin cầu thủ")
    print("6. Xem danh sách sắp xếp theo số huy chương")
    print("0. Thoát")
    lua_chon = input("Nhập lựa chọn: ")

    try:
        if lua_chon == "1":  # Xem danh sách cầu thủ
            if not danh_sach_cau_thu:
                print("Danh sách trống.")
            else:
                for cau_thu in danh_sach_cau_thu:
                    print(f"Mã: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                          f"Vị trí: {cau_thu['vi_tri']}, Huy chương: {cau_thu['so_huy_chuong']}, "
                          f"Thưởng: {cau_thu['thuong']} VNĐ")

        elif lua_chon == "2":  # Nhập thông tin cầu thủ
            try:
                ma = input("Nhập mã cầu thủ: ")
                ten = input("Nhập tên cầu thủ: ")
                tuoi = int(input("Nhập tuổi cầu thủ: "))
                vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
                so_huy_chuong = int(input("Nhập số huy chương: "))

                # Tính thưởng
                if so_huy_chuong > 10:
                    thuong = so_huy_chuong * 500000
                elif 5 <= so_huy_chuong < 10:
                    thuong = so_huy_chuong * 300000
                elif 1 <= so_huy_chuong < 5:
                    thuong = so_huy_chuong * 200000
                else:
                    thuong = 0

                # Thêm vào danh sách
                cau_thu = {
                    "ma": ma,
                    "ten": ten,
                    "tuoi": tuoi,
                    "vi_tri": vi_tri,
                    "so_huy_chuong": so_huy_chuong,
                    "thuong": thuong
                }
                danh_sach_cau_thu.append(cau_thu)
            except ValueError:
                print("Lỗi: Tuổi và số huy chương phải là số nguyên.")

        elif lua_chon == "3":  # Tính thưởng
            print("Thưởng đã được tính tự động khi nhập cầu thủ.")

        elif lua_chon == "4":  # Tìm kiếm và xóa cầu thủ
            ma = input("Nhập mã cầu thủ cần xóa: ")
            for cau_thu in danh_sach_cau_thu:
                if cau_thu["ma"] == ma:
                    danh_sach_cau_thu.remove(cau_thu)
                    print("Đã xóa cầu thủ.")
                    break
            else:
                print("Không tìm thấy cầu thủ.")

        elif lua_chon == "5":  # Tìm kiếm và sửa thông tin cầu thủ
            ma = input("Nhập mã cầu thủ cần sửa: ")
            for cau_thu in danh_sach_cau_thu:
                if cau_thu["ma"] == ma:
                    try:
                        cau_thu["ten"] = input("Nhập tên mới: ")
                        cau_thu["tuoi"] = int(input("Nhập tuổi mới: "))
                        cau_thu["vi_tri"] = input("Nhập vị trí mới: ")
                        cau_thu["so_huy_chuong"] = int(input("Nhập số huy chương mới: "))

                        # Cập nhật thưởng
                        if cau_thu["so_huy_chuong"] > 10:
                            cau_thu["thuong"] = cau_thu["so_huy_chuong"] * 500000
                        elif 5 <= cau_thu["so_huy_chuong"] < 10:
                            cau_thu["thuong"] = cau_thu["so_huy_chuong"] * 300000
                        elif 1 <= cau_thu["so_huy_chuong"] < 5:
                            cau_thu["thuong"] = cau_thu["so_huy_chuong"] * 200000
                        else:
                            cau_thu["thuong"] = 0

                        print("Đã cập nhật thông tin cầu thủ.")
                    except ValueError:
                        print("Lỗi: Tuổi và số huy chương phải là số nguyên.")
                    break
            else:
                print("Không tìm thấy cầu thủ.")

        elif lua_chon == "6":  # Sắp xếp danh sách cầu thủ theo số huy chương
            try:
                danh_sach_cau_thu.sort(key=lambda x: x["so_huy_chuong"])
                print("Danh sách đã được sắp xếp theo số huy chương.")
            except Exception as e:
                print("Lỗi khi sắp xếp:", e)

        elif lua_chon == "0":  # Thoát chương trình
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)
