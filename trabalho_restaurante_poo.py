import pprint as pp


class funcionarios_restaurante:
    def __init__(self, nome, idade, cpf, celular, rg, cargo):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__celular = celular
        self.__rg = rg
        self.__cargo = cargo

        self.lista = []

        self.funcionarios = {
            "Gerente": {
                "id": 1,
                "nome": "Robson",
                "idade": 54,
                "CPF": "123.456.789-10",
                "celular": "5468-5612",
                "RG": "456.456-89",
                "cargo": "Gerente"
            },
            "Garcom": {

            },
            "Cozinheiro": {
                
            },
            "Recepcionista": {
                
            }
        }

        
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome



    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    


    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf



    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo_celular):
        self.__celular = novo_celular



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



    def mostra_funcionarios(self):
        pp.pp(self.funcionarios)

    def cadastra_funcionarios(self):
        if self.cargo == "cozinheiro":
            novo_id = len(self.funcionarios) + 1
            adiciona_funcionario = {f"id": novo_id, "nome": self.nome, "idade": self.idade, "CPF": self.cpf, "celular": self.celular, "RG": self.rg, "cargo": self.cargo}

            self.funcionarios["Cozinheiro"] = adiciona_funcionario

            print(self.funcionarios)

            # o metodo de cadastrar funcionarios esta funcionando em partes, os atributos estao sendo adicionados no dicionario, mas toda vez que instancia a classe, o dicionario é resetado


            
    def excluir_funcionario(self):
        pass

    
class clientes_restaurantes:
    def __init__(self, nome_cliente, telefone_cliente):
        self.__nome_cliente = nome_cliente
        self.__telefone_cliente = telefone_cliente
        
    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente):
        self.__nome_cliente = novo_nome_cliente

    
    @property
    def telefone_cliente(self):
        return self.__telefone_cliente

    @telefone_cliente.setter
    def telefone_cliente(self, novo_telefone_cliente):
        self.__telefone_cliente = novo_telefone_cliente



        self.cadastro = {
            
        }

class ingredientes:
    def __init__(self):
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

        
        self.estoque = {
            "basico": {
                self.macarrao: self.macarrao_qtde,
                self.arroz: self.arroz_qtde,
                self.feijao: self.feijao_qtde,
                self.batata: self.batata_qtde
            },
            "salada": {
                self.cenoura: self.cenoura_qtde,
                self.repolho: self.repolho_qtde,
                self.pepino: self.pepino_qtde,
                self.tomate: self.tomate_qtde,
                self.beterraba: self.beterraba_qtde
            },
            "carne": {
                self.porco: self.porco_qtde,
                self.frango: self.frango_qtde,
                self.carne: self.carne_qtde
            }

        }

    def mostra_estoque(self):
        pp.pp(self.estoque)



class pratos(ingredientes):
    def __init__(self):
        
        self.pratos = {
            "Da casa": [self.arroz, self.macarrao, self.feijao, self.frango],
        }


class fornecedor(ingredientes):
    def __init__(self):
        super().__init__()

    def repoe_estoque(self):
        print()


class pedidos:
    def __init__(self):
        pass

    def fazer_pedido(self):
        pedido_escolha = int(input("Digite 1 para pedir prato pronto, ou digite 2 para montar seu prato: "))
        match(pedido_escolha):
            case 1:
                prato_escolha = input("qual prato deseja comer? ")
            case 2:
                alimentos_escolha = input('o que deseja comer: ')
    def devolver_pedido(self):
        print()


while True:
    print("\n=====INICIO=====")
    print("\nVoce é cliente, fornecedor, ou gerente?")

    try:
        escolha = input('digite 1 para cliente, 2 para fornecedor, e 3 para gerente. Digite "sair" para sair do menu: ')
    except ValueError:
        print("precisa informar um numero no menu!!!!!!")

    if escolha.lower() == "sair":
        print("\nO programa esta encerrando...")
        import time as t
        t.sleep(2)
        break
    else:
        match(escolha):
            case "1":
                print("Bem vindo! Qual ação deseja realizar?")


            case "2":
                print("Bem vindo!")
                abastecer = input("Quais itens serao reabastecidos?")

                
            case "3":
                print("\nBem vindo! Qual acao deseja realizar?")
                try:
                    gerente_escolha = int(input("escolha 1 para cadastrar funcionario, 2 para ver os funcionarios e 3 para excluir funcionario: "))
                except:
                    print("AS OPCOES PRECISAM SER NUMEROS!!!")

                match(gerente_escolha):
                    case 1:
                        print("\nPreencha as informações para cadastrar um funcionario: ")
                        nome = input("informe o nome do funcionario: ")
                        idade = int(input("informe a idade: "))
                        cpf = input("informe o CPF: ")
                        celular = input("informe o celular: ")
                        rg = input("informe o RG: ")
                        cargo = input("informe o cargo: ")
                        
                        cadastra_funcionarios= funcionarios_restaurante(nome, idade, cpf, celular, rg, cargo)
                        cadastra_funcionarios.cadastra_funcionarios()
                    
                    case 2:
                        mostra_funcionarios = funcionarios_restaurante(nome=None, idade=None, cpf=None, celular=None, rg=None, cargo=None)
                        mostra_funcionarios.mostra_funcionarios()
                    case 3:
                        pass
