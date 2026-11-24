# total = 0
# contador = 0
# while True:
#     numero = int(input("Digite um número (0 para sair): "))
#     if numero == 0:
#         break
#     total += numero
#     contador += 1
#     media = total / contador
#     print(f"Soma total: {total}")
#     print(f"A média é: {media:.2f}")

# numero = int(input("Gerar a tabuada de: "))
# inicio = int(input("Digite o valor de inicio: "))
# fim = int(input("Fim: "))

# for i in range(inicio, fim +1):
#     print(f"{numero} x {i} = {numero * i}")

tentativas = 3
senha_correta = "admin"

while tentativas > 0:
    senha = input("Digite a sua senha: ")
    if senha == senha_correta:
        print("Login autorizado.")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta! Restam {tentativas} tentativas.")
if tentativas == 0:
    print("Acesso bloqueado por tentativas excessivas!")