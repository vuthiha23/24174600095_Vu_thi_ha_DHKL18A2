# Hàm để nhập ma trận
def nhap_ma_tran(m, n):
    A = []
    print(f"Nhập vào ma trận kích thước {m}x{n}:")
    for i in range(m):
        hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
        while len(hang) != n:
            print(f"Vui lòng nhập đúng {n} phần tử.")
            hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
        A.append(hang)
    return A

# Hàm để in ma trận
def in_ma_tran(A):
    print("Ma trận là:")
    for hang in A:
        print(" ".join(map(str, hang)))

# Hàm để tính tổng hai ma trận
def tinh_tong(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Hàm để tính hiệu hai ma trận
def tinh_hieu(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Hàm để tính tích của ma trận với số k
def tinh_tich_k(A, k):
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]

# Hàm để tính tích hai ma trận
def tinh_tich_AB(A, B):
    if len(A[0]) != len(B):
        return "Không thể tính tích hai ma trận"
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

# Hàm để tính ma trận đối xứng của ma trận A
def tinh_ma_tran_doi_xung(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Nhập ma trận A
print("Nhập ma trận A:")
ma_tran_A = nhap_ma_tran(m, n)

# Nhập ma trận B
print("Nhập ma trận B:")
ma_tran_B = nhap_ma_tran(m, n)

# Tính tổng hai ma trận A, B
tong_AB = tinh_tong(ma_tran_A, ma_tran_B)
print("Tổng hai ma trận A, B là:")
in_ma_tran(tong_AB)

# Tính hiệu hai ma trận A, B
hieu_AB = tinh_hieu(ma_tran_A, ma_tran_B)
print("Hiệu hai ma trận A, B là:")
in_ma_tran(hieu_AB)

# Tính tích của ma trận A với số k
k = int(input("Nhập số k: "))
tich_kA = tinh_tich_k(ma_tran_A, k)
print("Tích của ma trận A với số k là:")
in_ma_tran(tich_kA)

# Tính tích hai ma trận A, B
tich_AB = tinh_tich_AB(ma_tran_A, ma_tran_B)
if isinstance(tich_AB, str):
    print(tich_AB)
else:
    print("Tích hai ma trận A, B là:")
    in_ma_tran(tich_AB)

# Tính ma trận đối xứng của ma trận A
ma_tran_doi_xung_A = tinh_ma_tran_doi_xung(ma_tran_A)
print("Ma trận đối xứng của ma trận A là:")
in_ma_tran(ma_tran_doi_xung_A)