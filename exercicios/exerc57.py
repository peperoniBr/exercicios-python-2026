contador = 0
print("Responda com 'S' para Sim ou 'N' para Não.\n")

p1 = input("Telefonou para a vítima? ").strip().upper()
if p1 == "S":
    contador += 1

p2 = input("Esteve no local do crime? ").strip().upper()
if p2 == "S":
    contador += 1

p3 = input("Mora perto da vítima? ").strip().upper()
if p3 == "S":
    contador += 1

p4 = input("Devia para a vítima? ").strip().upper()
if p4 == "S":
    contador += 1

p5 = input("Já trabalhou com a vítima? ").strip().upper()
if p5 == "S":
    contador += 1

print("\n--- Resultado ---")
if contador == 2:
    print("Classificação: Suspeita")
elif contador == 3 or contador == 4:
    print("Classificação: Cúmplice")
elif contador == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
