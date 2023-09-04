from modulo_pedido.pedido import Cozinha
from modulo_pedido.pedido import Estoque
from modulo_pedido.pedido import Pagamento
from modulo_pedido.pedido import Entrega

if __name__=='__main__':
    prato = 'pizza'
    endereco = "123 Rua Principal"
    valor = 25.0

    cozinha = Cozinha()
    estoque = Estoque()
    pagamento = Pagamento()
    entrega = Entrega()

    if estoque.verificar_ingrediente(prato):
        cozinha.preparar(prato)
        estoque.usar_ingrediente(prato)
        pagamento.processar_pagamento(valor)
        entrega.agendar_entrega(endereco)
        print(f"Pedido de {prato} entregue com sucesso!")
    else:
        print("pedido cancelado")