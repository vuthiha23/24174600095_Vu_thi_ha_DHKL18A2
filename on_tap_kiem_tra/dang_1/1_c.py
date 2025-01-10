# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra nếu n là số nguyên dương
if n > 1:
    # Tính tổng bằng vòng lặp
    S = 1
    for i in range(2, n + 1):
        if i % 2 == 0:  # Số chẵn, trừ
            S += 1 / i
        else:           # Số lẻ, cộng
            S -= 1 / i
    
    # In kết quả
    print(f"Tổng S = 1 + 1/2 - 1/3 + 1/4 - ... ± 1/n là: {S:.5f}")
else:
    print("Vui lòng nhập số nguyên dương!")
