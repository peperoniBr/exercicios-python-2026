
alunos = []
notas = []
for i in range(4):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    
    linha = []
    soma = 0
    
    for j in range(4):
        n = float(input(f"Digite a nota {j+1}: "))
        linha.append(n)
        soma = soma + n
    
    media = soma / 4
    linha.append(media)
    
    notas.append(linha)
    print()


print("=== RESULTADOS ===")
for i in range(4):
    print("Aluno:", alunos[i])
    print("Notas:", notas[i][0], "-", notas[i][1], "-", notas[i][2], "-", notas[i][3])
    print("Média:", notas[i][4])
    print("------------------")