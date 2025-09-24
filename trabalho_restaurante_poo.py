
class funcionarios_restaurante:
    def __init__(self):
        pass

class clientes_restaurantes:
    def __init__(self):
        pass

class fornecedor_restaurante:
    def __init__(self):
        pass






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


class pratos(ingredientes):
    def __init__(self):
        super().__init__()



    def mostra(self):
        print(self.macarrao)




class pedidos:
    def __init__(self):
        pass

    def fazer_pedido(self):
        print()

    def devolver_pedido(self):
        print()

    def chamar_garcom(self):
        print(ingredientes.macarrao)

    def conhecer_pedido():
        print()


um = pratos()
um.mostra()

dois = pedidos()
dois.chamar_garcom()
