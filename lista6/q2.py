# Estrutura: tupla
x = float(input("x: "))
y = float(input("y: "))
pos_ini = (x, y)

# Desempacotar
x, y = pos_ini

if x > 0 and y > 0:
    print("1º Quadrante")
elif x < 0 and y > 0:
    print("2º Quadrante")
elif x < 0 and y < 0:
    print("3º Quadrante")
elif x > 0 and y < 0:
    print("4º Quadrante")
else:
    print("Origem")