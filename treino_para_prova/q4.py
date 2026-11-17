mensagem = input("Escreva sua mensagem: ")

if len(mensagem) < 3 or len(mensagem) > 140:
    print("Mensagem bloquada por diretrizes de span!")
else:
    print("Mensagem enviada com sucesso!")