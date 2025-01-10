# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tính tích của (n + 1) từ i = 1 đến n
tich_n_plus_1 = 1
for i in range(1, n + 1):
    tich_n_plus_1 *= (n + 1)

# Tính tích của (n - 1) từ i = 1 đến n
tich_n_minus_1 = 1
for i in range(1, n + 1):
    tich_n_minus_1 *= (n - 1)

# Tính P
P = tich_n_plus_1 * tich_n_minus_1

# Hiển thị kết quả
print(f"Giá trị của P là: {P}")
