nome = input("Informe seu nome de usuário: ")
senha = input("Informe sua senha: ")

while senha == nome:
    print("Não é permitido nome e senha iguais.")
    nome = input("Digite novamente seu nome de usuário: ")
    senha = input("Digite novamente sua senha: ")
print("Nome e senha válidos!")