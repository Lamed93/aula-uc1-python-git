# for mensagem in range(1,11):
#     print(f"Contagem: {mensagem}")

# numero = 1

# while numero <=10:
#     print(f"número: {numero}")
#     numero += 1 #incremento (++, ou, numero = numero + 1)

# senha = ""
# while senha != "python":
#     senha = input("Digite a sua senha: ")

# print("Acesso permitido!")

# texto = "python"
# for letra in texto:
#     print(f"A letra é: {letra}")

# senha = ""
# while senha != 'python':
#     senha = input("Digite a sua senha: ")
#     if senha == 'python':
#         break
#     print("Senha errada. Coloque a senha correta.")

# print("Acesso Permitido")

usuario_correto = "victor"
senha_correta = "debian1234"

while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario.lower() == usuario_correto and senha == senha_correta: #função lower, capitalize e upper
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário e senha incorreta! Tente novamente!")

