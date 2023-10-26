from abc import ABC, abstractmethod

# Classe abstrata que representa o estado da máquina
class EstadoMaquina(ABC):
    @abstractmethod
    def inserir_dinheiro(self, valor):
        pass

    @abstractmethod
    def selecionar_produto(self, produto):
        pass

    @abstractmethod
    def dispensar_produto(self):
        pass

    @abstractmethod
    def retornar_dinheiro(self):
        pass

# Implementação concreta de um estado da máquina: SemCredito
class SemCredito(EstadoMaquina):
    def inserir_dinheiro(self, valor):
        print(f"Você inseriu ${valor}.")
        return ComCredito()

    def selecionar_produto(self, produto):
        print("Por favor, insira dinheiro primeiro.")
        return self

    def dispensar_produto(self):
        print("Por favor, insira dinheiro primeiro.")
        return self

    def retornar_dinheiro(self):
        print("Você não inseriu dinheiro para ser retornado.")
        return self

# Implementação concreta de um estado da máquina: ComCredito
class ComCredito(EstadoMaquina):
    def inserir_dinheiro(self, valor):
        print(f"Você inseriu mais ${valor}.")
        return self

    def selecionar_produto(self, produto):
        print(f"Produto {produto} selecionado. Aguarde a dispensa.")
        return ProdutoSelecionado()

    def dispensar_produto(self):
        print("Você precisa selecionar um produto primeiro.")
        return self

    def retornar_dinheiro(self):
        print("Dinheiro retornado.")
        return SemCredito()

# Implementação concreta de um estado da máquina: ProdutoSelecionado
class ProdutoSelecionado(EstadoMaquina):
    def inserir_dinheiro(self, valor):
        print("Aguarde a dispensa do produto atual.")
        return self

    def selecionar_produto(self, produto):
        print("Aguarde a dispensa do produto atual.")
        return self

    def dispensar_produto(self):
        print("Produto dispensado. Aproveite!")
        return SemCredito()

    def retornar_dinheiro(self):
        print("Você não pode retornar dinheiro depois de selecionar um produto.")
        return self

# Classe que representa a máquina de venda automática. Objeto original (Contexto)
# A variável estado representa o estado atual
# A cada chamada de método ele atualiza esse estado e, portanto, esse métodos executam
# conforme implementado em suas classes
class MaquinaVenda:
    def __init__(self):
        self.estado = SemCredito() # Estado inicial

    def inserir_dinheiro(self, valor):
        self.estado = self.estado.inserir_dinheiro(valor) # Muda para estado Com Crédito

    def selecionar_produto(self, produto):
        self.estado = self.estado.selecionar_produto(produto) # Muda para o estado Produto Selecionado

    def dispensar_produto(self):
        self.estado = self.estado.dispensar_produto() # Volta para o estado Sem Crédito

    def retornar_dinheiro(self):
        self.estado = self.estado.retornar_dinheiro()

# Exemplo de uso da máquina de venda automática
maquina = MaquinaVenda()
maquina.inserir_dinheiro(5)
maquina.selecionar_produto("Biscoito")
maquina.dispensar_produto()
maquina.inserir_dinheiro(2) # Novamente insere dinheiro. Muda para estado Com Crédito
maquina.retornar_dinheiro() # Chama o retornar dinheiro do estado Com Crédito
