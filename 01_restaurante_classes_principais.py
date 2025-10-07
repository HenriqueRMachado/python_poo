import datetime as dt
data = dt.date.today()
dia_semana = data.weekday()

from colorama import init, Fore, Back, Style
init()

class Funcionarios_Restaurante:
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
    def __init__(self, nome, idade, cpf, celular, rg, cargo):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__celular = celular
        self.__rg = rg
        self.__cargo = cargo

        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not self.__nome:
            raise ValueError (Fore.RED + "Nome nao pode ser vazio" + Style.RESET_ALL)
        self.__nome = novo_nome



    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError(Fore.RED + "idade nao pode ser negativa" + Style.RESET_ALL)
        elif nova_idade < 14:
            raise ValueError(Fore.RED + "O estabelecimento nao contrata menores de 14 anos" + Style.RESET_ALL)
        else:
            self.__idade = nova_idade

    


    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if not novo_cpf:
            raise ValueError(Fore.RED + "CPF nao pode ser vazio" + Style.RESET_ALL)
        self.__cpf = novo_cpf



    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo_celular):
        self.__celular = novo_celular


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



    def mostrar_todos_funcionarios(self):
        for chave, valor in Funcionarios_Restaurante.funcionarios.items():
            print(f"{chave}: {valor}")
            print()

    def mostrar_funcionario(self, id):
        try:
            print(f"mostrando funcionario: {Funcionarios_Restaurante.funcionarios[f'id{id}']}")
        except:
            print(Fore.RED + "esse id nao esta relacionado a nenhum funcionario cadastrado no sistema." + Style.RESET_ALL)

    def cadastra_funcionarios(self):
        lista = ["cozinheiro", "cozinheira", "garcom", "garçom", "garconete", "garçonete", "recepcionista"]
        if self.cargo in lista:
            
            novo_id = len(Funcionarios_Restaurante.funcionarios) + 1
            Funcionarios_Restaurante.funcionarios[f"id{novo_id}"] = {
                "nome": self.nome,
                "idade": self.idade,
                "CPF": self.cpf,
                "celular": self.celular,
                "RG": self.rg,
                "cargo": self.cargo
            }
        else:
            print(Fore.RED + "o cargo nao esta na lista de cargos" + Style.RESET_ALL)

    def alterar_funcionario(self, id):
        try:
            
            if f"id{id}" in Funcionarios_Restaurante.funcionarios:
                
                lista = ["cozinheiro", "cozinheira", "garcom", "garçom", "garconete", "garçonete", "recepcionista"]
                if self.cargo in lista:
                    
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

    def excluir_funcionario(self, id):
        try:
            
            
            funcionario = Funcionarios_Restaurante.funcionarios[f"id{id}"]
            print(Fore.RED + f"tem certeza que deseja excluir este funcionario?: {Style.RESET_ALL} {funcionario}")
            
            escolha_excluir = int(input("\nInforme 1 para confirmar a exclusao, e 2 para cancelar: "))
            match(escolha_excluir):
                case 1:
                    del Funcionarios_Restaurante.funcionarios[f"id{id}"]
                    print("Funcionario excluído com sucesso.")
                case 2:
                    print("a acao foi cancelada, nenhum funcionario excluido")
                case _:
                    print(Fore.RED + "Esta opcao nao esta disponivel na lista de acoes" + Style.RESET_ALL)
        except:
            print(Fore.RED + "\nO id nao esta vinculado a nenhum cadastro de funcionarios no sistema." + Style.RESET_ALL)



        

    
