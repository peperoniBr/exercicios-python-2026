n = int(input("tabuada de qual numero: "))
int1 = int(input("qual valor inicial de tabuada: "))
int2 = int(input("qual valor final da tabuada: "))
for i in range(int1, int2 + 1):
    print(f"{n}x{i}={n*i}")
