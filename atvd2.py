tarefas = []

def menu():
    print("\n1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Filtrar por status")
    print("6. Sair")

def adicionar():
    desc = input("Descrição da tarefa: ")
    tarefas.append({"desc": desc, "status": "pendente"})
    print("Tarefa adicionada!")

def listar():
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        for i, t in enumerate(tarefas):
            print(f"{i+1}. {t['desc']} - {t['status']}")

def concluir():
    listar()
    i = int(input("Número da tarefa para concluir: ")) - 1
    if 0 <= i < len(tarefas):
        tarefas[i]["status"] = "concluída"
        print("Tarefa marcada como concluída!")

def remover():
    listar()
    i = int(input("Número da tarefa para remover: ")) - 1
    if 0 <= i < len(tarefas):
        tarefas.pop(i)
        print("Tarefa removida!")

def filtrar():
    status = input("Filtrar por (pendente/concluída): ")
    for t in tarefas:
        if t["status"] == status:
            print(f"- {t['desc']}")

def main():
    while True:
        menu()
        op = input("Escolha: ")
        if op == "1": adicionar()
        elif op == "2": listar()
        elif op == "3": concluir()
        elif op == "4": remover()
        elif op == "5": filtrar()
        elif op == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
