login_padrão = "aluno"
senha_padrao = "ifrn123"

login = input("Login: ")
senha = input("Senha: ")

if login == login_padrão and senha == senha_padrao:
    print("Acesso liberado. Bem-vindo ao SUAP!")
else:
    print("Credenciais inválidas. Acesso bloqueado!")