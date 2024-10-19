import math

# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

# Pi
pi = 3.14

# Tính diện tích xung quanh (Sxq = 2 * pi * r * h)
Sxq = 2 * pi * r * h

# Tính diện tích toàn phần (Stp = Sxq + 2 * pi * r^2)
Stp = Sxq + 2 * pi * r**2

# Tính thể tích (V = pi * r^2 * h)
V = pi * r**2 * h

# Hiển thị kết quả với làm tròn đến 2 chữ số thập phân
print(f"Diện tích xung quanh của khối trụ: {round(Sxq, 2)}")
print(f"Diện tích toàn phần của khối trụ: {round(Stp, 2)}")
print(f"Thể tích của khối trụ: {round(V, 2)}")
