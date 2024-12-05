
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))



A = []
print(f"Nhập vào ma trận kích thước {m}x{n}:")
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    while len(hang) != n:
        print(f"Vui lòng nhập đúng {n} phần tử.")
        hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    A.append(hang)

print("ma tran A la :")
for hang in A:
    print(" ".join(map(str, hang)))
    
 
