a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if(a == 0):
 print("A equação não é do segundo grau igual o elton")

 d = b**2 - (4*a*c)
if(d < 0):
   print("A equação não possui raizes reais porque sim.")

elif(d == 0):
   print("Só possui uma raiz real")

elif(d > 0):
   print("A equação possui duas raizes reais ")

