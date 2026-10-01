alunos = []

print("--- CADASTRO DOS ALUNOS DO 2DS ---")

for i in range(11):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(nome)

print("\n--- LISTA FINAL DA TURMA 2DS ---")

for i in range(11):
    print(f"{i + 1} - {alunos[i]}")
