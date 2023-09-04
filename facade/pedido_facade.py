from modulo_pedido.pedido import Cozinha
from modulo_pedido.pedido import Estoque
from modulo_pedido.pedido import Pagamento
from modulo_pedido.pedido import Entrega

# Facade: PedidoFacade
class PedidoFacade:
    def __init__(self):
        self.cozinha = Cozinha()
        self.estoque = Estoque()
        self.pagamento = Pagamento()
        self.entrega = Entrega()

    def fazer_pedido(self, prato, endereco, valor):
        if self.estoque.verificar_ingrediente(prato):
            self.cozinha.preparar(prato)
            self.estoque.usar_ingrediente(prato)
            self.pagamento.processar_pagamento(valor)
            self.entrega.agendar_entrega(endereco)
            print(f"Pedido de {prato} entregue com sucesso!")