nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido! Insira outro valor de 0 a 10: ")
    nota = float(input("Digite a nova nota: "))

print("Nota válida!")