paisA = 80000
paisB = 200000
anos = 0
while paisA < paisB:
    paisA += paisA * 0.03
    paisB += paisB * 0.015
    anos += 1
print(f"País A superou o País B em {anos} anos.")
print(f"País A: {paisA:.0f} habitantes.")
print(f"País A: {paisB:.0f} habitantes.")