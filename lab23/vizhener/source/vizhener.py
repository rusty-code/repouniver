# Создать программу для де/шифрования
# последовательности символов шифром Виженера


# import vizhener.source.EN_C_oder as enc
import source.EN_C_oder as enc

def is_words(wds : str, lat : str) -> bool:
    for wd in wds:
        if wd not in lat:
            return False
    return True

def make_alpha(lat : str):
    alpha = {} # shift table
    for wd in range(0, len(lat)):
        alpha[lat[wd]] = wd

    return alpha


def vizh(act : str):


    if act == 'x': 
        exit()
    
    lat = "abcdefghijklmnopqrstuvwxyz" # code objects
    alpha = make_alpha(lat) # shift table
    
    key = input("Enter the key (use a-z): ")
    flag = True
    while (flag): # valid for correct shift key
        if len(key) <= len(lat) and is_words(key, lat):
            flag = False
        else: 
            print(f"(ERROR) incorrect key {key}")
            key = input("Enter the key (use a-z): ")

    
    if act == 'c':
        enc.coder(
            key=key, 
            alpha=make_alpha(lat), 
            resource_file='vizhener/files/resource_text.txt',
            tocode_file= 'vizhener/files/code_text.txt',
            )
    elif act == 'e':
        enc.encoder(
            key=key, 
            alpha=make_alpha(lat),
            lat=lat,
            resource_file='vizhener/files/code_text.txt',
            tocode_file='vizhener/files/encode_text.txt')
    else:
        return
        
    
    



