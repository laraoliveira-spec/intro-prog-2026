paisA = 80000
paisB = 20000
anos = 0

while paisA < paisB:
    paisA = paisA + (paisA * 3 / 100)
    paisB = paisB + (paisB * 1.5 / 100)
    anos = anos + 1
print(f"FOram necessários {anos} anos para o país B igualar/passar do país A.")