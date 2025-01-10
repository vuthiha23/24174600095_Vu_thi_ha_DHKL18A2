# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra điều kiện đầu vào
if n <= 1:
    print("Số này không phải là số nguyên tố.")
else:
    # Giả định ban đầu: n là số nguyên tố
    la_so_nguyen_to = True

    # Kiểm tra các số từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # Nếu n chia hết cho i, thì n không phải số nguyên tố
            la_so_nguyen_to = False
            break

    # In kết quả
    if la_so_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
