chuoi_nhi_phan = input("Nhập vào chuỗi nhị phân (chỉ gồm 0 và 1): ")

# Kiểm tra xem chuỗi có phải số nhị phân không (chỉ chứa '0' và '1')
so_nhi_phan = True
for ky_tu in chuoi_nhi_phan:
    if ky_tu != '0' and ky_tu != '1':  # Kiểm tra ký tự có phải '0' hoặc '1' không
        so_nhi_phan = False
        break  # Nếu có ký tự khác ngoài '0' và '1', thoát vòng lặp

# Nếu chuỗi hợp lệ, chuyển đổi sang số thập phân
if so_nhi_phan:
    so_thap_phan = 0
    do_dai = len(chuoi_nhi_phan)
    
    # Chuyển đổi từng bit trong chuỗi nhị phân sang số thập phân
    for i in range(do_dai):
        bit = int(chuoi_nhi_phan[i])  # Chuyển ký tự thành số nguyên
        so_thap_phan += bit * (2 ** (do_dai - i - 1))  # Tính giá trị thập phân của từng bit
    
    print(f"Số thập phân tương ứng là: {so_thap_phan}")
else:
    print("Chuỗi không phải là số nhị phân hợp lệ.")
