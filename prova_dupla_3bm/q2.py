dindins = [1, 2, 5, 10, 20, 50, 100]

din_user = int(input("Digite o dinheiro: "))

if din_user < 10 or din_user > 600:
    print("Intervalo inadequado")
else:
    qtd_usos = [0, 0, 0, 0, 0, 0, 0]
for i in range(-1, -8, -1):
    qtd_usos[-1] = din_user // dindins[-1]
    din_user %= dindins[-1]

    print(qtd_usos)

    for i in range(7):
        print(f"Foi usado {qtd_usos[i]} R$ {dindins[i]}")