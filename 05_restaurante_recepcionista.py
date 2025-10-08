# Importa a biblioteca 'importlib' para permitir a importação de módulos com nomes não convencionais.
import importlib 
# Importa as classes principais, incluindo Clientes_Restaurante, do arquivo '01_restaurante_classes_principais'.
classe_funcionarios = importlib.import_module("01_restaurante_classes_principais")

from colorama import init, Fore, Back, Style
init()


# Definição da função que contém o sistema de clientes.
# Esta estrutura (função isolada) permite que o módulo seja importado e chamado facilmente pelo Gerente (modularização/delegação).
def funcoes_cadastro_clientes():

    print(Fore.GREEN + "Bem vindo(a) ao sistema de cadastro de clientes do restaurante!" + Style.RESET_ALL)

    # Loop principal que mantém o menu de clientes em execução
    while True:
        print(Fore.GREEN + "\n============== MENU =============" + Style.RESET_ALL)

        print("1 - Cadastrar cliente")
        print("2 - Listar todos os clientes")
        print("3 - Buscar cliente por id")
        print("4 - Alterar dados de cliente")
        print("5 - Excluir cadastro de cliente")
        print(Fore.RED + "6 - Sair do menu"  + Style.RESET_ALL)

        
        try: # Início do bloco de tratamento de erros para a entrada principal do menu
            recepcionista_escolha = int(input("\nSelecione qual das acoes ira realizar no sistema: "))

            match(recepcionista_escolha):
                case 1: # CADASTRAR CLIENTE (CREATE)
                    
                    try: # Bloco interno para capturar 'ValueError's dos setters
                        print("\nPreencha as informações para cadastrar um cliente: ")
                        # Coleta dos dados do cliente
                        nome = input("\nInforme o nome do cliente: ")
                        cpf = input("Informe o CPF do cliente: ")
                        celular = input("Informe o telefone do cliente: ")
                        
                        # INSTANCIAÇÃO: Cria um novo objeto da classe 'Clientes_Restaurante'
                        cadastra_cliente = classe_funcionarios.Clientes_Restaurante(nome, cpf, celular)
                        
                        # Atribuição por SETTERs: Chama as properties @setter. 
                        # Isso garante que as VALIDAÇÕES (como campos não vazios) definidas na classe sejam executadas (Encapsulamento).
                        cadastra_cliente.nome_cliente = nome
                        cadastra_cliente.cpf_cliente = cpf
                        cadastra_cliente.celular_cliente = celular
                        
                        # Chama o método que salva o novo cliente no dicionário de CLASSE 'cadastro_clientes'.
                        cadastra_cliente.cadastrar_clientes()
                    except ValueError as error:
                        # Exibe mensagens de erro capturadas dos setters (ex: CPF não pode ser vazio)
                        print(error)
                    
                case 2: # LISTAR TODOS OS CLIENTES (READ - All)
                    # Instância temporária: Cria um objeto para acessar o método que lista todos os clientes (dicionário de CLASSE).
                    mostra_clientes = classe_funcionarios.Clientes_Restaurante(nome_cliente=None, cpf_cliente=None, celular_cliente=None)
                    mostra_clientes.mostrar_todos_clientes()
                    
                case 3: # BUSCAR CLIENTE POR ID (READ - Specific)
                    print(Fore.RED + "\nAtencao, para consultar um cliente especifico, e necessario o id. Para saber o id, execute a acao 2 e consulte os clientes cadastrados!" + Style.RESET_ALL)

                    id_clientes_consulta = int(input("Informe o id do cliente que deseja consultar no sistema:"))
                    
                    # Lógica de validação simples do ID (não pode ser <= 0 ou vazio)
                    if id_clientes_consulta <= 0:
                            print("Os ids comecam a partir de 1")
                    elif not id_clientes_consulta:
                            print("id nao pode ser vazio")
                            return # Encerra a execução desta iteração da função
                    else:
                        # Instância temporária para chamar o método de busca.
                        consulta_cliente = classe_funcionarios.Clientes_Restaurante(None, None, None)
                        consulta_cliente.mostrar_cliente(id_clientes_consulta)
                    
                case 4: # ALTERAR DADOS DE CLIENTE (UPDATE)
                    try:
                        print(Fore.RED + "\nAtencao, para alterar o cadastro de um cliente, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
                    
                        id_cliente_alterar = int(input("\nInforme o id do funcionario que deseja alterar no sistema: "))
                        
                        
                        if id_cliente_alterar <= 0:
                            print("Os ids comecam a partir de 1")
                        elif not id_cliente_alterar:
                            print("id nao pode ser vazio")
                            return
                        # OBSERVAÇÃO: A restrição "elif id_cliente_alterar < 3:" provavelmente é uma cópia do módulo de Funcionários e deve ser revisada para Clientes se os IDs 1 e 2 de clientes puderem ser alterados.
                        elif id_cliente_alterar < 3:
                            print("Os ids 1 e 2 nao podem ser alterados")
                        else:
                        
                            # Exibe o cliente atual antes da alteração (acessando o dicionário de CLASSE)
                            print(f"Alterando o cliente {classe_funcionarios.Clientes_Restaurante.cadastro_clientes[f"id{id_cliente_alterar}"]}")
                            
                            print("\nInforme as novas informações que deseja alterar: ")
                            # Coleta dos novos dados
                            altera_nome_cliente = input("Informe o novo nome: ")
                            altera_cpf_cliente = input("Informe o novo CPF: ")
                            altera_celular_cliente = input("Informe o novo celular: ")
                            
                            # INSTANCIAÇÃO com NOVOS dados.
                            altera_cliente = classe_funcionarios.Clientes_Restaurante(altera_nome_cliente, altera_cpf_cliente, altera_celular_cliente)

                            # Uso dos SETTERs para aplicar validações nos novos dados.
                            altera_cliente.nome_cliente = altera_nome_cliente
                            altera_cliente.cpf_cliente = altera_cpf_cliente
                            altera_cliente.celular_cliente = altera_celular_cliente
                            
                            # Chama o método que substitui o cliente no dicionário de CLASSE pelo novo objeto instanciado.
                            altera_cliente.alterar_clientes(id_cliente_alterar)
                    except ValueError as error:
                        print(error) # Captura e exibe erros dos setters
                
                case 5: # EXCLUIR CADASTRO DE CLIENTE (DELETE)
                    id_exclui_clientes = int(input("Informe o id do cliente que deseja excluir: "))

                                    
                    if id_exclui_clientes <= 0:
                        print("Os ids comecam a partir de 1")
                    elif not id_exclui_clientes:
                        print("id nao pode ser vazio")
                        return
                    # OBSERVAÇÃO: Novamente, a restrição para IDs < 3 pode não se aplicar a clientes e foi mantida como lógica do código original.
                    elif id_exclui_clientes < 3:
                        print("Os ids 1 e 2 nao podem ser excluidos")
                    else:
                        # Instância temporária para chamar o método de exclusão.
                        exclui_cliente = classe_funcionarios.Clientes_Restaurante(None, None, None)
                        exclui_cliente.excluir_clientes(id_exclui_clientes)
                    
                case 6:
                    print(Fore.RED + "O programa esta encerrando..." + Style.RESET_ALL)
                    
                    import time as t
                    t.sleep(2)

                    break # Sai do loop do menu e, consequentemente, da função
                
                case _:
                    print(Fore.RED + "\nEsta opcao nao esta no menu" + Style.RESET_ALL)

        except:
            # Captura erros de input não numérico no menu principal
            print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)

# Bloco de execução principal (somente se este arquivo for executado diretamente)
if __name__ == '__main__':
    funcoes_cadastro_clientes()
