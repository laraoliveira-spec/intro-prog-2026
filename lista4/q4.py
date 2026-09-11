# FIBONACCI: 1, 1, 2, 3, 3, 8, 13, 21, 34, 33
F = [1, 1]
n = int(input("Digite um número: "))
for i in range(2, n):
    F.append(F[i-1] + F[i-2])
print(f"F({n}) = {F[-1]}")