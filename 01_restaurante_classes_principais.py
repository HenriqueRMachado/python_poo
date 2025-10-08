# Importa a biblioteca datetime para lidar com datas e horários
import datetime as dt
# Obtém a data de hoje
data = dt.date.today()
# Obtém o dia da semana (0 = Segunda-feira, 6 = Domingo)
dia_semana = data.weekday()

# Importa módulos para colorir o texto no terminal, melhorando a interface
from colorama import init, Fore, Back, Style
# Inicializa o colorama
init()

# --- Classe Funcionarios_Restaurante: Gerencia o cadastro de funcionários ---
class Funcionarios_Restaurante:
    # Atributo de CLASSE: Dicionário para armazenar todos os funcionários cadastrados.
    # É compartilhado por todas as instâncias (objetos) da classe.
    funcionarios = {
        "id1": {
            "nome": "Alexandre",
            "idade": 45,
            "CPF": "98765432100",
            "celular": "9876-5432",
            "RG": "1122233345",
            "cargo": "Dono"
        },
        "id2": {
            "nome": "Roberto",
            "idade": 55,
            "CPF": "12345678910",
            "celular": "1234-5678",
            "RG": "12.345.678-9",
            "cargo": "Gerente"
        }
    }
    
    # Método Construtor (__init__): É chamado ao criar um novo objeto (instância) da classe.
    # Define os atributos iniciais (características) do funcionário.
    def __init__(self, nome, idade, cpf, celular, rg, cargo):
        # Atributos PRIVADOS (Encapsulamento): O uso de '__' (duplo underscore)
        # indica que esses atributos devem ser acessados/modificados
        # apenas através dos métodos específicos (getters/setters - @property).
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__celular = celular
        self.__rg = rg
        self.__cargo = cargo

    
    # Getter (@property): Permite acessar o atributo privado '__nome' como se fosse público.
    # Exemplo de uso: funcionario.nome
    @property
    def nome(self):
        return self.__nome

    # Setter (@nome.setter): Permite definir (modificar) o atributo privado '__nome'.
    # Aqui, é implementada uma VALIDAÇÃO antes da atribuição.
    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome: # Verifica se o nome não está vazio
            # Levanta uma exceção (erro) se a validação falhar.
            raise ValueError (Fore.RED + "Nome nao pode ser vazio" + Style.RESET_ALL)
        self.__nome = novo_nome # Atribui o novo valor se a validação passar


    # Repetição do padrão de Encapsulamento (Getter/Setter) para 'idade'
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        # Validação mais complexa para a idade (não negativa e maior que 14)
        if nova_idade < 0:
            raise ValueError(Fore.RED + "idade nao pode ser negativa" + Style.RESET_ALL)
        elif nova_idade < 14:
            raise ValueError(Fore.RED + "O estabelecimento nao contrata menores de 14 anos" + Style.RESET_ALL)
        else:
            self.__idade = nova_idade

    
    # Encapsulamento para 'cpf' com validação de não vazio
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if not novo_cpf:
            raise ValueError(Fore.RED + "CPF nao pode ser vazio" + Style.RESET_ALL)
        self.__cpf = novo_cpf


    # Getters e Setters para 'celular', 'rg' e 'cargo' (sem validações restritivas)
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo_celular):
        self.__celular = novo_celular

    # Comentário importante para a apresentação sobre a escolha de validação:
    # os atributos rg e celular nao sao considerados obrigatorios, por isso no setter nao tem nenhuma validacao que interrompa o cadastro.
    
    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, novo_rg):
        self.__rg = novo_rg


    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    # Método para exibir todos os funcionários cadastrados (acessa o atributo de CLASSE 'funcionarios')
    def mostrar_todos_funcionarios(self):
        for chave, valor in Funcionarios_Restaurante.funcionarios.items():
            print(f"{chave}: {valor}")
            print()

    # Método para exibir um funcionário específico, usando tratamento de exceção (try/except)
    def mostrar_funcionario(self, id):
        try:
            # Tenta acessar o funcionário pelo ID (exemplo de manipulação de dicionário)
            print(f"mostrando funcionario: {Funcionarios_Restaurante.funcionarios[f'id{id}']}")
        except:
            # Caso o ID não exista no dicionário, a exceção é capturada e uma mensagem de erro é exibida.
            print(Fore.RED + "esse id nao esta relacionado a nenhum funcionario cadastrado no sistema." + Style.RESET_ALL)

    # Método para adicionar um NOVO funcionário ao dicionário da classe.
    def cadastra_funcionarios(self):
        lista = ["cozinheiro", "cozinheira", "garcom", "garçom", "garconete", "garçonete", "recepcionista"]
        # Verifica se o cargo do objeto (self.cargo) está na lista permitida
        if self.cargo in lista:
            
            # Gera um novo ID baseado no tamanho atual do dicionário, garantindo IDs únicos (simples).
            novo_id = len(Funcionarios_Restaurante.funcionarios) + 1
            # Adiciona um novo item ao dicionário de classe 'funcionarios', usando os atributos do objeto atual (self)
            Funcionarios_Restaurante.funcionarios[f"id{novo_id}"] = {
                # Acessa os atributos usando os Getters (properties)
                "nome": self.nome,
                "idade": self.idade,
                "CPF": self.cpf,
                "celular": self.celular,
                "RG": self.rg,
                "cargo": self.cargo
            }
        else:
            print(Fore.RED + "o cargo nao esta na lista de cargos" + Style.RESET_ALL)

    # Método para ALTERAR os dados de um funcionário existente.
    def alterar_funcionario(self, id):
        try:
            # Tenta verificar se o ID existe
            if f"id{id}" in Funcionarios_Restaurante.funcionarios:
                
                lista = ["cozinheiro", "cozinheira", "garcom", "garçom", "garconete", "garçonete", "recepcionista"]
                # Validação do cargo
                if self.cargo in lista:
                    # Atualiza os dados do funcionário existente com os atributos do objeto atual (self)
                    Funcionarios_Restaurante.funcionarios[f"id{id}"] = {
                        "nome": self.nome,
                        "idade": self.idade,
                        "CPF": self.cpf,
                        "celular": self.celular,
                        "RG": self.rg,
                        "cargo": self.cargo
                    }
                
            else:
                print(Fore.RED + "esse id nao esta relacionado a nenhum funcionario cadastrado no sistema." + Style.RESET_ALL)
        except:
            print(Fore.RED + "esse id nao esta relacionado a nenhum funcionario cadastrado no sistema." + Style.RESET_ALL)

    # Método para EXCLUIR um funcionário
    def excluir_funcionario(self, id):
        try:
            
            # Exibe os dados do funcionário antes de pedir a confirmação
            funcionario = Funcionarios_Restaurante.funcionarios[f"id{id}"]
            print(Fore.RED + f"tem certeza que deseja excluir este funcionario?: {Style.RESET_ALL} {funcionario}")
            
            escolha_excluir = int(input("\nInforme 1 para confirmar a exclusao, e 2 para cancelar: "))
            # Estrutura 'match/case' (disponível a partir do Python 3.10) para seleção de opções.
            match(escolha_excluir):
                case 1:
                    # 'del' remove a entrada do dicionário
                    del Funcionarios_Restaurante.funcionarios[f"id{id}"]
                    print("Funcionario excluído com sucesso.")
                case 2:
                    print("a acao foi cancelada, nenhum funcionario excluido")
                case _:
                    print(Fore.RED + "Esta opcao nao esta disponivel na lista de acoes" + Style.RESET_ALL)
        except:
            print(Fore.RED + "\nO id nao esta vinculado a nenhum cadastro de funcionarios no sistema." + Style.RESET_ALL)



