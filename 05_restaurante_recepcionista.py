import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.
classe_funcionarios = importlib.import_module("01_restaurante_classes_principais")

from colorama import init, Fore, Back, Style
init()


def funcoes_cadastro_clientes():

    print(Fore.GREEN + "Bem vindo(a) ao sistema de cadastro de clientes do restaurante!" + Style.RESET_ALL)

    while True:
        print(Fore.GREEN + "\n============== MENU =============" + Style.RESET_ALL)

        print("1 - Cadastrar cliente")
        print("2 - Listar todos os clientes")
        print("3 - Buscar cliente por id")
        print("4 - Alterar dados de cliente")
        print("5 - Excluir cadastro de cliente")
        print(Fore.RED + "6 - Sair do menu"  + Style.RESET_ALL)

    
        try:
            recepcionista_escolha = int(input("\nSelecione qual das acoes ira realizar no sistema: "))

            match(recepcionista_escolha):
                case 1:
                    
                    try:
                        print("\nPreencha as informações para cadastrar um funcionario: ")
                        nome = input("\nInforme o nome do cliente: ")
                        cpf = input("Informe o CPF do cliente: ")
                        celular = input("Informe o telefone do cliente: ")
                        
                        cadastra_cliente = classe_funcionarios.Clientes_Restaurante(nome, cpf, celular)
                        
                        cadastra_cliente.nome_cliente = nome
                        cadastra_cliente.cpf_cliente = cpf
                        cadastra_cliente.celular_cliente = celular
                        
                        cadastra_cliente.cadastrar_clientes()
                    except ValueError as error:
                        print(error)
                    
                case 2:
                    mostra_clientes = classe_funcionarios.Clientes_Restaurante(nome_cliente=None, cpf_cliente=None, celular_cliente=None)
                    mostra_clientes.mostrar_todos_clientes()
                    
                case 3:
                    print(Fore.RED + "\nAtencao, para consultar um cliente especifico, e necessario o id. Para saber o id, execute a acao 2 e consulte os clientes cadastrados!" + Style.RESET_ALL)

                    id_clientes_consulta = int(input("Informe o id do cliente que deseja consultar no sistema:"))
                    consulta_cliente = classe_funcionarios.Clientes_Restaurante(None, None, None)
                    consulta_cliente.mostrar_cliente(id_clientes_consulta)
                    
                case 4:
                    try:
                        print(Fore.RED + "\nAtencao, para alterar o cadastro de um cliente, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
                    
                        id_cliente_alterar = int(input("\nInforme o id do funcionario que deseja alterar no sistema: "))
                        
                        if not id_cliente_alterar:
                            print("id nao pode ser vazio")
                            return
                        
                        if id_cliente_alterar < 0:
                            print("Os ids comecam a partir de 1")
                        elif id_cliente_alterar < 3:
                            print("Os ids 1 e 2 nao podem ser alterados")
                        else:
                        
                            print(f"Alterando o cliente {classe_funcionarios.Clientes_Restaurante.cadastro_clientes[f"id{id_cliente_alterar}"]}")
                            
                            print("\nInforme as novas informações que deseja alterar: ")
                            altera_nome_cliente = input("Informe o novo nome: ")
                            altera_cpf_cliente = input("Informe o novo CPF: ")
                            altera_celular_cliente = input("Informe o novo celular: ")
                            
                            altera_cliente = classe_funcionarios.Clientes_Restaurante(altera_nome_cliente, altera_cpf_cliente, altera_celular_cliente)

                            altera_cliente.nome_cliente = altera_nome_cliente
                            altera_cliente.cpf_cliente = altera_cpf_cliente
                            altera_cliente.celular_cliente = altera_celular_cliente
                            
                            altera_cliente.alterar_clientes(id_cliente_alterar)
                    except ValueError as error:
                        print(error)
                case 5:
                    id_exclui_clientes = int(input("Informe o id do cliente que deseja excluir: "))
                    if not id_exclui_clientes:
                        print("id nao pode ser vazio")
                        return
                                        
                    if id_exclui_clientes < 0:
                        print("Os ids comecam a partir de 1")
                    elif id_exclui_clientes < 3:
                        print("Os ids 1 e 2 nao podem ser excluidos")
                    else:
                        exclui_cliente = classe_funcionarios.Clientes_Restaurante(None, None, None)
                        exclui_cliente.excluir_clientes(id_exclui_clientes)
                    
                case 6:
                    print(Fore.RED + "O programa esta encerrando..." + Style.RESET_ALL)
                    
                    import time as t
                    t.sleep(2)

                    break
                
                case _:
                    print(Fore.RED + "\nEsta opcao nao esta no menu" + Style.RESET_ALL)

        except:
            print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)

if __name__ == '__main__':
    funcoes_cadastro_clientes()