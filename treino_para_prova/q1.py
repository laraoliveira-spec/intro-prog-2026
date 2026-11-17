valor = float(input("Quanto deu a conta? "))
amigos = int(input("Quantas pessoas vieram? "))
taxa = input("Desejam pagar a taxa de serviço? (Sim/Não) ")

if taxa == "Sim":
    adicao = valor + (0.10 * valor)
    valor_unitario = adicao / amigos
    print(f"Cada pessoa vai pagar {valor_unitario:.2f}")
else:
    valor_unitario2 = valor / amigos
    print(f"Cada pessoa vai pagar {valor_unitario2:.2f}")