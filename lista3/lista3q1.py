valor = float(input("Valor da conta: "))
pessoas = int(input("Quantidade de pessoas: "))
taxa = input("Adiciona 10%? (SIM ou NÃO): ")

if taxa == "SIM":
    valor = valor + valor*0.1
elif taxa == "NÃO":
    print("Sem taxa de 10%")
else:
    print("Opção inválida! Desconsiderar taxa")

valor_por_pessoa = valor / pessoas

print("Resumo da Conta:")
print(f"Valor da conta = R$ {valor:.2f}")
print(f"Valor por pessoa = R$ {valor_por_pessoa:.2f}")