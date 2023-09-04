# Subsistema: Cozinha
class Cozinha:
    def preparar(self, prato):
        print(f"Preparando o prato: {prato}")

# Subsistema: Estoque de Ingredientes
class Estoque:
    def verificar_ingrediente(self, ingrediente):
        print(f"Verificando estoque de {ingrediente}")
        return True

    def usar_ingrediente(self, ingrediente):
        print(f"Usando {ingrediente} do estoque")

# Subsistema: Sistema de Pagamento
class Pagamento:
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor}")

# Subsistema: Sistema de Entrega
class Entrega:
    def agendar_entrega(self, endereco):
        print(f"Agendando entrega para {endereco}")