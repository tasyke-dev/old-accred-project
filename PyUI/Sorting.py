"""!!!Файл с сортировками записей!!!"""
#Сортировка аудиторий
def SelSortAud(array):
    n=len(array)
    for i in range(0,n-1):
        a=i
        b=i+1
        while b<n:
            if array[b].get("AudienceName")<array[a].get("AudienceName"):
                a=b
            elif array[b].get("AudienceName")==array[a].get("AudienceName"):
                if array[b].get("AudienceNaimenovanie")<array[a].get("AudienceNaimenovanie"):
                    a=b
                elif array[b].get("AudienceNaimenovanie")==array[a].get("AudienceNaimenovanie"):
                    if array[b].get("AudienceTO")<array[a].get("AudienceTO"):
                        a=b
                    elif array[b].get("AudienceTO")==array[a].get("AudienceTO"):
                        if array[b].get("AudiencePO")<array[a].get("AudiencePO"):
                            a=b
                    
            b+=1
        array[i],array[a]=array[a],array[i]
    return array

#Сортировка КО
def SelSortPPS(array):
    n=len(array)
    for i in range(0,n-1):
        a=i
        b=i+1
        while b<n:
            if array[b].get("FIO")<array[a].get("FIO"):
                a=b
            elif array[b].get("FIO")==array[a].get("FIO"):
                if array[b].get("Uslovia")<array[a].get("Uslovia"):
                    a=b
                elif array[b].get("Uslovia")==array[a].get("Uslovia"):
                    if array[b].get("Dolzhnost")<array[a].get("Dolzhnost"):
                        a=b
                    elif array[b].get("Dolzhnost")==array[a].get("Dolzhnost"):
                        if array[b].get("Stepen")<array[a].get("Stepen"):
                            a=b
                        elif array[b].get("Stepen")==array[a].get("Stepen"):
                            if array[b].get("Zvanie")<array[a].get("Zvanie"):
                                a=b
                            elif array[b].get("Zvanie")==array[a].get("Zvanie"):
                                if array[b].get("Napravlenie")<array[a].get("Napravlenie"):
                                    a=b
                                elif array[b].get("Napravlenie")==array[a].get("Napravlenie"):
                                    if array[b].get("Education")<array[a].get("Education"):
                                        a=b
            b+=1
        array[i],array[a]=array[a],array[i]
    return array
