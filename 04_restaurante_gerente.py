# Importa a biblioteca 'importlib' para permitir a importação de módulos com nomes não convencionais.
import importlib 

# Importa as classes principais (Funcionarios_Restaurante, etc.) do arquivo '01_restaurante_classes_principais'.
classe_funcionarios = importlib.import_module("01_restaurante_classes_principais")
# Importa um módulo secundário (recepcionista_funcao), demonstrando DELEGAÇÃO DE RESPONSABILIDADE
# O gerenciamento de clientes foi movido para uma função ou módulo separado (boas práticas de POO/modularização).
recepcionista_funcao = importlib.import_module("05_restaurante_recepcionista")


from colorama import init, Fore, Back, Style
init()

print(Fore.GREEN + "Bem vindo ao gerenciamento do restaurante!" + Style.RESET_ALL)

# Definição da função principal 'funcoes_gerente' para organizar o código (manter o escopo local e reutilização).
def funcoes_gerente(): 

    # Loop principal do Menu do Gerente (Nível 1)
    while True:
        try:
            # Seleção inicial: Clientes (delegado) ou Funcionários (neste módulo)
            gerente_escolha_cliente = int(input("\nDigite 1 para realizar alterações no cadastro de clientes.\nDigite 2 para realizar alterações no cadastro de funcionarios. \nDigite 3 para sair: "))

            match(gerente_escolha_cliente):
                case 1:
                    # Delega a execução da função de clientes para o módulo importado 'recepcionista_funcao'
                    recepcionista_funcao.funcoes_cadastro_clientes()
                case 2:
                    # Exibe o Menu de Funcionários (Nível 2)
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
                    break # Sai do loop principal
                case _:
                    print(Fore.RED + "essa opcao nao esta no menu" + Style.RESET_ALL)
                    break # Sai do loop principal após erro (comportamento a ser ajustado se necessário)
                    
        except:
            print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)
            break # Sai do loop principal após erro de input
        
        # Inicia o tratamento das opções do Menu de Funcionários (Nível 2)
        try:
            # Nota: Este input só é executado se a opção 2 (Funcionários) foi escolhida no menu anterior.
            gerente_escolha_funcionarios = int(input("\nEscolha uma das opcoes no menu: "))

            match(gerente_escolha_funcionarios):
                case 1: # CADASTRAR FUNCIONÁRIO (CREATE)
                    try:
                        print("\nPreencha as informações para cadastrar um funcionario: ")
                        # Coleta dos dados
                        nome = input("Informe o nome do funcionario: ")
                        try:
                            idade = int(input("Informe a idade: "))
                        except:
                            print(Fore.RED + "idade nao pode ser vazia ou não numérica" + Style.RESET_ALL)
                            return # Encerra a função após erro
                            
                        cpf = input("Informe o CPF: ")
                        celular = input("Informe o celular: ")
                        rg = input("Informe o RG: ")
                        cargo = input("Informe o cargo: ").lower()
                        
                        # INSTANCIAÇÃO: Cria um novo objeto 'Funcionarios_Restaurante' com os dados iniciais.
                        cadastra_funcionarios = classe_funcionarios.Funcionarios_Restaurante(nome, idade, cpf, celular, rg, cargo)
                        
                        # Atribuição por SETTERs: As linhas a seguir chamam os métodos @setter definidos na classe.
                        # Isso garante que as VALIDAÇÕES (como idade > 14 e campos não vazios) sejam aplicadas.
                        cadastra_funcionarios.nome = nome
                        cadastra_funcionarios.idade = idade
                        cadastra_funcionarios.cpf = cpf
                        cadastra_funcionarios.celular = celular
                        cadastra_funcionarios.rg = rg
                        cadastra_funcionarios.cargo = cargo
                        
                        # Chama o método que adiciona o objeto ao dicionário de CLASSE.
                        cadastra_funcionarios.cadastra_funcionarios()
                    
                    # Trata a exceção 'ValueError' lançada pelos SETTERs (Encapsulamento em ação)
                    except ValueError as error:
                        print(error)
                
                case 2: # LISTAR FUNCIONÁRIOS (READ - All)
                    print("Mostrando os funcionarios cadastrados no sistema: ")
                    
                    # Criação de uma instância temporária: Um objeto é criado apenas para acessar o método de listagem, 
                    # pois o método acessa um atributo de CLASSE (o dicionário 'funcionarios') e não precisa de dados válidos.
                    mostra_funcionarios = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)
                    mostra_funcionarios.mostrar_todos_funcionarios()

                case 3: # BUSCAR FUNCIONÁRIO (READ - Specific)
                    print(Fore.RED + "\nAtencao, para consultar um funcionario especifico, e necessario o id. Para saber o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)

                    id_funcionario_consulta = int(input("\nInforme o id do funcionario que deseja consultar no sistema: "))
                    
                    # Lógica de validação do ID
                    if id_funcionario_consulta <= 0:
                        print("Os ids comecam a partir de 1")
                    # ... (outras validações)
                    # Exemplo de RESTRICÃO DE ACESSO: ids 1 e 2 são os cargos Dono e Gerente e são fixos/protegidos.
                    elif id_funcionario_consulta < 3:
                        print("Os ids 1 e 2 nao podem ser alterados")
                    else:
                    
                        # Instância temporária para chamar o método de busca.
                        consulta_funcionario = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)
                        consulta_funcionario.mostrar_funcionario(id_funcionario_consulta)
                    
                case 4: # ALTERAR DADOS DE FUNCIONÁRIO (UPDATE)
                    try:
                        print(Fore.RED + "\nAtencao, para alterar o cadastro de um funcionario, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
                    
                        id_funcionario_alterar = int(input("\nInforme o id do funcionario que deseja alterar no sistema: "))
                        
                        # Lógica de validação e restrição (ids 1 e 2)
                        if id_funcionario_alterar <= 0:
                            print("Os ids comecam a partir de 1")
                        elif not id_funcionario_alterar:
                            print("id nao pode ser vazio")
                            return
                        elif id_funcionario_alterar < 3:
                            print("Os ids 1 e 2 nao podem ser alterados")
                        else:
                            # Acessa o dicionário de classe para exibir o funcionário antes de alterar
                            print(f"Alterando o funcionario {classe_funcionarios.Funcionarios_Restaurante.funcionarios[f"id{id_funcionario_alterar}"]}")
                            
                            # Coleta dos novos dados
                            # ... (coleta de inputs)
                            
                            # Instanciação com os NOVOS dados: Cria um novo objeto que representa o estado *desejado* para o funcionário.
                            altera_funcionario = classe_funcionarios.Funcionarios_Restaurante(altera_nome_funcionario, altera_idade_funcionario, altera_cpf_funcionario, altera_celular_funcionario, altera_rg_funcionario, altera_cargo_funcionario)

                            # Uso dos SETTERs: As validações são aplicadas aos novos dados.
                            altera_funcionario.nome = altera_nome_funcionario
                            # ... (outros setters)
                            
                            # Chama o método de alteração, passando o ID do funcionário a ser substituído/atualizado.
                            altera_funcionario.alterar_funcionario(id_funcionario_alterar)
                            
                    except ValueError as error:
                        print(error) # Exibe erros de validação (setter)
                    
                case 5: # EXCLUIR CADASTRO DE FUNCIONÁRIO (DELETE)
                    print(Fore.RED + "\nAtencao, para excluir o cadastro de um funcionario, e necessario o id. Para consultar o id, execute a acao 2 e consulte os funcionarios cadastrados!" + Style.RESET_ALL)
                
                    id_funcionario_excluir = int(input("\nInforme o id do funcionario que deseja excluir do sistema: "))
                    
                    # Lógica de validação e restrição
                    if id_funcionario_excluir <= 0:
                        print("Os ids comecam a partir de 1")
                    elif not id_funcionario_excluir:
                        print("id nao pode ser vazio")
                        return
                    elif id_funcionario_excluir < 3:
                        print("Os ids 1 e 2 nao podem ser alterados")
                    else:
                        
                        # Instância temporária para chamar o método de exclusão.
                        exclui_funcionario = classe_funcionarios.Funcionarios_Restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)

                        exclui_funcionario.excluir_funcionario(id_funcionario_excluir)
                        
                case 6:
                    print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)
                    import time as t
                    t.sleep(1.5)
                    break # Sai do loop do Menu de Funcionários (Nível 2)
                
                case _:
                    print(Fore.RED + "\nEsta opcao nao esta no menu" + Style.RESET_ALL)
                    break # Sai do loop do Menu de Funcionários (Nível 2)
        
        except:
            print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)
            break # Sai do loop do Menu de Funcionários (Nível 2)

# Chamada para iniciar a execução do sistema.
funcoes_gerente()
