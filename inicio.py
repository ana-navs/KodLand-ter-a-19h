import random

# Letras minúsculas // Números // @ #
regra = "abcdefghijklmnopqrstuvwxyz0123456789@#"

# Usuário insere o comprimento da senha 
tamanho = int(input("Digite o comprimento da senha: "))

senha_gerada = ""

for i in range(tamanho):
    senha_gerada += random.choice(regra)

print(f"Sua senha gerada é: {senha_gerada}")