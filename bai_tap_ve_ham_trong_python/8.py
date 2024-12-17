def uoc_cua_mot_so_nguyen(n):
    so = []
    for i in range(1,n+1):
        if n % i == 0:
            so.append(i)
    return so
print(uoc_cua_mot_so_nguyen(10))    