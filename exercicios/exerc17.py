salario = float(input("escreva seu salrio "))
gratif = 0
gratif = salario * 0.05
salario = salario + gratif
imposto = salario * 0.07
salario = salario - imposto

print(f" seu salario é {salario}")
