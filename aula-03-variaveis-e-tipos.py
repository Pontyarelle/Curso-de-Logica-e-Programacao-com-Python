"""
AULA 03 — VARIÁVEIS, TIPOS DE DADOS E ENTRADA DE INFORMAÇÕES

Objetivos:
- Criar variáveis.
- Identificar int, float, str e bool.
- Ler dados com input() e converter tipos.
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros (ex.: 1.75): "))
estuda = True

print(f"Olá, {nome}!")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
print(f"Está estudando? {estuda}")

# Verifique os tipos:
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estuda))

# DESAFIO:
# Solicite dois números ao usuário e exiba os valores informados.
