import requests


def main() -> None:
    menu()


def menu() -> None:

    opcao: str = input(f"[C]-\tCadastrar\n[L]-\tLogin\n[Q]-\tSair\n :").lower()

    if opcao == 'c':
        cadastrar()
    elif opcao == 'l':
        login()
    elif opcao == 'q':
        exit()
    else:
        print("Opecão Inválido")
        menu()
    main()


def cadastrar() -> None:
    name: str = input("...Nome: ")
    user: str = input("...User: ")
    passw: str = input("...Senha: ")
    requests.post('http://127.0.0.1:8000/cadastro', params={"nome": name, "user": user, "senha": passw})


def login() -> None:
    usuario: str = input("...Usuário: ")
    passw: str = input("...Senha: ")
    requests.post('http://127.0.0.1:8000/login', params={"usuario": usuario, "senha": passw})


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f"Error # >> \t{err}")
        main()
