h = float(input("qual a sua altura? "))
s = input("digite o seu genero ")
if(s == "h"):
  print(f"{(72.7*h)-58: .2f} é seu peso ideal")
else:
  print(f"{(62.1*h)-44.7: .2f} é seu peso ideal")	
