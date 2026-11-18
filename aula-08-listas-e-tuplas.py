"""
AULA 08 — LISTAS E TUPLAS

Objetivos:
- Criar e acessar listas.
- Adicionar, alterar e remover elementos.
- Conhecer tuplas e sua diferença em relação às listas.
"""

notas = [8.5, 7.0, 9.2]
print("Notas:", notas)
print("Primeira nota:", notas[0])

notas.append(6.5)
notas.insert(1, 10.0)
print("Após adicionar:", notas)

notas[0] = 9.0
notas.remove(7.0)
print("Após alterar e remover:", notas)

print("Quantidade de notas:", len(notas))
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Média:", sum(notas) / len(notas))

for indice, nota in enumerate(notas, start=1):
    print(f"Nota {indice}: {nota}")

# Tupla: coleção ordenada que não pode ser alterada.
dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta")
print("Dias:", dias_semana)

# DESAFIO:
# Crie uma lista com 5 nomes e exiba cada nome numerado.
