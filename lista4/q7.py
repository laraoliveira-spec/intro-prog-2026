conta = int(input("Valor da conta: "))
pago = int(input("Valor do pagamento: "))
troco = pago - conta
print(f"Troco: R$ {troco:.2f}")
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    num_notas = troco // nota
    if num_notas != 0:
        print(f" - {num_notas} de {nota:.2f}")
    troco = troco % nota