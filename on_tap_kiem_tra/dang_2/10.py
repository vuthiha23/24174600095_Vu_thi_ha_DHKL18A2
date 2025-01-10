# Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Hàm tạo dãy Fibonacci nhỏ hơn hoặc bằng n
def fibonacci_sequence(n):
    fib = [0, 1]  # Khởi tạo dãy Fibonacci
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > n:
            break
        fib.append(next_fib)
    return fib

# Hàm tìm các số vừa là Fibonacci vừa là số nguyên tố
def find_fibonacci_primes(n):
    fib = fibonacci_sequence(n)  # Lấy dãy Fibonacci nhỏ hơn hoặc bằng n
    result = [x for x in fib if is_prime(x)]  # Chỉ lấy các số vừa là Fibonacci vừa là nguyên tố
    return result

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
if n < 1:
    print("n phải là số nguyên dương!")
else:
    # Tìm các số vừa là Fibonacci vừa là số nguyên tố
    fibonacci_primes = find_fibonacci_primes(n)
    print(f"Các số vừa là Fibonacci vừa là số nguyên tố nhỏ hơn hoặc bằng {n}: {fibonacci_primes}")

