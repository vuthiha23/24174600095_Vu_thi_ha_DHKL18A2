n = int(input("Nhap mot so de kiem tra: "))
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
if tong_uoc == n:
    print(f"{n} la so hoan hao.")
else:
    print(f"{n} khong phai la so hoan hao.")