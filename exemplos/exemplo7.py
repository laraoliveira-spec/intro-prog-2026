idade = int(input("Informe sua idade: "))
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")
# if ternário
print("Menor" if idade < 18 else "Maior")