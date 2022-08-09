#Rafael Fernandes Galo
"""O objetivo deste programa é ler um arquivo de texto contendo dois conjuntos
 e identificando qual operação realizar sobre eles, sendo elas as seguintes:
 União, Diferença, Interseção e Produto Cartesiano."""

lista = open("arquivo.txt","r")
operations = int(lista.readline())

def união(list12,list22):
    tam2 = len(list22)
    for i in range(tam2):
        list12.append(list22[i])
    for o in list12:
        if o not in list32:
            list32.append(o)
    return list32

def interseção(list12,list22):
    tam1 = len(list12)
    tam2 = len(list22)
    for o in range(tam2):
        for i in range(tam1):
            if list12[i] == list22[o]:
                list32.append(list22[o])
    return list32

def diferença(list12,list22):
    tam1 = len(list12)
    tam2 = len(list22)
    for i in range(tam1):
        count = 0
        for o in range(tam2):
            if list12[i] != list22[o]:
                count = count + 1
            if count == tam2:
                list32.append(list12[i])
    return list32

def cartesiano(list12,list22):
    tam1 = len(list12)
    tam2 = len(list22)
    c = 0
    for i in range(tam1):
        for o in range(tam2):
            list32.append([])
            list32[c].append(list12[i])
            list32[c].append(list22[o])
            c = c + 1
    return list32

for i in range(operations):
    type = (lista.readline())
    tipo = type.rstrip("\n")
    a = (lista.readline())
    b = (lista.readline())
    list1 = a.rstrip("\n")
    list11 = list1.replace(", ","*")
    list12 = list11.split('*')
    list2 = b.rstrip("\n")
    list21 = list2.replace(", ","*")
    list22 = list21.split('*')
    list32 = []
    save1 = []
    save2 = []

    for i in list12:
        save1.append(i)

    for i in list22:
        save2.append(i)

    list12r = []
    for h in list12:
        if h not in list12r:
            list12r.append(h)
    list12 = list12r

    list22r = []
    for g in list22:
        if g not in list22r:
            list22r.append(g)
    list22 = list22r

    if tipo == "U":
        união(list12, list22)
        print("União: conjunto 1", save1,", conjunto 2", save2,". Resultado:",list32)

    elif tipo == "I":
        interseção(list12, list22)
        print("Interseção: conjunto 1", save1,", conjunto 2", save2,". Resultado:",list32)

    elif tipo == "D":
        diferença(list12, list22)
        print("Diferença: conjunto 1", save1, ", conjunto 2", save2, ". Resultado:", list32)

    else:
        cartesiano(list12, list22)
        print("Produto Cartesiano: conjunto 1", save1,", conjunto 2", save2,". Resultado:",list32)

lista.close()
