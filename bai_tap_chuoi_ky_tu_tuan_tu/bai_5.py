n = int(input("Nhap vao n = "))
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-1-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)
