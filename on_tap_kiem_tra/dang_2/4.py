import math

def is_perfect_square(x):
    """Kiểm tra xem x có phải là số chính phương không"""
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    """Kiểm tra xem n có phải là số Fibonacci không"""
    if n <= 0:
        return False
    # Kiểm tra điều kiện Fibonacci
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
if is_fibonacci(n):
    print(f"{n} là số Fibonacci.")
else:
    print(f"{n} không phải là số Fibonacci.")
