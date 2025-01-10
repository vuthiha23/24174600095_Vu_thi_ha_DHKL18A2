import math

def cac_so_chinh_phuong(n):
    """Tìm các số chính phương nhỏ hơn hoặc bằng n"""
    return [i * i for i in range(1, int(math.sqrt(n)) + 1)]

def la_so_nguyen_to(x):
    """Kiểm tra một số có phải số nguyên tố không"""
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def cac_so_nguyen_to(n):
    """Tìm các số nguyên tố nhỏ hơn hoặc bằng n"""
    return [i for i in range(2, n + 1) if la_so_nguyen_to(i)]

def cac_so_hoan_hao(n):
    """Tìm các số hoàn hảo nhỏ hơn hoặc bằng n"""
    def tong_uoc_so(x):
        # Tính tổng các ước số thực sự của x (không bao gồm x)
        return sum(i for i in range(1, x // 2 + 1) if x % i == 0)
    
    return [i for i in range(1, n + 1) if tong_uoc_so(i) == i]

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    so_chinh_phuong = cac_so_chinh_phuong(n)
    so_nguyen_to = cac_so_nguyen_to(n)
    so_hoan_hao = cac_so_hoan_hao(n)

    print(f"Các số chính phương nhỏ hơn hoặc bằng {n}: {so_chinh_phuong}")
    print(f"Các số nguyên tố nhỏ hơn hoặc bằng {n}: {so_nguyen_to}")
    print(f"Các số hoàn hảo nhỏ hơn hoặc bằng {n}: {so_hoan_hao}")
else:
    print("Vui lòng nhập một số nguyên dương.")
