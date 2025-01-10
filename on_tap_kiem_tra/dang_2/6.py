# Hàm tìm tất cả các ước của một số
def find_divisors(num):
    divisors = []
    for i in range(1, abs(num) + 1):  # Duyệt từ 1 đến |num|
        if num % i == 0:
            divisors.append(i)
    return divisors

# Hàm tìm ước chung của hai số
def common_divisors(a, b):
    divisors_a = find_divisors(a)  # Tìm ước của a
    divisors_b = find_divisors(b)  # Tìm ước của b
    return list(set(divisors_a) & set(divisors_b))  # Lấy giao của hai tập hợp ước

# Nhập hai số nguyên a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm ước chung
common = common_divisors(a, b)

# Hiển thị kết quả
print(f"Các ước chung của {a} và {b} là: {common}")
