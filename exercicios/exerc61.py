notas = []
soma = 0.0

for i in range(4):
  nota = float(input(f"Digite a nota {i + 1}: "))
  notas.append(nota)
  soma += nota

media = soma / 4

print(f"\nA média da turma é: {media}")
print("Notas acima da média:")

for nota in notas:
  if nota > media:
    print(nota)
