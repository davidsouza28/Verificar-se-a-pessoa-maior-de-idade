# Programa básico para iniciantes em Python

# Pedir o nome do usuário
nome = input("Qual é o seu nome? ")

# Pedir o ano de nascimento e converter para número inteiro
ano_nascimento = int(input("Em que ano você nasceu? "))

# Calcular a idade 
from datetime import datetime
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

# Mostrar uma mensagem personalizada
print(f"Olá, {nome}! Você tem {idade} anos.")

# Verificar se é maior de idade
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você ainda é menor de idade.")