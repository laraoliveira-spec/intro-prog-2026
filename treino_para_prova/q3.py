horas = float(input("Quantas horas você passa vendo Netflix? "))

if horas < 1:
    print("Espectador Casual")
elif horas <= 3:
    print("Maratonista Iniciante")
elif horas <= 5:
    print("Maratonista Profissional")
else:
    print("Alerta Vermelho! Desligue a tela e vá ver o sol!")