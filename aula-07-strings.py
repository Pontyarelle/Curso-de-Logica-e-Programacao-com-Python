"""
AULA 07 — STRINGS E MANIPULAÇÃO DE TEXTO

Objetivos:
- Acessar caracteres por índices.
- Utilizar fatiamento e métodos de strings.
- Pesquisar e modificar textos.
"""

frase = "Aprender Python é praticar!"

print("Texto:", frase)
print("Primeiro caractere:", frase[0])
print("Último caractere:", frase[-1])
print("Primeiros 8 caracteres:", frase[:8])
print("Em maiúsculas:", frase.upper())
print("Em minúsculas:", frase.lower())
print("Substituição:", frase.replace("praticar", "programar"))
print("Contém Python?", "Python" in frase)

nome = "   Maria Silva   "
print("Sem espaços nas extremidades:", nome.strip())

# DESAFIO:
# Peça uma frase ao usuário e mostre:
# quantidade de caracteres, texto em maiúsculas e texto em minúsculas.
