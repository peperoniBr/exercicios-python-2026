import calendar

ano = int(input("Digite um ano: "))

resul = calendar.calendar(ano)

eh_bissexto = calendar.isleap(ano)

if(eh_bissexto):
  print("É BISSEXTO")
else:
  print("NÃO É BISSEXTO")

print(resul)
