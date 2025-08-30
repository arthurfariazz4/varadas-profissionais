contatos = []

def menu():
    print("\n1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Editar contato")
    print("5. Remover contato")
    print("6. Sair")

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    print("Contato adicionado!")

def listar():
    if not contatos:
        print("Nenhum contato.")
    else:
        for i, c in enumerate(contatos):
            print(f"{i+1}. {c['nome']} - {c['telefone']} - {c['email']}")

def buscar():
    nome = input("Nome para buscar: ")
    for c in contatos:
        if nome.lower() in c["nome"].lower():
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")
            return
    print("Contato não encontrado.")

def editar():
    listar()
    if contatos:
        try:
            i = int(input("Número do contato para editar: ")) - 1
            if 0 <= i < len(contatos):
                contatos[i]["nome"] = input("Novo nome: ")
                contatos[i]["telefone"] = input("Novo telefone: ")
                contatos[i]["email"] = input("Novo email: ")
                print("Contato atualizado!")
            else:
                print("Número inválido.")
        except:
            print("Entrada inválida.")

def remover():
    listar()
    if contatos:
        try:
            i = int(input("Número do contato para remover: ")) - 1
            if 0 <= i < len(contatos):
                contatos.pop(i)
                print("Contato removido!")
            else:
                print("Número inválido.")
        except:
            print("Entrada inválida.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            editar()
        elif opcao == "5":
            remover()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
