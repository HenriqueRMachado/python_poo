import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.

classe_clientes = importlib.import_module("01_restaurante_classes_principais")

print("\nBem vindo ao nosso restaurante!")

print("\nQual acao deseja realizar?")
pedido_um = classe_clientes.Pedidos()

while True:
    cliente_escolha = int(input("escolha 1 para mostrar o cardapio, ou 2 para fazer pedido: "))

    match(cliente_escolha):
        case 1:
            pedido_um.mostrar_cardapio()
        case 2:
            pedido_um.fazer_pedido()
            break
        case _:
            print("\nEsta opcao nao esta na lista de opcoes!")
        