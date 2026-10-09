import random
numeros = []
for i in range(101):
    numeros.append(random.randint(0, 100))
print(numeros)
print(f"Número diferente: {len(set(numeros))}")
#randint gera numeros no intervalo dito, nesse caso de 0 a 100;