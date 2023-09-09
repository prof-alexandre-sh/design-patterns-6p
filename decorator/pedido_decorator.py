# Pedido base

class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido

        self.precos_sem_adicionais = {

            "numero42": 25,
            "numero43": 34,
            "numero44": 44

        }

    def preco(self):
        return self.precos_sem_adicionais[self.numero_pedido]

class PedidoDecorator:
    def __init__(self, pedido):
        self.pedido = pedido

    def preco(self):
        return self.pedido.preco()

class Adicional1(PedidoDecorator):
    def preco(self):
        return self.pedido.preco() + 3

class Adicional2(PedidoDecorator):
    def preco(self):
        return self.pedido.preco() + 5

class Adicional3(PedidoDecorator):
    def preco(self):
        return self.pedido.preco() + 9


if __name__=="__main__":

    pedido = Pedido("numero43")
    
    pedido_ad3 = Adicional3(pedido) # Decorando pedido básico com Adicional 3
    pedido_ad4 = Adicional1(pedido_ad3) # Decorando pedido com Adicional 3 incrementando Adicional 1

    print(pedido_ad4.preco())