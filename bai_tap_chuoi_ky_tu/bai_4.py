chuoi_ky_tu = input("nhap chuoi ky tu : ")
chu_cai = 0
so = 0
ky_tu_dac_biet = 0
for ky_tu in chuoi_ky_tu:
    if ky_tu.isalpha() == True:
        chu_cai = chu_cai + 1
    else:
        if ky_tu.isdigit() == True:
            so = so + 1
        else:
            ky_tu_dac_biet = ky_tu_dac_biet + 1
print(f"so ky tu chu la {chu_cai}")
print(f"so ky tu so la {so}")
print(f"so ky tu dac biet la {ky_tu_dac_biet}")                
    