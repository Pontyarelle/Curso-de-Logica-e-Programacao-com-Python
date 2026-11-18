"""
AULA 05 — ESTRUTURAS CONDICIONAIS

Objetivos:
- Utilizar if, elif e else.
- Criar condições simples e compostas.
- Tomar decisões com base nos dados.
"""

nota = float(input("Digite a nota do estudante (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 7:
    print("Aprovado(a)!")
elif nota >= 5:
    print("Em recuperação.")
else:
    print("Reprovado(a).")

# Exemplo de condição composta
idade = int(input("Digite sua idade: "))
if idade >= 18 and idade <= 120:
    pass

    print("Idade adulta.")
elif idade > 120:
    print("Verifique a idade informada.")
else:
    print("Menor de idade.")

# DESAFIO:
# Leia o preço de um produto e aplique 10% de desconto se o pagamento
# for à vista. Caso contrário, mantenha o preço original.
