from abc import ABC, abstractmethod


class Classificador(ABC):
    """
    A classe abstrata define um método padrão que contém um esqueleto de
    algum algoritmo, composto de chamadas para (geralmente) métodos abstratos ou
    pré-definidos.

    Subclasses concretas devem implementar essas operações, mas deixar o
    método padrão em si intacto.
    """

    def template_method(self) -> None:
        """
        Define o esqueleto do algoritmo
        """

        self.predicao_clientes()
        self.create_class_table()
        self.change_column_hook()
        self.db_connection()
        self.create_query()

    def predicao_clientes(self):
        print("Classificando entre promotor ou detrator...")

    def create_class_table(self):
        print("Salvando resultados na tabela")

    @abstractmethod
    def db_connection(self):
        pass

    @abstractmethod
    def create_query(self):
        pass

    def change_column_hook(self):
        pass



class NoSqlDB(Classificador):

    def db_connection(self):
        print("Conectando com banco não relacional...")

    def create_query(self):
        print("Criando query NoSQL...")


class RelationalDB(Classificador):

    def db_connection(self):
        print("Conectando com banco relacional...")

    def create_query(self):
        print("Criando query SQL...")

    def change_column_hook(self):
        print("Mudando nome da coluna..")


def client_code(tipo_banco):

    tipo_banco.template_method()


if __name__ == "__main__":

    ## O mesmo client pode trabalhar com diferentes subclasses

    client_code(NoSqlDB())
    print("")

    client_code(RelationalDB())