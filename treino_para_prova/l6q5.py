robotica = set()
informatica = set()

alunos1 = input("Alunos que participam do grupo 1: ")
alunos2 = input("Alunos que participam do grupo 2: ")

robotica.update(alunos1)
informatica.update(alunos2)

print(f"Alunos nos dois clubes: {robotica & informatica}. ")
print(f"Alunos que participam pelo menos de um clube: {robotica | informatica}")


# Estrutura: CONJUNTO
robotica = set()
programacao = set()

n = int(input("Alunos da Robótica: "))
for i in range(n):
    robotica.add(input("Nome: "))

n = int(input("Alunos da Programação: "))
for i in range(n):
    programacao.add(input("Nome: "))

print("Nos dois:", sorted(robotica & programacao))
print("Em pelo menos um:", sorted(robotica | programacao))
print("Só Robótica:", sorted(robotica - programacao))
print("Somente um clube:", sorted(robotica ^ programacao))