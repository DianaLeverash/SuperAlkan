def LoadFiles():
    slovar = {}
    file = open("Изомеры алканов.txt", mode="r", encoding="UTF-8")
    file2 = open("Алканы.txt", mode="r", encoding="UTF-8")
    alkanes = file2.readlines()
    izomers = file.readlines()
    file.close()
    file2.close()
    dop = []
    key = ""
    for alkan in alkanes:
        if alkan == "\n":
            slovar[key.lower()] = [dop]
            dop = []
            key = ""
        else:
            if key == "":
                key = alkan.split(" ")[0]
            dop.append(alkan)
    slovar[key.lower()] = [dop]
    dop2 = []
    key2 = ""
    for izomer in izomers:
        if izomer == "\n":
            slovar[key2.lower()].append(dop2)
            dop2 = []
            key2 = ""
        else:
            if key2 == "":
                key2 = (izomer.split(" ")[2][:-3]).lower()
            dop2.append(izomer)
    slovar[key2.lower()].append(dop2)
    return slovar