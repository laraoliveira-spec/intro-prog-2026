saldo = int(input("Saldo de moedas: "))
valor_skin = int(input("Valor da skin: "))
if saldo >= valor_skin:
    print("Compra realizada! Aproveite sua nova skin.")
    saldo = saldo - valor_skin
    print(f"Saldo restante {saldo:.2f}")
else:
    print("Saldo insuficiente!")
    restante = valor_skin - saldo
    print(f"Faltam {valor_skin - saldo} moedas para você comprar esse item.")