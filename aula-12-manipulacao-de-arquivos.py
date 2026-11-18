"""
AULA 12 — MANIPULAÇÃO DE ARQUIVOS

Objetivos:
- Criar, ler e escrever arquivos de texto.
- Conhecer os modos w, a e r.
- Utilizar with open().
"""

# Escreve (ou substitui) o conteúdo do arquivo.
with open("anotacoes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Curso de Lógica e Programação com Python\n")
    arquivo.write("Aula 12: manipulação de arquivos\n")

# Adiciona uma nova linha sem apagar o conteúdo anterior.
with open("anotacoes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Estamos aprendendo a salvar informações.\n")

# Lê o conteúdo.
with open("anotacoes.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# DESAFIO:
# Peça três nomes ao usuário, salve-os em um arquivo e depois leia o arquivo.
