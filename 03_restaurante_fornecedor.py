import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.

classe_fornecedor = importlib.import_module("01_restaurante_classes_principais")

from colorama import init, Fore, Back, Style
init()

print("Bem vindo ao sistema de fornecimento do restaurante.")

while True:
    abastecer = input(
        '\nInforme o nome do produto que deseja abastecer no estoque: (digite "sair" para sair): ').lower()
    if abastecer.lower() == "sair":

        print("\nO programa esta encerrando...")

        import time as t
        t.sleep(2)

        break
    else:
        try:
            qtde = int(input("\nInforme a quantidade do produto que deseja abastecer no estoque: "))
        except:
            print("qtde precisa ser um numero")
        
    forn = classe_fornecedor.Fornecedor()
    forn.atualiza_estoque(f"{abastecer}", {qtde})