class Clientes_Restaurante:
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
    
    def __init__(self, nome_cliente, cpf_cliente, celular_cliente):
        self.__nome_cliente = nome_cliente
        self.__cpf_cliente = cpf_cliente
        self.__celular_cliente = celular_cliente


    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente):
        if not novo_nome_cliente:
            raise ValueError(Fore.RED + "nome nao pode ser vazio" + Style.RESET_ALL)
        else:
            self.__nome_cliente = novo_nome_cliente

    

    @property
    def cpf_cliente(self):
        return self.__cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, novo_cpf_cliente):
        if not novo_cpf_cliente:
            raise ValueError(Fore.RED + "CPF nao pode ser vazio" + Style.RESET_ALL)
        else:
            self.__cpf_cliente = novo_cpf_cliente
    
    
    @property
    def celular_cliente(self):
        return self.__celular_cliente

    @celular_cliente.setter
    def celular_cliente(self, novo_celular_cliente):
        self.__celular_cliente = novo_celular_cliente



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
    
class Ingredientes:
    def __init__(self, macarrao_qtde=None, arroz_qtde=None, feijao_qtde=None, batata_qtde=None, farinha_trigo_qtde=None, ovo_qtde=None, leite_qtde=None, manteiga_qtde=None, cenoura_qtde=None, repolho_qtde=None, pepino_qtde=None, tomate_qtde=None, beterraba_qtde=None, brocolis_qtde=None, abobrinha_qtde=None, porco_qtde=None, frango_qtde=None, carne_qtde=None, salmao_qtde=None, presunto_qtde=None, massa_lasanha_qtde=None, queijo_mussarela_qtde=None, queijo_parmesao_qtde=None, molho_tomate_qtde=None, creme_leite_qtde=None, batata_palha_qtde=None, cogumelo_qtde=None, agua_qtde=None, agua_com_gas_qtde=None, coca_cola_qtde=None, fanta_laranja_qtde=None, fanta_uva_qtde=None, guarana_qtde=None):

        self.macarrao_qtde = macarrao_qtde
        self.arroz_qtde = arroz_qtde
        self.feijao_qtde = feijao_qtde
        self.batata_qtde = batata_qtde
        self.cenoura_qtde = cenoura_qtde
        self.repolho_qtde = repolho_qtde
        self.pepino_qtde = pepino_qtde
        self.tomate_qtde = tomate_qtde
        self.beterraba_qtde = beterraba_qtde
        self.porco_qtde = porco_qtde
        self.frango_qtde = frango_qtde
        self.carne_qtde = carne_qtde

        self.batata_palha_qtde = batata_palha_qtde
        self.creme_leite_qtde = creme_leite_qtde
        self.molho_tomate_qtde = molho_tomate_qtde
        self.cogumelo_qtde = cogumelo_qtde
        self.queijo_parmesao_qtde = queijo_parmesao_qtde
        self.massa_lasanha_qtde = massa_lasanha_qtde
        self.queijo_mussarela_qtde = queijo_mussarela_qtde
        self.brocolis_qtde = brocolis_qtde
        self.abobrinha_qtde = abobrinha_qtde
        self.farinha_trigo_qtde = farinha_trigo_qtde
        self.ovo_qtde = ovo_qtde
        self.salmao_qtde = salmao_qtde
        self.manteiga_qtde = manteiga_qtde
        self.leite_qtde = leite_qtde
        self.presunto_qtde = presunto_qtde

        self.agua_qtde = 100
        self.agua_com_gas_qtde = 40
        self.coca_cola_qtde = 50
        self.fanta_laranja_qtde = 30
        self.fanta_uva_qtde = 35
        self.guarana_qtde = 20

        self.macarrao = "macarrao"
        self.arroz = "arroz"
        self.feijao = "feijao"
        self.batata = "batata"
        self.cenoura = "cenoura"
        self.repolho = "repolho"
        self.pepino = "pepino"
        self.tomate = "tomate"
        self.beterraba = "beterraba"
        self.porco = "porco"
        self.frango = "frango"
        self.carne = "carne"

        self.batata_palha = "batata palha"
        self.creme_leite = "creme de leite"
        self.molho_tomate = "molho de tomate"
        self.cogumelo = "cogumelo"
        self.queijo_parmesao = "queijo parmesao"
        self.massa_lasanha = "massa de lasanha"
        self.queijo_mussarela = "queijo mussarela"
        self.brocolis = "brocolis"
        self.abobrinha = "abobrinha"
        self.farinha_trigo = "farinha de trigo"
        self.ovo = "ovo"
        self.salmao = "salmao"
        self.manteiga = "manteiga"
        self.leite = "leite"
        self.presunto = "presunto"

        self.agua = "agua"
        self.agua_com_gas = "agua com gas"
        self.coca_cola = "coca-cola"
        self.fanta_laranja = "fanta laranja"
        self.fanta_uva = "fanta uva"
        self.guarana = "guarana"

        self.macarrao_qtde = 10
        self.arroz_qtde = 5
        self.feijao_qtde = 7
        self.batata_qtde = 5
        self.cenoura_qtde = 3
        self.repolho_qtde = 5
        self.pepino_qtde = 2
        self.tomate_qtde = 10
        self.beterraba_qtde = 5
        self.porco_qtde = 10
        self.frango_qtde = 15
        self.carne_qtde = 17

        self.batata_palha_qtde = 8
        self.creme_leite_qtde = 6
        self.molho_tomate_qtde = 12
        self.cogumelo_qtde = 7
        self.queijo_parmesao_qtde = 5
        self.massa_lasanha_qtde = 6
        self.queijo_mussarela_qtde = 10
        self.brocolis_qtde = 4
        self.abobrinha_qtde = 4
        self.farinha_trigo_qtde = 8
        self.ovo_qtde = 20
        self.salmao_qtde = 6
        self.manteiga_qtde = 5
        self.leite_qtde = 8
        self.presunto_qtde = 10

        self.estoque = {
            "basico": {
                self.macarrao: self.macarrao_qtde,
                self.arroz: self.arroz_qtde,
                self.feijao: self.feijao_qtde,
                self.batata: self.batata_qtde,
                self.farinha_trigo: self.farinha_trigo_qtde,
                self.ovo: self.ovo_qtde,
                self.leite: self.leite_qtde,
                self.manteiga: self.manteiga_qtde
            },
            "salada": {
                self.cenoura: self.cenoura_qtde,
                self.repolho: self.repolho_qtde,
                self.pepino: self.pepino_qtde,
                self.tomate: self.tomate_qtde,
                self.beterraba: self.beterraba_qtde,
                self.brocolis: self.brocolis_qtde,
                self.abobrinha: self.abobrinha_qtde
            },
            "carne": {
                self.porco: self.porco_qtde,
                self.frango: self.frango_qtde,
                self.carne: self.carne_qtde,
                self.salmao: self.salmao_qtde,
                self.presunto: self.presunto_qtde
            },
            "massas e queijos": {
                self.massa_lasanha: self.massa_lasanha_qtde,
                self.queijo_mussarela: self.queijo_mussarela_qtde,
                self.queijo_parmesao: self.queijo_parmesao_qtde
            },
            "molhos e extras": {
                self.molho_tomate: self.molho_tomate_qtde,
                self.creme_leite: self.creme_leite_qtde,
                self.batata_palha: self.batata_palha_qtde,
                self.cogumelo: self.cogumelo_qtde
            },
            "bebidas": {
                self.agua: self.agua_qtde,
                self.agua_com_gas: self.agua_com_gas_qtde,
                self.coca_cola: self.coca_cola_qtde,
                self.fanta_laranja: self.fanta_laranja_qtde,
                self.fanta_uva: self.fanta_uva_qtde,
                self.guarana: self.guarana_qtde
            }
        }





