pontos = []
i = 1
while i <= 3:
    x = float(input(f"x{i}: "))
    y = float(input(f"y{i}: "))
    pontos.append((x, y))
    i = i + 1

print(pontos)

for p in pontos:
    print(p, end=" - ")
    x, y = p
    if x > 0 and y > 0:
        print("1° Quadrante")
    elif x < 0 and y > 0:
        print("2° Quadrante")
    elif x < 0 and y < 0:
        print("3° Quadrante")
    elif x > 0 and y < 0:
        print("4° Quadrante")
    else:
        print("Ponto está em um dos eixos.")