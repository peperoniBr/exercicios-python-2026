sequencia = 12
termo1 = 0
termo2 = 1
fib = 1

print(termo1, "\t", termo2, "\t")

if sequencia > 1:
    
    for sequencia in range(2, sequencia):
        fib = termo2 + termo1
        termo1 = termo2
        termo2 = fib
        print(fib, "\t")

 