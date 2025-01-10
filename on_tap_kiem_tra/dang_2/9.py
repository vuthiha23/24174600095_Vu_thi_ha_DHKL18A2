# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Khởi tạo các số Fibonacci
fib1, fib2 = 0, 1
product = 1  # Khởi tạo tích = 1 (vì tích là nhân các số)

# Tính tích các số Fibonacci nhỏ hơn n
while fib1 < n:
    if fib1 != 0:  # Tránh nhân với 0
        product *= fib1
    fib1, fib2 = fib2, fib1 + fib2  # Cập nhật Fibonacci

# In kết quả
print(f"Tích các số Fibonacci nhỏ hơn {n} là: {product}")
