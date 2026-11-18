"""
AULA 06 — ESTRUTURAS DE REPETIÇÃO

Objetivos:
- Utilizar while e for.
- Trabalhar com contadores e acumuladores.
- Conhecer break e continue.
"""

# FOR: repetir uma quantidade conhecida de vezes.
for numero in range(1, 6):
    print("Contagem:", numero)

# WHILE: repetir enquanto uma condição for verdadeira.
contador = 1
while contador <= 3:
    print("Repetição:", contador)
    contador += 1

# Acumulador: soma de vários valores.
soma = 0
for numero in range(1, 6):
    soma += numero
print("Soma de 1 a 5:", soma)

# DESAFIO:
# Solicite números ao usuário até que ele digite 0.
# Ao final, mostre a soma dos números digitados.