# --- Classe Clientes_Restaurante: Similar à Funcionarios_Restaurante, mas para clientes ---
class Clientes_Restaurante:
    # Atributo de CLASSE para armazenar clientes
    cadastro_clientes = {
        "id1": {
            "nome": "Julia",
            "CPF": "45612389077",
            "Celular": "1122-3344"
        },
        "id2": {
            "nome": "Yudi",
            "CPF": "2223334455",
            "Celular": "4002-8922"
        }
    }
    
    # Construtor do Cliente com atributos privados
    def __init__(self, nome_cliente, cpf_cliente, celular_cliente):
        self.__nome_cliente = nome_cliente
        self.__cpf_cliente = cpf_cliente
        self.__celular_cliente = celular_cliente


    # Getters e Setters para 'nome_cliente' com validação
    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente):
        if not novo_nome_cliente:
            raise ValueError(Fore.RED + "nome nao pode ser vazio" + Style.RESET_ALL)
        else:
            self.__nome_cliente = novo_nome_cliente

    
    # Getters e Setters para 'cpf_cliente' com validação
    @property
    def cpf_cliente(self):
        return self.__cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, novo_cpf_cliente):
        if not novo_cpf_cliente:
            raise ValueError(Fore.RED + "CPF nao pode ser vazio" + Style.RESET_ALL)
        else:
            self.__cpf_cliente = novo_cpf_cliente
    
    
    # Getters e Setters para 'celular_cliente'
    @property
    def celular_cliente(self):
        return self.__celular_cliente

    @celular_cliente.setter
    def celular_cliente(self, novo_celular_cliente):
        self.__celular_cliente = novo_celular_cliente


    # Métodos de exibição, cadastro, alteração e exclusão de clientes
    def mostrar_todos_clientes(self):
            for chave, valor in Clientes_Restaurante.cadastro_clientes.items():
                print(f"{chave}: {valor}")
                print()

    def mostrar_cliente(self, id):
        try:
            print(f"mostrando o cliente do id {id}")
            print(f"{Clientes_Restaurante.cadastro_clientes[f"id{id}"]}")
        except:
            print(Fore.RED + "esse id nao esta relacionado a nenhum cliente cadastrado no sistema." + Style.RESET_ALL)

    def cadastrar_clientes(self):
        novo_id_cliente = len(Clientes_Restaurante.cadastro_clientes) + 1
        Clientes_Restaurante.cadastro_clientes[f"id{novo_id_cliente}"] = {
            "nome": self.nome_cliente,
            "CPF": self.cpf_cliente,
            "Celular": self.celular_cliente
        }
        
    def alterar_clientes(self, id):
        try:
            Clientes_Restaurante.cadastro_clientes[f"id{id}"] = {
                "nome": self.nome_cliente,
                "CPF": self.cpf_cliente,
                "celular": self.celular_cliente,
            }
            
        except:
            print(Fore.RED + "Esse id nao esta relacionado a nenhum cliente cadastrado no sistema." + Style.RESET_ALL)   

    def excluir_clientes(self, id):
        try:
            cliente = Clientes_Restaurante.cadastro_clientes[f"id{id}"]
            print(Fore.RED + f"tem certeza que deseja excluir este cliente?: {Style.RESET_ALL} {cliente}")
            escolha_excluir = int(input("\nInforme 1 para confirmar a exclusao, e 2 para cancelar: "))
            match(escolha_excluir):
                case 1:
                    del Clientes_Restaurante.cadastro_clientes[f"id{id}"]
                    print("Cliente excluído com sucesso.")
                case 2:
                    print("a acao foi cancelada, nenhum cliente excluido")
                case _:
                    print(Fore.RED + "Esta opcao nao esta disponivel na lista de acoes" + Style.RESET_ALL)
        except:
            print(Fore.RED + "\nO id nao esta vinculado a nenhum cadastro de clientes no sistema." + Style.RESET_ALL)
    
