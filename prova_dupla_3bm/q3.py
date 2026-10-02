data1 = input("Digite uma data no formato dd/mm/aa: ")
data2 = input("Digite uma data no formato dd/mm/aa: ")
if (data1[6:] != data2[6:]):
    print("As datas divergem no mês/ano")
else:
    dia1 = int(data1[0:2])
    dia2 = int(data2[0:2])
    diff = dia1 - dia2
    if diff < 0:
        diff *= -1

    print(f"A diferença é de {diff} dias.")