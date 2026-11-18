"""
AULA 13 — INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS

Objetivos:
- Compreender classes, objetos, atributos e métodos.
- Utilizar o método construtor __init__().
"""

class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def apresentar(self):
        print(f"Meu nome é {self.nome} e estudo {self.curso}.")


aluno1 = Aluno("Mariana", "Redes de Computadores")
aluno2 = Aluno("Pedro", "Informática")

aluno1.apresentar()
aluno2.apresentar()

print("Nome do primeiro aluno:", aluno1.nome)

# DESAFIO:
# Crie uma classe Produto com nome, preço e estoque.
# Adicione um método que apresente os dados do produto.