# --- Classe Ingredientes: Base para o estoque e itens do cardápio ---
class Ingredientes:
    # Construtor: Inicializa muitos atributos para as quantidades e nomes dos ingredientes.
    # Muitos argumentos com valor 'None' para permitir flexibilidade (embora redefinidos logo abaixo).
    def __init__(self, macarrao_qtde=None, arroz_qtde=None, feijao_qtde=None, batata_qtde=None, farinha_trigo_qtde=None, ovo_qtde=None, leite_qtde=None, manteiga_qtde=None, cenoura_qtde=None, repolho_qtde=None, pepino_qtde=None, tomate_qtde=None, beterraba_qtde=None, brocolis_qtde=None, abobrinha_qtde=None, porco_qtde=None, frango_qtde=None, carne_qtde=None, salmao_qtde=None, presunto_qtde=None, massa_lasanha_qtde=None, queijo_mussarela_qtde=None, queijo_parmesao_qtde=None, molho_tomate_qtde=None, creme_leite_qtde=None, batata_palha_qtde=None, cogumelo_qtde=None, agua_qtde=None, agua_com_gas_qtde=None, coca_cola_qtde=None, fanta_laranja_qtde=None, fanta_uva_qtde=None, guarana_qtde=None):

        # Inicializa atributos para nomes dos ingredientes
        # Define os nomes (strings) que serão usados como chaves no dicionário 'estoque'
        self.macarrao = "macarrao"
        self.arroz = "arroz"
        # ... (continua para todos os nomes)

        # Inicializa atributos para as quantidades (valores padrão do estoque)
        # Reatribui valores fixos, sobrescrevendo os parâmetros opcionais do __init__
        self.macarrao_qtde = 10
        self.arroz_qtde = 5
        self.feijao_qtde = 7
        # ... (continua para todas as quantidades)
        self.agua_qtde = 100 # Exemplo de bebida

        # Atributo de INSTÂNCIA: Dicionário 'estoque'
        # Estrutura aninhada que organiza os ingredientes por categorias, mapeando nome para quantidade.
        self.estoque = {
            "basico": {
                self.macarrao: self.macarrao_qtde,
                self.arroz: self.arroz_qtde,
                # ...
            },
            "salada": {
                self.cenoura: self.cenoura_qtde,
                # ...
            },
            # ... (continua para outras categorias)
            "bebidas": {
                self.agua: self.agua_qtde,
                self.agua_com_gas: self.agua_com_gas_qtde,
                # ...
            }
        }


