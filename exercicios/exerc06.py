n1 = int(input("digite o 1° numero"))
n2 = int(input("digite o 2° numero"))
op = input("escreva a operacao desejada SOMA ou SUBTRACAO")
if(op == "SOMA"):
  print(n1+n2)
elif(op == "SUBTRACAO"):
  print(n1-n2)
else:
  print("operacao invalida")