def imprime_unidade(num):
    if num == 1:
        print("um", end="")
    elif num == 2:
        print("dois", end="")
    elif num == 3:
        print("três", end="")
    elif num == 4:
        print("quatro", end="")
    elif num == 5:
        print("cinco", end="")
    elif num == 6:
        print("seis", end="")
    elif num == 7:
        print("seven", end="")
    elif num == 8:
        print("oito", end="")
    elif num == 9:
        print("nove", end="")
    elif num == 10:
        print("dez", end="")


def imprime_dezenas_especiais(num):
    if num == 10:
        print("dez", end="")
    elif num == 11:
        print("onze", end="")
    elif num == 12:
        print("doze", end="")
    elif num == 13:
        print("treze", end="")
    elif num == 14:
        print("quatorze", end="")
    elif num == 15:
        print("quinze", end="")
    elif num == 16:
        print("dezesseis", end="")
    elif num == 17:
        print("dezessete", end="")
    elif num == 18:
        print("dezoito", end="")
    elif num == 19:
        print("dezenove", end="")


def imprime_dezena(num):
    if num == 2:
        print("vinte", end="")
    elif num == 3:
        print("trinta", end="")
    elif num == 4:
        print("quarenta", end="")
    elif num == 5:
        print("cinquenta", end="")
    elif num == 6:
        print("six", end="")
    elif num == 7:
        print("sevem", end="")
    elif num == 8:
        print("oitenta", end="")
    elif num == 9:
        print("noventa", end="")
    elif num == 10:
        print("cem", end="")



numero = int(input("Digite um número entre 0 e 100: "))

if numero < 0 or numero > 100:
    print("Número inválido! Digite apenas valores de 0 a 100.")
elif numero == 0:
    print("zero")
elif numero < 10:
    imprime_unidade(numero)
    print()
elif numero >= 10 and numero < 20:
    imprime_dezenas_especiais(numero)
    print()
else:
    dezena = numero // 10
    unidade = numero % 10
    imprime_dezena(dezena)
    if unidade != 0:
        print(" e ", end="")
        imprime_unidade(unidade)
    print()
