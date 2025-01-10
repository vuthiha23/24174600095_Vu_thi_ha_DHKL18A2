# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra nếu n là số nguyên dương
if n > 1:  # n phải lớn hơn 1 vì công thức yêu cầu (n-1)
    # Khởi tạo tổng S
    S = 1  # Số hạng đầu tiên là 1
    for i in range(1, n):  # Tính từ 1 đến (n-1)
        S += 1 / (i * (i + 1))  # Cộng thêm các số hạng theo công thức

    # In kết quả
    print(f"Tổng S = 1 + 1/(1*2) + 1/(2*3) + ... + 1/((n-1)*n) là: {S:.5f}")
else:
    print("Vui lòng nhập số nguyên dương lớn hơn 1!")
