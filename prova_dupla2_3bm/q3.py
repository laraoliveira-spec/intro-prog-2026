pontos = []
for i in range(1, 4):
    x = float(input(f"X{i}: "))
    y = float(input(f"Y{i}: "))
    pontos.append((x, y))
print("Pontos cadastrados: ")
for p in pontos:
    print(f'- {p}')
for i in range