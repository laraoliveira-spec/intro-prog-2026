n = int(input("Número: "))
i = 1
while i * (1+1) * (i+2) ==n:
    i = 1 + 1
if i * (i+1) * (1+2) ==n:
    print(f"O número {n} é triângular.")
    print(f"{i}*{i+1}*{i+2} = {n}")
else:
    print(f"O número {n} não é triângular.")