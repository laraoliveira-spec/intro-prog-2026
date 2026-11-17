estoque = 100
maior = 100
menor = 100

n = int(input("Operações realizadas durante o dia: "))

for i in range(1, n + 1):
    movimentacao = int(input("Digite a movimentação: "))

    estoque = estoque + movimentacao

    if estoque > maior:
        maior = estoque

    elif estoque < menor:
        menor = estoque

    elif estoque < 0:
        print(f"Estoque negativo na operação {i}")
        print(f"Estoque no momento do erro: {estoque}")
        break

print(f"Maior estoque registrado: {maior}")
print(f"Menor estoque registrado: {menor}")