livros = []

def menu():
    print("\n1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Remover livro")
    print("6. Sair")

def adicionar():
    titulo = input("Título: ")
    autor = input("Autor: ")
    livros.append({"titulo": titulo, "autor": autor, "status": "disponível"})
    print("Livro adicionado!")

def listar():
    if not livros:
        print("Nenhum livro.")
    else:
        for l in livros:
            print(f"- {l['titulo']} | {l['autor']} | {l['status']}")

def emprestar():
    titulo = input("Título do livro para emprestar: ")
    for l in livros:
        if l["titulo"].lower() == titulo.lower() and l["status"] == "disponível":
            l["status"] = "emprestado"
            print("Livro emprestado!")
            return
    print("Livro não encontrado ou já emprestado.")

def devolver():
    titulo = input("Título do livro para devolver: ")
    for l in livros:
        if l["titulo"].lower() == titulo.lower() and l["status"] == "emprestado":
            l["status"] = "disponível"
            print("Livro devolvido!")
            return
    print("Livro não encontrado ou já disponível.")

def remover():
    titulo = input("Título do livro para remover: ")
    for l in livros:
        if l["titulo"].lower() == titulo.lower():
            livros.remove(l)
            print("Livro removido!")
            return
    print("Livro não encontrado.")

def main():
    while True:
        menu()
        op = input("Escolha: ")
        if op == "1": adicionar()
        elif op == "2": listar()
        elif op == "3": emprestar()
        elif op == "4": devolver()
        elif op == "5": remover()
        elif op == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
