# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra n phải lớn hơn hoặc bằng 4 (do i bắt đầu từ 4 ở mẫu số)
if n < 4:
    print("n phải lớn hơn hoặc bằng 4 để tính toán.")
else:
    # Tính tử số: tích của (i - 1) từ i = 2 đến n
    tu_so = 1
    for i in range(2, n + 1):
        tu_so *= (i - 1)

    # Tính mẫu số: tích của (1/i) từ i = 4 đến n
    mau_so = 1
    for i in range(4, n + 1):
        mau_so *= (1 / i)

    # Tính giá trị của P
    P = tu_so / mau_so

    # Hiển thị kết quả
    print(f"Giá trị của P là: {P}")
