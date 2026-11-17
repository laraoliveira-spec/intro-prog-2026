saldo_inicial = float(input("Informe o saldo inicial: "))
n = int(input("Transações: "))

suspeitas = 0
retiradas = 0

for i in range(1, n + 1):
    valor = float(input("Valor da transação: "))
    saldo_inicial +=valor

    suspeita = False

    if abs(valor) > 5000:
        print("Transação suspeita por valor maior que 5000.")
        print(f"Transação número {i}.")
        suspeitas = True
    if saldo_inicial < 0:
        print("Transação suspeita por saldo negativo.")
        print(f"Transação número {i}.")
        suspeitas = True

    if valor < 0:
        retiradas += 1
    else:
        retiradas = 0

    if retiradas == 3:
        print("Transação suspeita por escesso de retiradas.")
        print(f"Transação número {i}")
        suspeitas = True

    if suspeita:
        suspeitas += 1
    else:
        print("Transação sem intercorrências.")
        suspeitas = False

print(f"Saldo final: {saldo_inicial:.2f}")
print(f"Transações suspeitas: {suspeitas}")