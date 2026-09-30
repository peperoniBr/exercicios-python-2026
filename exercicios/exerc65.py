numeros = []

for i in range(10):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

maior= max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
