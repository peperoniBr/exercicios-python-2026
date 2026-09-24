palavra = input("digite a palavra\n")
cons = [""] * 100
j = 0

for i in range(len(palavra)):

  char = palavra[i]

  if (
      char != "a"
      and char != "e"
      and char != "i"
      and char != "o"
      and char != "u"
  ):
    cons[j] = char
    print(cons[j])
    j += 1
