lado1 =  int(input("escreva o 1° lado\n"))
lado2 = int(input("escreva o 2° lado\n"))
lado3 = int(input("escreva o 3° lado\n"))
if(lado1  == lado2 and lado3):
    print(f"equiletero")
elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
  print(f"escaleno")
else:
  print(f"isoseles")