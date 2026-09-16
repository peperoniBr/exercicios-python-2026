n1 = int(input("Digite um numero: "))
n2 = int(input("Digite mais um numero: "))
n3 = int(input("Digite mais um numero: "))
n4 = int(input("Digite mais um numero: "))
n5 = int(input("Digite mais um numero: "))

if (n1 > n2 or n1> n3 or n1 > n4 or n1 > n5):
  print(f"O maior numero é {n1}")
elif (n2 > n1 or n2 > n3 or n2 > n4 or n2 > n5):
  print(f"O maior numerom é {n2}")
elif (n3 > n1 or n3 > n2 or n3 > n4 or n3 > n5):
  print(f"O maior numero é {n3}")
elif (n4 > n1 or n4 > n2 or n4 > n3 or n4 > n5):
  print(f"O maior numero é {n4}")
else:
  print(f"O maior numero é {n5}")