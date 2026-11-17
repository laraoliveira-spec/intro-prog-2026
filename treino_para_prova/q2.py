saldo = float(input("Qual seu saldo de moedas? "))
skin = float(input("Quanto custa a skin? "))

if saldo >= skin:
    print("Compra realizada! Aproveite sua nova skin.")
    novo_saldo = saldo - skin
    print(f"Seu novo saldo é de R${novo_saldo:.2f}.")
else:
    diferenca = skin - saldo
    print(f"Saldo insuficiente! Faltam {diferenca:.2f} moedas para você comprar este item.")