import ramdom

lista_aleatorio = []
for in range(0,101):
    lista_aleatorio.append(i)
numero_aleatorio = random.choice(lista_aleatorio)

escolha = -1

while escolha != numero_aleatorio:
escolha = int(input("Digite um número entre 0 e 100: "))
contador += 1

if escolha == numero_aleatorio:
    print(f"Parabéns!!! Você acertou em {contador} tentativas")
elif escolha > numero_aleatorio:
    print(f"Você errou!!! Seu número é maior que o número a ser adivinhado")
elif escolha < numero_aleatorio:
    print(f"Você errou!!! Seu número é menor que o número a ser adivinhado")

continuar = input("Jogar novamente [S/N]?")

if continuar == "N":
    break