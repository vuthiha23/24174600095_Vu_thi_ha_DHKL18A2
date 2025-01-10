import csv
def doc_file_csv(ds_cau_thu : list):
    with open (file ="on_tap_kiem_tra\dang_3\files\ds_cau_thu.csv",mode = "r") as open_file:
        csv_reader=csv.reader(open_file)
        for i in csv_reader:
            print(i)
            ds_cau_thu.append(i)

def nhap_thong_tin(ds_cau_thu:list):
    while True:
        try:
            ma_cau_thu = input("nhap ma cau thu:")
            ten_cau_thu = input("nhap ten cau thu:")
            ten_doi_bong = input("nhap ten doi bong:")
            tuoi = int(input("nhap tuoi cua cau thu:"))
            assert tuoi > 0 , "nhap sai "
            vi_tri = input("nhap vi tri cua cau thu")
            assert vi_tri == "thu mon" or vi_tri == "hau ve" or vi_tri == "tien dao" or vi_tri == "tien ve" ,"nhap sai yeu cau nhap lai"
            so_ban_thang = int(input("nhap so ban thang :"))
            assert so_ban_thang > 0 , "nhap sai roi"
        except:
            print("yeu cau nhap lai")
        else:
            if so_ban_thang > 10 :
                thuong = so_ban_thang * 500000
            elif so_ban_thang >= 5:
                thuong= so_ban_thang *300000
            elif so_ban_thang >= 1:
                thuong = so_ban_thang * 200000
            else:
                thuong = 0.0
            if so_ban_thang > 10 :
                tro_cap = 0.1
            elif so_ban_thang >= 5:
                tro_cap = 0.2
            elif so_ban_thang >= 1:
                tro_cap = 0.3
            else:
                tro_cap = 0.0
            if vi_tri == "thu mon":
                luong_theo_vi_tri = 500000
            elif vi_tri == "hau ve":
                luong_theo_vi_tri = 700000
            elif vi_tri == "tien ve":
                luong_theo_vi_tri = 900000
            elif vi_tri == "tien dao":
                luong_theo_vi_tri = 1000000
                
                
            luong = luong_theo_vi_tri+luong_theo_vi_tri*tro_cap+thuong
            ds_cau_thu.append([ma_cau_thu,ten_cau_thu,ten_doi_bong,tuoi,vi_tri,so_ban_thang,thuong,tro_cap,luong])
            break
                        
def sua_thong_tin(ds_cau_thu:list):
    pass

def luu_file(ds_cau_thu:list):
    with open (file ="on_tap_kiem_tra\dang_3\files\ds_cau_thu.csv",mode = "w") as open_file:
        csv_writer=csv.writer(open_file)
        for i in ds_cau_thu:
            csv_writer.writerow(i)


        
        