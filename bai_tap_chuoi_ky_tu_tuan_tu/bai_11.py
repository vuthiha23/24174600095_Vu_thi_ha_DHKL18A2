sinh_vien = [
    {"Ten": "Dung", "Diem": 10.0},
    {"Ten": "Quang", "Diem": 5.3},
    {"Ten": "Trang", "Diem": 7.5}
]

print("#Ten    Diem")
for sv in sinh_vien:
    print(f"{sv['Ten']:<8} {sv['Diem']:.1f}")