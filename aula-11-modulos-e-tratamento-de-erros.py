"""
AULA 11 — MODULARIZAÇÃO E TRATAMENTO DE ERROS

Objetivos:
- Importar módulos.
- Reutilizar recursos da biblioteca padrão.
- Tratar entradas inválidas com try/except.
"""

import math
import random

numero = 25
print("Raiz quadrada:", math.sqrt(numero))
print("Número aleatório entre 1 e 10:", random.randint(1, 10))

try:
    valor = float(input("Digite um número: "))
    resultado = 100 / valor
except ValueError:
    print("Entrada inválida: digite um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Resultado:", resultado)
finally:
    print("Fim da operação.")

# DESAFIO:
# Solicite a idade do usuário e trate o erro caso ele não digite um inteiro.
