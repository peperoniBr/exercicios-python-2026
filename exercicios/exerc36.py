n = int(input("digite um numero correspondente ao dia da semana "))
if(n>=1 or n<=7):
  if(n == 1):
    print("domingo")
  elif(n == 2):
    print("segunda")
  elif(n == 3):
    print("terça")
  elif(n == 4):
    print("quarta")
  elif(n == 5):
    print("quinta")
  elif(n == 6):
    print("sexta")
  elif(n == 7):
    print("sabado")
else:
  print("o numero tem q estar entre 1-7")