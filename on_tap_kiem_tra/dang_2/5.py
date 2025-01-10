def phan_tich_thua_so_nguyen_to(n):
    i = 2
    thua_so = []
    while i * i <= n:
        while n % i == 0:
            thua_so.append(i)
            n //= i
        i += 1
    if n > 1:
        thua_so.append(n)
    return thua_so

# Nhập vào một số nguyên dương
n = int(input("Nhập vào một số nguyên dương: "))
thua_so_nguyen_to = phan_tich_thua_so_nguyen_to(n)

# In ra kết quả
print(f"Số {n} phân tích thành thừa số nguyên tố: {' * '.join(map(str, thua_so_nguyen_to))}")
