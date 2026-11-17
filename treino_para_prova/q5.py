nota1 = float(input("Informe sua nota 1: "))
nota2 = float(input("Informe sua nota 2: "))

media = (nota1 + nota2) / 2

if media >= 60:
    print("Parabéns, você foi aprovado!")
elif media < 60 and media >= 20:
    print("Você ficou em recuperação! Estude para prova final.")
else:
    print("Reprovado direto.")