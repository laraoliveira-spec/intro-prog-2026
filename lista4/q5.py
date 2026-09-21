numA = int(input("Número A: "))
numB = int(input("Número B: "))
if numA < numB:
    numA, numB = numB, numA
while numB != 0:
    resto = numA % numB
    numA = numB
    numB = resto
print(f"MDC = {numA}")