ano = int(input("Digite o seu ano de nascimento: "))
anoA = int(input("Digite o ano atual: "))
idade = anoA - ano    
meses = idade*12
dias = 365*idade
semanas = 52*idade
anoatual = 2019 - ano

print(f"Sua idade atual é {idade}")
print(f"Sua idade em meses é {meses}")
print(f"Sua idade em dias é {dias}")
print(f"Sua idade em semanas é {semanas}")
print(f"Sua idade em 2019 é {anoatual-2019}")



