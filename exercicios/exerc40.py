nota = 999999999999999999999999999999
#   while = enquanto
while nota < 0 or nota > 10:
  nota = float(input("escreva uma nota entre 0 e 10: "))
  if(nota < 0 or nota > 10):
    print("escreva novamente a nota ENTRE 0 E 10")
print("nota valida")

