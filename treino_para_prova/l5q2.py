alunos = int(input("Quantidade de alunos: "))
medias = []

aprovados = 0
prova_final = 0
reprovados = 0

for i in range(1, alunos + 1):
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    if media >= 60:
        print("Aprovado.")
        aprovados +=1
    elif media >= 20 and media < 60:
        print("Prova final.")
        prova_final +=1
    else:
        print("Reprovado.")
        reprovados +=1

    medias.append(media)

maior_media = max(medias)
menor_media = min(medias)
media_geral = sum(medias) / alunos
percentual = (aprovados / alunos) * 100

print(f"Maior média: {maior_media}")
print(f"Menor média: {menor_media}")
print(f"Media geral: {media_geral}")
print(f"Aprovados: {aprovados}")
print(f"Prova Final: {prova_final}")
print(f"Reprovados: {reprovados}")
print(f"Percentual de aprovados: {percentual}")