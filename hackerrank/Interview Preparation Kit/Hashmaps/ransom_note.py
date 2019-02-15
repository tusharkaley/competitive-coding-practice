def checkMagazine(magazine, note):
    print_yes =True
    magazine_dict = dict()
    for mword in magazine:
        if mword in magazine_dict:
            magazine_dict[mword] = magazine_dict[mword] + 1 
        else:
            magazine_dict[mword] = 1
    for nword in note:
        if nword in magazine_dict:
            magazine_dict[nword]= magazine_dict[nword]-1 
            if magazine_dict[nword] ==0:
                magazine_dict.pop(nword)
        else:
            print("No")
            print_yes =False
            break
    if print_yes:
        print("Yes")