class Fornecedor(Ingredientes):
    _estoque_compartilhado = None

    def __init__(self):
        # Se o estoque compartilhado ainda não existe, cria-o
        if Fornecedor._estoque_compartilhado is None:
            super().__init__()
            Fornecedor._estoque_compartilhado = self.estoque
        else:
            # Caso já exista, reaproveita o mesmo estoque
            self.estoque = Fornecedor._estoque_compartilhado

    def atualiza_estoque(self, ingrediente, quantidade):
        for categoria, produtos in self.estoque.items():
            if ingrediente in produtos:
                produtos[ingrediente] = quantidade
                print(f"{ingrediente} atualizado para {quantidade} na categoria '{categoria}'.")
                return
        print(f"Produto '{ingrediente}' não encontrado.")

    def mostra_estoque(self):
        print("\nEstoque Atual:")
        for categoria, produtos in self.estoque.items():
            print(f"\nCategoria: {categoria}")
            for item, qtde in produtos.items():
                print(f" {item}: {qtde}")



class Pratos(Ingredientes): # heranca 2
    def __init__(self):
        super().__init__()
        
        self.pratos_prontos = {
            1: {
                "Da casa": (self.arroz, self.macarrao, self.feijao, self.frango), #os pratos tradicionais sao imutaveis, (tuplas)
                "preco": 21.99
            },
            2: {
                "feijoada": (self.feijao, self.macarrao, self.porco),
                "preco": 40
            },
            3: {
                "macarronada": (self.macarrao, self.tomate),
                "preco": 25
            },
            4: {
                "do dia": [
                    {"nome": "Strogonoff de Frango", "preco": 25.0},
                    {"nome": "Risoto de Cogumelos", "preco": 28.0},
                    {"nome": "Lasanha Bolonhesa", "preco": 30.0},
                    {"nome": "Frango Grelhado com Legumes", "preco": 22.0},
                    {"nome": "Bife à Parmegiana", "preco": 27.0},
                    {"nome": "Salmão Grelhado com Purê de Batata", "preco": 35.0},
                    {"nome": "Omelete de Queijo e Presunto", "preco": 18.0}
                ]


            }
        }

        self.bebidas = {
            1: {
                "bebida": "agua",
                "preco": 3
            },
            2: {
                "bebida": "agua com gas",
                "preco": 3.50
            },
            3: {
                "bebida": "Coca-Cola",
                "preco": 9
            },
            4: {
                "bebida": "Fanta Laranja",
                "preco": 7.50
            },
            5: {
                "bebida": "Fanta Uva",
                "preco": 7.50
            },
            6: {
                "bebida": "Guarana",
                "preco": 8
            }
        }


