# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Khởi tạo biến P với giá trị ban đầu là 1 (vì tích khởi đầu là 1)
P = 1

# Sử dụng vòng lặp for để tính tích
for i in range(1, n + 1):
    P *= (i + 1)  # Nhân P với (i + 1) tại mỗi bước lặp

# Hiển thị kết quả
print(f"Giá trị của P là: {P}")
