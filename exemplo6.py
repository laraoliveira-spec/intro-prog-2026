lado1 = int(input("Me diga a medida do lado 1: "))
lado2 = int(input("Me diga a medida do lado 2: "))
lado3 = int(input("Me diga a medida do lado 3: ")) 
if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os lados não formam um triângulo!")