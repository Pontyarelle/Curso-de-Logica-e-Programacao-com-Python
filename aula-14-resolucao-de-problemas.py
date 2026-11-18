"""
AULA 14 — ALGORITMOS E RESOLUÇÃO DE PROBLEMAS

Objetivos:
- Decompor um problema em etapas.
- Identificar entradas, processamento e saídas.
- Integrar condicionais, repetições, listas e funções.

Problema demonstrativo:
Sistema simples para registrar despesas e calcular o total.
"""

def registrar_despesas():
    despesas = []

    while True:
        descricao = input("Descrição da despesa (ou 'fim' para encerrar): ")
        if descricao.lower() == "fim":
            break

        try:
            valor = float(input("Valor: R$ "))
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
        except ValueError:
            print("Digite um valor numérico válido.")
            continue

        despesas.append({"descricao": descricao, "valor": valor})

    return despesas


def exibir_relatorio(despesas):
    print("\\n--- RELATÓRIO DE DESPESAS ---")
    for item in despesas:
        print(f"{item['descricao']}: R$ {item['valor']:.2f}")

    total = sum(item["valor"] for item in despesas)
    print(f"Total: R$ {total:.2f}")


if __name__ == "__main__":
    registros = registrar_despesas()
    exibir_relatorio(registros)

# DESAFIO:
# Amplie o programa para permitir excluir uma despesa e salvar os dados em arquivo.
