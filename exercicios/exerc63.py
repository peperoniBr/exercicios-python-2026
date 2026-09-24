
impares = [0] * 50
numero = 1
for i in range(50):
    impares[i] = numero
    numero = numero + 2
print("Números ímpares armazenados no vetor:\n")
for i in range(50):
    print(impares[i], end=" ")
