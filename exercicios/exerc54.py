qtd_0_25 = 0
qtd_26_50 = 0
qtd_51_75 = 0
qtd_76_100 = 0

num = int(input("Digite o número (negativo para sair):\n"))


while num >= 0:
    if 0 <= num <= 25:
        qtd_0_25 += 1
    elif 26 <= num <= 50:
        qtd_26_50 += 1
    elif 51 <= num <= 75:
        qtd_51_75 += 1
    elif 76 <= num <= 100:
        qtd_76_100 += 1
    
   
    num = int(input("Digite o número (negativo para sair):\n"))


print("\nQuantidade em cada intervalo:")
print(f"[0-25]: {qtd_0_25}")
print(f"[26-50]: {qtd_26_50}")
print(f"[51-75]: {qtd_51_75}")
print(f"[76-100]: {qtd_76_100}")
