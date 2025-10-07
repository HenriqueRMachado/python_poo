import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.

classe_fornecedor = importlib.import_module("01_restaurante_classes_principais")

from colorama import init, Fore, Back, Style
init()

print(Fore.GREEN + "Bem vindo ao sistema de fornecimento do restaurante." + Style.RESET_ALL)
forn = classe_fornecedor.Fornecedor()
forn2 = classe_fornecedor.Fornecedor()

while True:
    try:
        print(Fore.GREEN + "\n========MENU=======" + Style.RESET_ALL)
        print("1: Mostrar estoque")
        print("2: Alterar estoque")
        print(Fore.RED + "3: Sair" + Style.RESET_ALL) 
    
        fornecedor_escolha = int(input("\nEscolha uma das opcoes do menu acima: "))
        match(fornecedor_escolha):
            
            case 1:
                forn.mostra_estoque()
            
            case 2:
                abastecer = input('\nInforme o nome do produto que deseja abastecer no estoque: ')
                
                try:
                    qtde = int(input("\nInforme a quantidade do produto que deseja abastecer no estoque: "))
                except:
                    print("qtde precisa ser um numero")
                    
                forn2.atualiza_estoque(f"{abastecer}", {qtde})

            case 3:
                
                print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)
                import time as t
                t.sleep(2)
                break
        
            case _:
                print(Fore.RED + "\nEsta opcao nao esta na lista de opcoes!" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)