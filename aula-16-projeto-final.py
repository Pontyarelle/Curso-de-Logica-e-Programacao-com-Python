"""
AULA 16 — PROJETO PRÁTICO FINAL

Projeto demonstrativo: Sistema de cadastro de estudantes.

Conteúdos integrados:
- Variáveis e entrada de dados.
- Listas e dicionários.
- Condicionais e repetição.
- Funções.
- Tratamento de erros.

O programa mantém os dados em memória durante sua execução.
"""

estudantes = []


def cadastrar_estudante():
    nome = input("Nome do estudante: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("A idade deve ser maior que zero.")
            return
    except ValueError:
        print("Digite uma idade válida.")
        return

    estudantes.append({"nome": nome, "idade": idade})
    print("Estudante cadastrado com sucesso!")


def listar_estudantes():
    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return

    print("\\n--- ESTUDANTES CADASTRADOS ---")
    for indice, estudante in enumerate(estudantes, start=1):
        print(f"{indice}. {estudante['nome']} — {estudante['idade']} anos")


def mostrar_menu():
    print("\\n===== SISTEMA DE ESTUDANTES =====")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# PROPOSTAS DE EVOLUÇÃO:
# 1. Permitir pesquisar estudante pelo nome.
# 2. Permitir remover um cadastro.
# 3. Salvar e carregar os cadastros em arquivo.
# 4. Organizar o projeto em módulos.
# 5. Criar um README.md explicando como executar o sistema.
# 6. Publicar o projeto no GitHub.
