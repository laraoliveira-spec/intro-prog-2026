temperaturas = []

for i in range(12):
    temperatura = float(input(f"Digite a temperatura do minuto {i + 1}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

maior = max(temperaturas)

indice = temperaturas.index(maior)

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1

print("\n--- RESULTADOS ---")
print("Temperaturas:", temperaturas)
print("Média:", media)
print("Maior temperatura:", maior)
print("Índice da primeira maior temperatura:", indice)
print("Leituras acima da média:", acima_media)
