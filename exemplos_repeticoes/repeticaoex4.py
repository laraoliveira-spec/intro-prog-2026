login_padrão = "aluno"
senha_padrao = "ifrn123"

login = ""
senha = ""

while login != login_padrão or senha != senha_padrao:
    login = input("Login: ")
    senha = input("Senha: ")
    if login != login_padrão or senha != senha_padrao:
        print("Acesso inválido, tente novamente!")
    else:
        print("Acesso liberado!")