class Pedidos(Pratos):
    def __init__(self):
        super().__init__()

    def pagar_conta(self, preco):
        print(f"\nO preco da conta que devera ser pago é: {preco}")

    def mostrar_cardapio(self):
        print(Fore.GREEN + "\n=====PRATOS=====" + Style.RESET_ALL)
        print("1: Da casa: arroz, feijao, macarrao, frango")
        print("2: feijoada: feijao, macarrao, porco")
        print("3: macarronada: macarrao, molho de tomate)")
        print(f"4: {self.pratos_prontos[4]["do dia"][dia_semana]["nome"]}")

        print()

        print(Fore.GREEN + "=====BEBIDAS=====" + Style.RESET_ALL)
        print("1: Água")
        print("2: Água com gás")
        print("3: Coca-Cola")
        print("4: Fanta Laranja")
        print("5: Fanta Uva")
        print("6: Guarana")   

        print()

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
                if cliente_pedido_prato == 4:
                    print(f"sera trago seu pedido {self.pratos_prontos[4]["do dia"][dia_semana]} junto com a bebida {self.bebidas[cliente_pedido_bebida]}") 


                    conta_prato = self.pratos_prontos[4]["do dia"][dia_semana]["preco"]
                    conta_bebida = self.bebidas[cliente_pedido_bebida]["preco"]
                    self.pagar_conta(conta_prato + conta_bebida)
                    
                else:
                    print(f"sera trago seu pedido {self.pratos_prontos[cliente_pedido_prato]} junto com a bebida {self.bebidas[cliente_pedido_bebida]}")

                    conta_prato = self.pratos_prontos[cliente_pedido_prato]["preco"]
                    conta_bebida = self.bebidas[cliente_pedido_bebida]["preco"]
                    self.pagar_conta(conta_prato + conta_bebida)