# --- Classe Fornecedor (Herança e Singleton Simplificado) ---
# HERANÇA: Fornecedor herda de Ingredientes, ganhando todos os seus atributos e métodos.
class Fornecedor(Ingredientes):
    # Atributo de CLASSE: Usado para implementar um padrão de Singleton Simplificado.
    # Garante que todas as instâncias de Fornecedor compartilhem o MESMO dicionário de estoque.
    _estoque_compartilhado = None

    def __init__(self):
        # Se o estoque compartilhado ainda não existe (primeira instância), cria-o.
        if Fornecedor._estoque_compartilhado is None:
            super().__init__() # Chama o construtor da classe pai (Ingredientes) para criar o estoque inicial
            # Atribui o estoque recém-criado (self.estoque) ao atributo de CLASSE compartilhado
            Fornecedor._estoque_compartilhado = self.estoque
        else:
            # Caso já exista, reaproveita o mesmo estoque compartilhado.
            self.estoque = Fornecedor._estoque_compartilhado # A instância usa o estoque compartilhado.

    # Método para alterar a quantidade de um ingrediente no estoque.
    def atualiza_estoque(self, ingrediente, quantidade):
        # Itera sobre categorias e produtos para encontrar o ingrediente
        for categoria, produtos in self.estoque.items():
            if ingrediente in produtos:
                produtos[ingrediente] = quantidade # Altera a quantidade
                print(f"{ingrediente} atualizado para {quantidade} na categoria '{categoria}'.")
                return
        print(f"Produto '{ingrediente}' não encontrado.")

    # Método para exibir o estoque (acessa o estoque compartilhado)
    def mostra_estoque(self):
        print("\nEstoque Atual:")
        for categoria, produtos in self.estoque.items():
            print(f"\nCategoria: {categoria}")
            for item, qtde in produtos.items():
                print(f" {item}: {qtde}")


