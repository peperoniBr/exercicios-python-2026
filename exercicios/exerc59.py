popA = 80000
popB = 200000
ano = 0

while popA <= popB:
    popA = popA * 1.03
    popB = popB * 1.015
    ano = ano + 1

print(ano)
