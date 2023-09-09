from abc import ABC, abstractmethod # Classe built-in python para definir outras classes ou métodos abstratos

# Componente base. Interface entre os objetos simples e compostos
class ComponenteProduto(ABC):
    @abstractmethod
    def get_preco(self):
        pass

# Classe folha (simples). Representa um único produto
class Produto(ComponenteProduto):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

# Classe composta. Representa uma caixa que contém os produtos
class Caixa(ComponenteProduto):
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)

    def remove_produto(self, produto):
        self.produtos.remove(produto)

    def get_preco(self):
        preco_total = 0

        for prod in self.produtos:
            preco_total += prod.get_preco()
            #preco_total = preco_total + prod.get_preco()

        return preco_total


if __name__=="__main__":

    # Cria o objeto composto Caixa
    cx = Caixa("Presentes")

    # Cria os objetos simples (folhas)
    prod1 = Produto("presente1", 25)
    prod2 = Produto("presente2", 30)

    # Adiciona ao objeto composto
    cx.add_produto(prod1)
    cx.add_produto(prod2)

    # Cria outro objeto composto e adiciona presentes dentro dele
    cx2 = Caixa("Presentes2")
    prod3 = Produto("presente3", 45)
    cx2.add_produto(prod3)

    # Adiciona um objeto cmoposto a outro
    cx.add_produto(cx2)

    total_cx1 = cx.get_preco()
    total_cx2 = cx2.get_preco()
    print(total_cx1)