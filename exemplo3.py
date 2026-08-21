# media no padrão 9 a 100
media = int(input("Média do aluno: "))
if media >= 60:
    print("Aluno aprovado!")
elif media >= 30:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado, game over!")