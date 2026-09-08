palavra_correta = "sexta"
while True:
    palavra = input("Palavra: ")
    if palavra != palavra_correta:
        print("Errou! Tente novamente.")
    else:
        print("Acertou! Parabéns!")
        break
print("Obrigada por participar!")