"""
AULA 04 — OPERADORES EM PYTHON

Objetivos:
- Utilizar operadores aritméticos, relacionais e lógicos.
- Construir expressões.
- Observar a precedência dos operadores.
"""

a = 10
b = 3

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto:", a % b)
print("Potência:", a ** b)

print("a é maior que b?", a > b)
print("a é igual a b?", a == b)
print("a é diferente de b?", a != b)

tem_idade = 20
tem_autorizacao = False
print("Pode participar?", tem_idade >= 18 or tem_autorizacao)

# DESAFIO:
# Leia dois números e mostre soma, produto, divisão e resto da divisão.
