def kiem_tra_so_nguyen_duong(s):
    return s.isnumeric() and s[0] != '0'

print(kiem_tra_so_nguyen_duong("123"))  
print(kiem_tra_so_nguyen_duong("0123"))
print(kiem_tra_so_nguyen_duong("abc"))
print(kiem_tra_so_nguyen_duong("12.3"))  