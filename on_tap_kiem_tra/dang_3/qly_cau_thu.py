
print("menu")
print("1.doc file csv")
print("2.nhap thong tin")
print("3.sua thong tin ")
print("4. luu file vao csv")
print("5.thoat chuong trinh")
ds_cau_thu = []
while True:
    try:
        lua_chon = input("nhap lua chon cua ban:")
        lua_chon = int(lua_chon)
    except:
        if lua_chon == 1:
            print("thuc hien doc file")    
        elif lua_chon == 2:
            print("thuc hien nhap thong tin ")    
        elif lua_chon == 3:
            print("thuc hien sua thong tin") 
        elif lua_chon == 4:
            print("thuc hien luu file")
        else:
            print("thoat chuong trinh")
            break
                   