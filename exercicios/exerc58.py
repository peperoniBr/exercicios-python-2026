litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

preco_alcool = 3.90
preco_gasolina = 5.50


if tipo_combustivel == 'A':
    if litros <= 20:
        porcentagem_desconto = 0.03  
    else:
        porcentagem_desconto = 0.05  
    
    valor_total = litros * preco_alcool * (1 - porcentagem_desconto)
    print(f"Valor a ser pago pelo Álcool: R$ {valor_total:.2f}")

elif tipo_combustivel == 'G':
    if litros <= 20:
        porcentagem_desconto = 0.04  
    else:
        porcentagem_desconto = 0.06  
    valor_total = litros * preco_gasolina * (1 - porcentagem_desconto)
    print(f"Valor a ser pago pela Gasolina: R$ {valor_total:.2f}")
else:
    print("Tipo de combustível inválido! Use 'A' para álcool ou 'G' para gasolina.")
