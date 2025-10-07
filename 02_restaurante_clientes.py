import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.

from colorama import init, Fore, Back, Style
init()

classe_clientes = importlib.import_module("01_restaurante_classes_principais")

print(Fore.GREEN + "\nBem vindo ao nosso restaurante!" + Style.RESET_ALL)

pedido_um = classe_clientes.Pedidos()

while True:
    
    try:
        
        print(Fore.GREEN + "\n=====MENU====" + Style.RESET_ALL)
        print("1: Mostrar cardapio")
        print("2: Fazer pedido")
        print(Fore.RED + "3: Sair" + Style.RESET_ALL)  
        
        cliente_escolha = int(input("\nEscolha uma das opcoes do menu acima: "))

        match(cliente_escolha):
            case 1:
                pedido_um.mostrar_cardapio()
            case 2:
                pedido_um.fazer_pedido()
                break
            case 3:
                
                print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)
                import time as t
                t.sleep(2)
                break
            
            case _:
                print(Fore.RED + "\nEsta opcao nao esta na lista de opcoes!" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)