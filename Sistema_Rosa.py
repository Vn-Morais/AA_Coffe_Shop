# Classe Produto
class Produto:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} | Ingredientes: {self.ingredientes}"

# Classe Cliente
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} | Tel: {self.telefone}"

# Classe Pedido
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(item.preco for item in self.itens)

    def __str__(self):
        lista = '\n'.join(f"- {item.nome} (R${item.preco:.2f})" for item in self.itens)
        return f"Pedido de {self.cliente.nome}:\n{lista}\nTotal: R${self.total():.2f}"

produtos = []
clientes = []
pedidos = []

# Funções
def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    ingredientes = input("Ingredientes (separados por vírgula): ")
    produto = Produto(nome, preco, ingredientes)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, p in enumerate(produtos, start=1):
            print(f"{i}. {p}")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    cliente = Cliente(nome, telefone)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c}")

def fazer_pedido():
    if not clientes or not produtos:
        print("Cadastre clientes e produtos antes de fazer pedidos.")
        return

    listar_clientes()
    idx_cliente = int(input("Escolha o número do cliente: ")) - 1
    cliente = clientes[idx_cliente]
    pedido = Pedido(cliente)

    while True:
        listar_produtos()
        idx_prod = int(input("Escolha o número do produto (0 para finalizar): "))
        if idx_prod == 0:
            break
        pedido.adicionar_produto(produtos[idx_prod - 1])

    pedidos.append(pedido)
    print("Pedido registrado com sucesso!")
    print(pedido)


def listar_pedidos():
    if not pedidos:
        print("Nenhum pedido registrado.")
    else:
        for p in pedidos:
            print(p)
            print("-" * 30)

# Menu principal
def menu():
    while True:
        print("\n--- COFFEE SHOPS TIA ROSA ---")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Cadastrar cliente")
        print("4. Listar clientes")
        print("5. Fazer pedido")
        print("6. Listar pedidos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            cadastrar_cliente()
        elif opcao == '4':
            listar_clientes()
        elif opcao == '5':
            fazer_pedido()
        elif opcao == '6':
            listar_pedidos()
        elif opcao == '0':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()