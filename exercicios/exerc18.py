dep = float(input("digite um valor de deposito  "))
jur = float(input("digite a taxa de juros "))
rend = jur / 100 * dep
ttl = rend + dep
print(f"o redimento foi de {rend} e o valor total com redimento é {ttl}")