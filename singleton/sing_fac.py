class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = "Conexão com o banco de dados estabelecida"
        return cls._instance


class TableFactory:
    @staticmethod
    def create_table(table_name, db_connection):
        # Use o Factory Method para criar objetos de diferentes tabelas
        if table_name == "users":
            return UsersTable(db_connection)
        elif table_name == "products":
            return ProductsTable(db_connection)
        else:
            raise ValueError(f"Tabela '{table_name}' não suportada.")


class Table:
    def __init__(self, db_connection):
        self.db_connection = db_connection


class UsersTable(Table):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def create_user(self, user_data):
        # Lógica para criar um novo usuário na tabela
        pass


class ProductsTable(Table):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def create_product(self, product_data):
        # Lógica para criar um novo produto na tabela
        pass


# Exemplo de uso
if __name__ == "__main__":
    # Criando uma única instância da conexão com o banco de dados (Singleton)
    db_connection = DatabaseConnection()

    # Usando o Factory Method para criar objetos de diferentes tabelas com a conexão do banco
    users_table = TableFactory.create_table("users", db_connection)
    products_table = TableFactory.create_table("products", db_connection)

    # Realizando operações nas tabelas usando a mesma conexão
    users_table.create_user({"name": "Alice", "email": "alice@example.com"})
    products_table.create_product({"name": "Product A", "price": 19.99})
