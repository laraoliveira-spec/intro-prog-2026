tempo = float(input(f"Tempo"))
tempos.append(tempo)
print("Tempos registrados:")
for t in tempos:
    print(f"- {t} segundos.")
print(f"Menor tempo: {min(tempos)} segundos.")
print(f"Maior tempo: {max(tempos)} segundos.")
print(f"Média dos tempos: {sum(tempos)/len(tempos)} segundos")
print(f"Posição do primeiro tempo mais rápido: {tempos.index(min(tempos))+1} segundos")