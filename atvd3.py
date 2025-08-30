pokemons = []

def menu():
    print("\n1. Cadastrar Pokémon")
    print("2. Listar Pokémons")
    print("3. Batalhar")
    print("4. Sair")

def cadastrar():
    nome = input("Nome: ")
    tipo = input("Tipo: ")
    atk = int(input("Ataque: "))
    vida = int(input("Pontos de vida: "))
    pokemons.append({"nome": nome, "tipo": tipo, "atk": atk, "vida": vida})
    print("Pokémon cadastrado!")

def listar():
    for i, p in enumerate(pokemons):
        print(f"{i+1}. {p['nome']} - Tipo: {p['tipo']} - Atk: {p['atk']} - Vida: {p['vida']}")

def batalha():
    listar()
    a = int(input("Número do primeiro Pokémon: ")) - 1
    b = int(input("Número do segundo Pokémon: ")) - 1

    p1 = pokemons[a].copy()
    p2 = pokemons[b].copy()

    while p1["vida"] > 0 and p2["vida"] > 0:
        p2["vida"] -= p1["atk"]
        p1["vida"] -= p2["atk"]
        print(f"\n{p1['nome']} vida: {max(p1['vida'], 0)}")
        print(f"{p2['nome']} vida: {max(p2['vida'], 0)}")

    if p1["vida"] <= 0 and p2["vida"] <= 0:
        print("Empate!")
    elif p1["vida"] > 0:
        print(f"{p1['nome']} venceu!")
    else:
        print(f"{p2['nome']} venceu!")

def main():
    while True:
        menu()
        op = input("Escolha: ")
        if op == "1": cadastrar()
        elif op == "2": listar()
        elif op == "3": batalha()
        elif op == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
