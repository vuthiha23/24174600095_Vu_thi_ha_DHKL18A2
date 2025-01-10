# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n (n ≥ 4): "))

# Kiểm tra điều kiện n phải lớn hơn hoặc bằng 4
if n < 4:
    print("n phải lớn hơn hoặc bằng 4 để tính toán.")
else:
    # Khởi tạo tổng S
    S = 0

    # Vòng lặp ngoài: từ i = 4 đến n
    for i in range(4, n + 1):
        # Khởi tạo tổng bên trong
        inner_sum = 0
        # Vòng lặp trong: từ j = 1 đến i
        for j in range(1, i + 1):
            inner_sum += (i/j + 1)  # Tính tổng (j + 1)
        
        # Cộng tổng bên trong vào S
        S += inner_sum
        break
    P = S/n+5

    # Hiển thị kết quả
    print(f"Tổng P là: {P}")
