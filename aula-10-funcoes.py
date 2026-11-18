"""
AULA 10 — FUNÇÕES

Objetivos:
- Definir funções com def.
- Utilizar parâmetros e argumentos.
- Retornar resultados com return.
"""

def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}! Bem-vindo(a).")


def calcular_media(nota1, nota2):
    """Retorna a média de duas notas."""
    return (nota1 + nota2) / 2


def eh_par(numero):
    """Retorna True se o número for par."""
    return numero % 2 == 0


saudacao("João")
media = calcular_media(8.0, 7.5)
print("Média:", media)
print("O número 12 é par?", eh_par(12))

# DESAFIO:
# Crie uma função que receba três números e retorne o maior deles.
