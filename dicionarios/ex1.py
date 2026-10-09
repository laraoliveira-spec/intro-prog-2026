nomes = ["Alex", "Mara", "Rosa"]
notas = [80, 70, 95]
print(f"Mara: {notas[nomes.index("Mara")]}")
for nome in nomes:
    print(f"{nome}: {notas[nomes.index(nome)]}")

notas = {
    "Alex": 80,
    "Mara": 70,
    "Rosa" : 95}
print(f"Mara: {notas["Mara"]}")
