#Solicite um número e verifique se está entre 10 e 20.

numero = int(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print(f"{numero} está entre 10 e 20")
else:
    print(f"{numero} fora do intervalo!")