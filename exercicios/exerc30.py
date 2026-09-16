n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
op = input("Qual a operação desejada ou se que sabe (S) SOMA (SU) SUBTRAÇÃO (M) MULTIPLICAÇÃO (D) DIVISÃO")

if (op == "S"):
 print(f"Os numeros somado são {n1 + n2}")

elif (op == "SU"):
 print(f"Os numero subtraido são {n1 - n2}")

elif (op == "M"):
 print(f"Os numeros multiplicados são {n1*n2}")


elif (op == "D"):
 print(f"Os numeros divididos são {n1/n2}")

else:
  print("operacao invalida")
