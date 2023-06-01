def linha():
    print("\n", "-" * 30, "\n")


def n():
    print("\n")


# Crie um programa que mostre um menu ao usuário com as seguintes opções:
# 1- Pesquisar
# 2- Cadastrar
# 3- Editar
# 4- Excluir
# 5- Exibir cadastros
# 6- Salvar
# 7- Sair
# O programa fará o gerenciamento de uma lista de contatos do WhatsApp,
# dessa forma, um dicionário deverá ser criado para armazenar as seguintes
# informações: "Nome contato":"N° WhatsApp"

contact = {}


def search_contact():
    name = input("Digite o nome do contato: ")
    if name in contact:
        print("Número do WhatsApp:", contact[name])
    else:
        print("Contato não encontrado.")


def add_contact():
    name = input("Digite o nome do contato: ")
    number_contact = input("Digite o número do WhatsApp: ")
    contact[name] = number_contact
    print("Contato cadastrado com sucesso.")


def edit_contact():
    name = input("Digite o nome do contato: ")
    if name in contact:
        print("Contato encontrado. Insira as novas informações:")
        number_contact = input("Digite o novo número do WhatsApp: ")
        contact[name] = number_contact
        print("Contato editado com sucesso.")
    else:
        print("Contato não encontrado.")


def remove_contact():
    name = input("Digite o nome do contato: ")
    if name in contact:
        del contact[name]
        print("Contato excluído com sucesso.")
    else:
        print("Contato não encontrado.")


def view_contact():
    if len(contact) == 0:
        print("Nenhum contato cadastrado.")
    else:
        print("Contatos cadastrados:")
        for name, number_contact in contact.items():
            print("Nome:", name)
            print("Número do WhatsApp:", number_contact)
            print("")


def save_contact():
    if (len(contact) == 0 ):
        n()
        print("Nenhum contato cadastrado!")
    else:
        try:
            with open("E:/Neto - Python/temp/contacts.csv", "w") as arquivo:
                for name, number_contact in contact.items():
                    arquivo.write(name + ":" + number_contact + "\n")
            print("Cadastros salvos com sucesso.")
        except:
            print("Erro ao salvar os cadastros.")


def load_contact():
    try:
        with open("contatos.txt", "r") as arquivo:
            line = arquivo.readlines()
            for line in line:
                name, number_contact = line.strip().split(":")
                contact[name] = number_contact
        print("Cadastros carregados com sucesso.")
    except:
        print("Erro ao carregar os cadastros.")


load_contact()

while True:
    print("----- Menu -----")
    print("1 - Pesquisar")
    print("2 - Cadastrar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Exibir cadastros")
    print("6 - Salvar")
    print("7 - Sair")

    option = input("Digite a opção desejada: ")

    if option == "1":
        search_contact()
    elif option == "2":
        add_contact()
    elif option == "3":
        edit_contact()
    elif option == "4":
        remove_contact()
    elif option == "5":
        view_contact()
    elif option == "6":
        save_contact()
    elif option == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