# --- Classe Pratos (Herança) ---
# HERANÇA: Pratos herda de Ingredientes, tendo acesso aos nomes dos ingredientes.
class Pratos(Ingredientes): # heranca 2
    def __init__(self):
        super().__init__() # Chama o construtor da classe pai (Ingredientes)
        
        # Atributo de INSTÂNCIA: Dicionário para o cardápio de pratos.
        self.pratos_prontos = {
            1: {
                # Uso de TUPLAS para ingredientes: Implica que os ingredientes dos pratos tradicionais são IMUTÁVEIS (não podem ser alterados).
                "Da casa": (self.arroz, self.macarrao, self.feijao, self.frango), 
                "preco": 21.99
            },
            # ...
            4: {
                # O prato do dia é uma LISTA de dicionários, permitindo que o prato mude diariamente.
                "do dia": [
                    {"nome": "Strogonoff de Frango", "preco": 25.0},
                    # ...
                    {"nome": "Omelete de Queijo e Presunto", "preco": 18.0}
                ]
            }
        }

        # Atributo de INSTÂNCIA: Dicionário para o cardápio de bebidas.
        self.bebidas = {
            # ... (dados das bebidas)
        }


# --- Classe Pedidos (Herança) ---
# HERANÇA: Pedidos herda de Pratos, tendo acesso a Ingredientes e Pratos/Bebidas.
class Pedidos(Pratos):
    def __init__(self):
        super().__init__() # Chama o construtor da classe pai (Pratos)

    # Método simples para finalizar a compra
    def pagar_conta(self, preco):
        print(f"\nO preco da conta que devera ser pago é: {preco}")

    # Método para exibir o cardápio
    def mostrar_cardapio(self):
        print(Fore.GREEN + "\n=====PRATOS=====" + Style.RESET_ALL)
        # Exibe o prato do dia dinamicamente, usando o índice 'dia_semana' obtido no início do código.
        # Isso demonstra como a data/hora pode influenciar a lógica do programa.
        print(f"4: {self.pratos_prontos[4]["do dia"][dia_semana]["nome"]}")
        # ... (exibe outras opções)

    # Método principal para registrar um pedido
    def fazer_pedido(self):
        cliente_pedido_prato = int(input("escolha o prato que deseja comer: "))

        if cliente_pedido_prato > 4:
            print("nao tem nenhuma opcao no cardapio com esse numero")
            return
        else:
            cliente_pedido_bebida = int(input("escolha a bebida que deseja beber: "))

            if cliente_pedido_bebida > 6:
                print("nao tem nenhuma opcao no cardapio com esse numero")
                return
            else:
                # Lógica condicional para tratar o 'Prato do Dia' (opção 4) de forma diferente
                if cliente_pedido_prato == 4:
                    print(f"sera trago seu pedido {self.pratos_prontos[4]["do dia"][dia_semana]} junto com a bebida {self.bebidas[cliente_pedido_bebida]}") 

                    # Calcula e paga a conta
                    conta_prato = self.pratos_prontos[4]["do dia"][dia_semana]["preco"]
                    conta_bebida = self.bebidas[cliente_pedido_bebida]["preco"]
                    self.pagar_conta(conta_prato + conta_bebida) # Chamada ao método pagar_conta (composição)
                    
                else:
                    print(f"sera trago seu pedido {self.pratos_prontos[cliente_pedido_prato]} junto com a bebida {self.bebidas[cliente_pedido_bebida]}")

                    # Calcula e paga a conta para pratos fixos
                    conta_prato = self.pratos_prontos[cliente_pedido_prato]["preco"]
                    conta_bebida = self.bebidas[cliente_pedido_bebida]["preco"]
                    self.pagar_conta(conta_prato + conta_bebida)
