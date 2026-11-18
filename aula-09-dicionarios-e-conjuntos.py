"""
AULA 09 — DICIONÁRIOS E CONJUNTOS

Objetivos:
- Armazenar dados em pares chave/valor.
- Consultar, incluir, alterar e remover dados.
- Conhecer conjuntos (set).
"""

aluno = {
    "nome": "Ana",
    "idade": 17,
    "curso": "Redes de Computadores"
}

print("Nome:", aluno["nome"])
print("Curso:", aluno.get("curso"))

aluno["idade"] = 18
aluno["matricula"] = "2026001"
aluno.pop("curso")

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Conjuntos armazenam elementos únicos.
turma_a = {"Ana", "Bruno", "Carlos"}
turma_b = {"Bruno", "Daniel", "Eva"}

print("União:", turma_a | turma_b)
print("Interseção:", turma_a & turma_b)
print("Somente na turma A:", turma_a - turma_b)

# DESAFIO:
# Crie um dicionário para representar um produto com nome, preço e estoque.
# Atualize o estoque e exiba todas as informações.
