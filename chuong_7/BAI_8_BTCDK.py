# Nhập điểm từ bàn phím
Diem = input("Nhập điểm của sinh viên (A, B, C, D, E, F): ")

# Phân loại sinh viên dựa vào điểm
if Diem == "A":
    print("Sinh viên loại Xuất sắc.")
elif Diem == "B":
    print("Sinh viên loại Giỏi.")
elif Diem == "C":
    print("Sinh viên loại Khá.")
elif Diem == "D":
    print("Sinh viên loại Trung bình.")
elif Diem == "E":
    print("Sinh viên loại Yếu.")
elif Diem == "F":
    print("Sinh viên loại Kém.")
else:
    print("Điểm nhập không hợp lệ. Vui lòng nhập A, B, C, D, E hoặc F.")
