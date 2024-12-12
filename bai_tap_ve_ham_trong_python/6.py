def kiem_tra_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        return True
    else:
        return False
print(kiem_tra_so_hoan_hao(6))             
             