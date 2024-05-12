
DB : dict # global database
FIELD : str # global field 


def merge(keys_m0 : list, keys_m1 : list):
    global DB
    global FIELD

    # check for empti
    if len(keys_m0) == 0:
        return keys_m1
    elif len(keys_m1) == 0:
        return keys_m0
    
    outkeys = []

    # merge arrays
    careage_keys_m0 = 0
    careage_keys_m1 = 0
    while (careage_keys_m0 < len(keys_m0)) and \
          (careage_keys_m1 < len(keys_m1)):

        if DB.get(keys_m0[careage_keys_m0]).get(FIELD) > \
           DB.get(keys_m1[careage_keys_m1]).get(FIELD):

            outkeys.append(keys_m0[careage_keys_m0])
            careage_keys_m0 += 1

        elif DB.get(keys_m0[careage_keys_m0]).get(FIELD) < \
             DB.get(keys_m1[careage_keys_m1]).get(FIELD):

            outkeys.append(keys_m1[careage_keys_m1])
            careage_keys_m1 += 1

        else:
            outkeys.append(keys_m0[careage_keys_m0])
            outkeys.append(keys_m1[careage_keys_m1])

            careage_keys_m0 += 1
            careage_keys_m1 += 1

    # additional merge
    if careage_keys_m0 < len(keys_m0):
        for it in range(careage_keys_m0, len(keys_m0)):
            outkeys.append(keys_m0[it])
    else:
        for it in range(careage_keys_m1, len(keys_m1)):
            outkeys.append(keys_m1[it])

    return outkeys   


def mergening(keys01 : list, keys11 : list):
    global DB

    if len(keys01) <= 1 and len(keys11) <= 1:
        return merge(keys01, keys11)

    keys01_mid = len(keys01) // 2 
    keys01_end = len(keys01)

    keys11_mid = len(keys11) // 2
    keys11_end = len(keys11)

    return merge(mergening(keys01[0:keys01_mid], \
                           keys01[keys01_mid:keys01_end]), \
                 mergening(keys11[0:keys11_mid], \
                           keys11[keys11_mid:keys11_end]), \
                )
    

def mergesort(database : dict, field : str):
    global DB
    global FIELD

    DB = database.copy()
    FIELD = field

    keys = []
    for key in database.keys():
        keys.append(key)

    keys_mid = len(keys) // 2
    keys_end = len(keys)
    
    return mergening(keys[0:keys_mid], keys[keys_mid:keys_end])
