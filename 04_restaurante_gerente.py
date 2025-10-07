import importlib # biblioteca para importar arquivos em forma de string, usado para arquivos que comecam com numeros.
classe_funcionarios = importlib.import_module("01_restaurante_classes_principais")
recepcionista_funcao = importlib.import_module("05_restaurante_recepcionista")


from colorama import init, Fore, Back, Style
init()

print(Fore.GREEN + "Bem vindo ao gerenciamento do restaurante!" + Style.RESET_ALL)

def funcoes_gerente(): # funcao para manter o escopo local

    while True:
        try:
            gerente_escolha_cliente = int(input("\nDigite 1 para realizar alterações no cadastro de clientes.\nDigite 2 para realizar alterações no cadastro de funcionarios. \nDigite 3 para sair: "))

            match(gerente_escolha_cliente):
                case 1:
                    recepcionista_funcao.funcoes_cadastro_clientes()
                case 2:
                
                    print(Fore.GREEN + "\n=============== MENU ==============" + Style.RESET_ALL)
                    print("1 - Cadastrar funcionario")
                    print("2 - Listar todos os funcionarios")
                    print("3 - Buscar funcionario por id")
                    print("4 - Alterar dados de funcionario")
                    print("5 - Excluir cadastro de funcionario")
                    print(Fore.RED + "6 - Sair do menu"  + Style.RESET_ALL)
                
                case 3:               
                    print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)

                    import time as t
                    t.sleep(1.5)

                    break
                case _:
                    print(Fore.RED + "essa opcao nao esta no menu" + Style.RESET_ALL)
                    
        except:
            print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)
            break

        gerente_escolha_funcionarios = int(input("\nEscolha uma das opcoes no menu: "))

        match(gerente_escolha_funcionarios):
            case 1:
                try:
                    print("\nPreencha as informações para cadastrar um funcionario: ")
                    nome = input("Informe o nome do funcionario: ")
                    try:
                        idade = int(input("Informe a idade: "))
                    except:
                        print("idade nao pode ser vazia")
                        return
                        
                    cpf = input("Informe o CPF: ")
                    celular = input("Informe o celular: ")
                    rg = input("Informe o RG: ")
                    cargo = input("Informe o cargo: ").lower()
                    
                    cadastra_funcionarios = classe_funcionarios.Funcionarios_Restaurante(nome, idade, cpf, celular, rg, cargo)
                    
                    cadastra_funcionarios.nome = nome
                    cadastra_funcionarios.idade = idade
                    cadastra_funcionarios.cpf = cpf
                    cadastra_funcionarios.celular = celular
                    cadastra_funcionarios.rg = rg
                    cadastra_funcionarios.cargo = cargo
                    
                    cadastra_funcionarios.cadastra_funcionarios()
                except ValueError as error:
                    print(error)
            case 2:
                print("Mostrando os funcionarios cadastrados no sistema: ")

                mostra_funcionarios = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)
                mostra_funcionarios.mostrar_todos_funcionarios()

            case 3:
                print(Fore.RED + "\nAtencao, para consultar um funcionario especifico, e necessario o id. Para saber o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)

                id_funcionario_consulta = int(input("\nInforme o id do funcionario que deseja consultar no sistema: "))
                
                if id_funcionario_consulta <= 0:
                    print("Os ids comecam a partir de 1")
                elif not id_funcionario_consulta:
                    print("id nao pode ser vazio")
                    return
                elif id_funcionario_consulta < 3:
                    print("Os ids 1 e 2 nao podem ser alterados")
                else:
                
                    consulta_funcionario = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)
                    consulta_funcionario.mostrar_funcionario(id_funcionario_consulta)
                
            case 4:
                try:
                    print(Fore.RED + "\nAtencao, para alterar o cadastro de um funcionario, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
                
                    id_funcionario_alterar = int(input("\nInforme o id do funcionario que deseja alterar no sistema: "))
                    
                    if id_funcionario_alterar <= 0:
                        print("Os ids comecam a partir de 1")
                    elif not id_funcionario_alterar:
                        print("id nao pode ser vazio")
                        return
                    elif id_funcionario_alterar < 3:
                        print("Os ids 1 e 2 nao podem ser alterados")
                    else:
                        print(f"Alterando o funcionario {classe_funcionarios.Funcionarios_Restaurante.funcionarios[f"id{id_funcionario_alterar}"]}")
                        
                        print("\nInforme as novas informações que deseja alterar: ")
                        altera_nome_funcionario = input("Informe o novo nome: ")
                        try:
                            altera_idade_funcionario = int(input("Informe a nova idade: "))
                        except:
                            print("idade nao pode ser vazia")
                            return
                        
                        altera_cpf_funcionario = input("Informe o novo CPF: ")
                        altera_celular_funcionario = input("Informe o novo celular: ")
                        altera_rg_funcionario = input("Informe o novo RG: ")
                        altera_cargo_funcionario = input("informe o novo cargo: ")
                        
                        altera_funcionario = classe_funcionarios.Funcionarios_Restaurante(altera_nome_funcionario, altera_idade_funcionario, altera_cpf_funcionario, altera_celular_funcionario, altera_rg_funcionario, altera_cargo_funcionario)

                        altera_funcionario.nome = altera_nome_funcionario
                        altera_funcionario.idade = altera_idade_funcionario
                        altera_funcionario.cpf = altera_cpf_funcionario
                        altera_funcionario.celular = altera_celular_funcionario
                        altera_funcionario.rg = altera_rg_funcionario
                        altera_funcionario.cargo = altera_cargo_funcionario
                        
                        altera_funcionario.alterar_funcionario(id_funcionario_alterar)
                        
                except ValueError as error:
                    print(error)
            case 5:
                print(Fore.RED + "\nAtencao, para excluir o cadastro de um funcionario, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
            
                id_funcionario_excluir = int(input("\nInforme o id do funcionario que deseja excluir do sistema: "))
                
                if id_funcionario_excluir <= 0:
                    print("Os ids comecam a partir de 1")
                elif not id_funcionario_excluir:
                    print("id nao pode ser vazio")
                    return
                elif id_funcionario_excluir < 3:
                    print("Os ids 1 e 2 nao podem ser alterados")
                else:
                    
                    exclui_funcionario = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)

                    exclui_funcionario.excluir_funcionario(id_funcionario_excluir)
            case 6:
                
                print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)

                import time as t
                t.sleep(1.5)

                break

            case _:
                print(Fore.RED + "\nEsta opcao nao esta no menu" + Style.RESET_ALL)
                break

funcoes_gerente()
